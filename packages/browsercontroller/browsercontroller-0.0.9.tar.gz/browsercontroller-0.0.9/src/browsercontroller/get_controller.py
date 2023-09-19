"""Gets a website controller and opens it."""
import os
import sys
import time
from typing import Any, Optional

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from typeguard import typechecked
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from browsercontroller.Hardcoded import Hardcoded, get_default_profile_dir
from browsercontroller.helper import get_browser_drivers, open_url


# pylint: disable=R0903
class OSType:
    """Was not able to import this class from pip webdriver_manager.utils."""

    LINUX = "linux"
    MAC = "mac"
    WIN = "win"


@typechecked
def os_name() -> str:
    """Returns the name of the operating system.

    Was not able to import this function from pip
    webdriver_manager.utils.
    """
    pl = sys.platform
    if pl in ["linux", "linux2"]:
        return OSType.LINUX
    if pl == "darwin":
        return OSType.MAC
    if pl == "win32":
        return OSType.WIN
    raise ValueError(f"Error, did not support os: {pl}.")


# pylint: disable=R0903
# pylint: disable=R0913
@typechecked
def get_ubuntu_apt_firefox_controller(
    *,
    url: str,
    default_profile: bool = False,
) -> webdriver:
    """Initialises object that gets the browser controller, then it gets the
    issues from the source repo, and copies them to the target repo."""

    # Store the hardcoded values used within this project
    hardcoded = Hardcoded()

    # get browser drivers
    get_browser_drivers(hardcoded)
    driver = initialise_website_controller(default_profile=default_profile)
    time.sleep(1)

    # Go to extension settings.
    driver = open_url(
        driver,
        url,
    )
    time.sleep(1)
    # Load again to allow the history to be dropped.
    driver = open_url(
        driver,
        url,
    )
    time.sleep(1)
    return driver


# pylint: disable=R0903
@typechecked
def initialise_website_controller(
    *,
    default_profile: bool,
    browser_name: Optional[str] = "chrome",
    clear_cookies: Optional[bool] = True,
) -> Any:
    """Constructs object that controls a firefox browser.

    TODO: Allow user to switch between running browser
    in background or foreground.
    """
    Hardcoded()
    # To run Firefox browser in foreground
    print("Loading geckodriver")
    path_to_chromedriver: str = f"{os.getcwd()}/chrome_driver/chromedriver114"
    print(f"path_to_chromedriver={path_to_chromedriver}")

    if browser_name == "firefox":
        # path_to_geckodriver:str = f"{os.getcwd()}/firefox_driver/geckodriver"
        binary_location = {
            OSType.LINUX: "/snap/firefox/3131/usr/lib/firefox/firefox",
            # OSType.LINUX: path_to_geckodriver,
        }[os_name()]
        option = webdriver.FirefoxOptions()
        option.binary_location = binary_location
        option.set_preference("useAutomationExtension", False)
        option.set_preference("dom.webdriver.enabled", False)
        option.add_argument("--disable-blink-features=AutomationControlled")

        if default_profile:
            option.add_argument("-profile")
            option.add_argument(get_default_profile_dir())
        else:
            option.add_argument("-private")

            # First trying to launch Firefox without installing it,
            # to evade rate-limits from driver download. If it does not work
            # Uncomment the install and run it manually, once.
            driver = webdriver.Firefox(
                options=option,
                service=FirefoxService(),
                # service=FirefoxService(GeckoDriverManager().install()),
            )

    if browser_name == "chrome":
        # Requires snap install chromium.
        binary_location = {
            # OSType.LINUX: path_to_chromedriver,
            OSType.LINUX: (
                "/snap/chromium/2623/usr/lib/chromium-browser/chrome"
            ),
        }[os_name()]
        option = webdriver.ChromeOptions()
        option.binary_location = binary_location

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser_name == "brave":
        binary_location = {
            OSType.LINUX: "/snap/brave/277/opt/brave.com/brave/brave-browser",
        }[os_name()]

        option = webdriver.ChromeOptions()
        option.binary_location = binary_location
        driver = webdriver.Chrome(
            options=option,
            service=ChromeService(
                ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
            ),
        )

    # clear cookies
    if clear_cookies:
        driver.delete_all_cookies()

    return driver

    # To run Firefox browser in background
    # os.environ["MOZ_HEADLESS"] = "1"
    # self.driver = webdriver.Firefox(
    # executable_path=r"firefox_driver/geckodriver")

    # To run Chrome browser in background
    # options = webdriver.ChromeOptions();
    # options.add_argument('headless');
    # options.add_argument('window-size=1200x600'); // optional
