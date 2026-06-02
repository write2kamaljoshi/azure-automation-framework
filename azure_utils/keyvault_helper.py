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


from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_URL = "https://kv-sdet-learning-01.vault.azure.net/"


def get_secret(secret_name):

    credential = DefaultAzureCredential()

    client = SecretClient(
        vault_url=KEY_VAULT_URL,
        credential=credential
    )

    return client.get_secret(secret_name).value