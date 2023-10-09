import requests
import subprocess
import json
import os

postman_api_key = os.environ.get('POSTMAN_API_KEY')
postman_api_key_env = os.environ.get('POSTMAN_API_KEY_ENV')
postman_environment_id = os.environ.get('POSTMAN_ENVIRONMENT_ID')
encryption_key = os.environ.get('ENCRYPTION_PASSPHRASE')

POSTMAN_API_URL = f"https://api.postman.com/environments/{postman_environment_id}"

OUTPUT_FILE_JSON = "postman_environment.json"
OUTPUT_FILE_GPG = "encrypted_postman_environment.gpg"

headers = {"X-Api-Key": postman_api_key}
response = requests.get(POSTMAN_API_URL, headers=headers)

if response.status_code == 200:
    with open(OUTPUT_FILE_JSON, "w") as json_file:
        json.dump(response.json(), json_file)
    print("Environment downloaded successfully.")
else:
    print("Failed to fetch the environment from Postman API.")

encryption_command = [
    "gpg", "--batch", "--passphrase", encryption_key, "--symmetric",
    "--cipher-algo", "AES256", "-o", OUTPUT_FILE_GPG, OUTPUT_FILE_JSON
]

try:
    subprocess.run(encryption_command, check=True)
    print(f"File '{OUTPUT_FILE_JSON}' has been encrypted and saved as '{OUTPUT_FILE_GPG}'")
except subprocess.CalledProcessError as e:
    print(f"Encryption failed: {e}")
