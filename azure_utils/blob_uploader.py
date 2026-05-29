from datetime import datetime

from azure.storage.blob import BlobServiceClient

from config.config import CONTAINER_NAME
from azure_utils.keyvault_helper import get_secret


def upload_report_to_blob():

    connection_string = get_secret("blob-connection-string")

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string
    )

    container_client = blob_service_client.get_container_client(
        CONTAINER_NAME
    )

    file_path = "reports/report.html"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    blob_name = f"report_{timestamp}.html"

    with open(file_path, "rb") as data:

        container_client.upload_blob(
            name=blob_name,
            data=data,
            overwrite=False
        )

    print(
        f"Report uploaded successfully to Azure Blob Storage as {blob_name}"
    )