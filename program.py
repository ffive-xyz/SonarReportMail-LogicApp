from sonarqube import SonarCloudClient
from dotenv import load_dotenv
import os

load_dotenv()

sonarcloud_url = os.getenv("sonarcloud_url")
sonarcloud_token = os.getenv("sonarcloud_token")

print(sonarcloud_url, sonarcloud_token)