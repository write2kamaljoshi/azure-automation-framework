# from azure.identity import DefaultAzureCredential
# from azure.keyvault.secrets import SecretClient
#
#
# KEY_VAULT_URL = "https://kv-sdet-learning-01.vault.azure.net/"
#
#
# credential = DefaultAzureCredential()
#
# client = SecretClient(
#     vault_url=KEY_VAULT_URL,
#     credential=credential
# )
#
#
# def get_secret(secret_name):
#
#     retrieved_secret = client.get_secret(secret_name)
#
#     return retrieved_secret.value
#
#
# from azure.identity import DefaultAzureCredential
# from azure.keyvault.secrets import SecretClient
#
# KEY_VAULT_URL = "https://kv-sdet-learning-01.vault.azure.net/"
#
#
# def get_secret(secret_name):
#
#     credential = DefaultAzureCredential()
#
#     client = SecretClient(
#         vault_url=KEY_VAULT_URL,
#         credential=credential
#     )
#
#     return client.get_secret(secret_name).value


import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_URL = "https://kv-sdet-learning-01.vault.azure.net/"


def get_secret(secret_name):

    import os

    print("ENV VARIABLES:")

    for key in os.environ:
        if "automation" in key.lower() or "blob" in key.lower():
            print(key)

    value = os.getenv(secret_name)

    print(f"Looking for secret: {secret_name}")
    print(f"Found in env? {value is not None}")

    if value:
        return value

    print("Using Key Vault SDK")

    credential = DefaultAzureCredential()

    client = SecretClient(
        vault_url=KEY_VAULT_URL,
        credential=credential
    )

    return client.get_secret(secret_name).value