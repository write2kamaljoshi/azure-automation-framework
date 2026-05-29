import pytest
from utils.driver_factory import get_driver
from azure_utils.blob_uploader import upload_report_to_blob


@pytest.fixture()
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


def pytest_sessionfinish(session, exitstatus):

    try:
        upload_report_to_blob()

    except Exception as e:
        print(f"Blob upload failed: {e}")