import csv
from datetime import date
from logging import getLogger
import requests
import time
from typing import Dict, List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logger = getLogger(__name__)


def initialize_service(user: str, password: str) -> webdriver:
    """If you disable 2FA it won't allow you to sign in,
    you need to have another email account for recovery.
    Service: Could be changed to ChromeService(ChromeDriverManager().install()),
    but is very unrelaiable.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    try:
        driver = login_google(driver, identifier=user, Passwd=password)
    except Exception as e:
        logger.error(f"An error occurred during login: {str(e)}")
    return driver


def login_google(driver: webdriver, **kwargs) -> webdriver:
    """Log in to Google services using Webdriver
    Using WebDriverWait() instead of time.sleep() as suggested by the docs.
    The password element has different terms for the input field and the button.

    Args:
        driver (webdriver): Selenium webdriver used to log in
        **kwargs (dict): User and password

    Returns:
        webdriver: Initialised driver with the log in.
    """
    driver.get("https://accounts.google.com/ServiceLogin")
    driver_wait = WebDriverWait(driver, 4)
    for field, value in kwargs.items():
        driver_wait.until(EC.presence_of_element_located(
            (By.NAME, field)
        )).send_keys(value)
        if str(field) == "Passwd":
            field = "password"
        parent_button = driver_wait.until(EC.element_to_be_clickable(
            (By.ID, str(field) + "Next"))
        )
        parent_button.find_element(By.TAG_NAME, "button").click()
    return driver


def build_report_url(
    gb_account: str, start_date: str, end_date: str
) -> Tuple[str, Dict]:
    """Cast the dates, build the url and params

    Args:
        gb_account (str): Numeric representation of the GB acc
        start_date (str): Start date for the report
        end_date (str): End date for the report

    Returns:
        (str, dict): url to download the report, params for the request
    """
    start = date.fromisoformat(start_date).strftime("%Y,%-m,%-d")
    end = date.fromisoformat(end_date).strftime("%Y,%-m,%-d")
    report_url = (
        f"https://play.google.com/books/publish/u/0/a/{gb_account}/"
        "downloadTrafficReport"
    )
    params = {"f.req": f"[[null,{start}],[null,{end}],2,0]"}
    return report_url, params


def get_report(report_url: str, driver: webdriver, params: Dict) -> str:
    """Once logged in Google, make a request to get the actual report.
    Gets the cookies from the selenium driver to allow you in.
    Sleep 5 seconds needed when you run the driver the first time as it's slow

    Args:
        report_url (str): url before the params
        driver (webdriver): driver needed to get the cookies
    Returns:
        str: decoded content csv from response
    """
    time.sleep(5)
    session = requests.Session()
    cookies = {
        cookie["name"]: cookie["value"]
        for cookie in driver.get_cookies()
        if cookie["domain"] == ".google.com"
    }
    response = session.get(report_url, cookies=cookies, params=params)
    if response.status_code != 200:
        raise OSError(
            "Bad response: ",
            response.status_code,
            "Message: ",
            response.content
        )

    return response.content.decode("utf-16")


def required_fields_present(
        required_fields: list[str],
        all_fields: list[str],
) -> set[str]:
    """Return any values in required_fields that are missing from all_fields."""
    return set(required_fields) - set(all_fields)


def extract_report_content(report_content, expected_headers=None) -> List[Dict]:
    """Process Google Play Books report content, returning structured data.

    Args:
        report_content (str): Google Books Report content.
        expected_headers (list, optional): List of headers expected.
    Returns:
        list_results list[dict]: CSV content as list of dict objects.
    """
    reader = csv.DictReader(report_content.splitlines(), delimiter="\t")
    headers = reader.fieldnames

    expected_headers = expected_headers or []
    if missing_fields := required_fields_present(expected_headers, headers):
        raise ValueError(f"Required headers missing: {missing_fields}")

    return list(reader)


def fetch_report(
        gb_account: str,
        user: str,
        password: str,
        start_date: str,
        end_date: str,
) -> str:
    """Initialise Selenium, log in to Google, fetch the Google Books report.

    Args:
        gb_account (str): Numeric str representing the account.
        user (str): Username or email.
        password (str): Password.
        start_date (str): Start date for the report.
        end_date (str): End date for the report.

    Returns:
        str: CSV response from Google Play Books.
    """
    service = initialize_service(user, password)
    report_url, params = build_report_url(gb_account, start_date, end_date)

    try:
        report_content = get_report(report_url, service, params)
    except (AttributeError, UnicodeDecodeError, ValueError) as err:
        logger.error(
            f"Failed to retrieve report {start_date}, {end_date}, "
            f"Error: {err}"
        )
        raise err
    finally:
        service.close()

    return report_content


"""
Use Cases 1: User has a CSV file
with open(csv_file, "r", encoding="utf-16") as f:
    results = f.read()


Use Cases 2: User wants to fetch data from Google Books site
results = fetch_report(
    gb_account, user, password, start_date, end_date, path_to_driver
)

Both Cases: After content is extracted from GB Report:
extract_report_content(results)
"""
