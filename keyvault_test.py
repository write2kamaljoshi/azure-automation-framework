from azure_utils.keyvault_helper import get_secret

email = get_secret("automation-email")

print(email)