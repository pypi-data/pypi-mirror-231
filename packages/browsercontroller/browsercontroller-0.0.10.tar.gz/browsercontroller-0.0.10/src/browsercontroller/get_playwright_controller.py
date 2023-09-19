"""Gets the Playwright website controller and opens it. Prerequisites: pip
install pytest-playwright playwright install.

(Or with anaconda:) conda config --add channels conda-forge conda config
--add channels microsoft conda install playwright
"""

from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Browser, Locator, Page
from typeguard import typechecked


@typechecked
def get_element_by_name_in_html(
    *,
    some_string: str,
    page: Page,
) -> Locator:
    """Returns an object that you can click based on a name in the html string
    of that object."""
    login_button: Locator = page.locator(
        '//button[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", '
        + f'"abcdefghijklmnopqrstuvwxyz"), "{some_string}")]'
    )
    print(f"The login button has text:{login_button.text_content()}")
    return login_button


@typechecked
def get_element_by_xpath_in_html(
    *,
    some_xpath: str,
    page: Page,
) -> Locator:
    """Returns an object that you can click based on a name in the html string
    of that object."""
    some_button: Locator = page.locator(some_xpath)
    return some_button


@typechecked
def initialise_playwright_browsercontroller(
    start_url: str,
) -> tuple[Browser, Page]:
    """
    Creates a Playwright browser, opens a new page, and navigates to a
    specified URL.
    TODO: allow returning the object within the with statement and using it
    outside this function.

    Returns:
        tuple[Browser, Page]: A tuple containing the browser and page objects.
    """
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            if (
                browser_type.name != "webkit"
                and browser_type.name == "firefox"
            ):
                print(f"browser_type={browser_type.name}")
                browser = browser_type.launch()

                # Create a new page and navigate to the URL
                # url = "https://chat.openai.com/auth/login"
                page = browser.new_page()
                page.goto(start_url)

                # Return the browser and page objects
                return browser, page
    raise ValueError("Error: Could not find browser.")
