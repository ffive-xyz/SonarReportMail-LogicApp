from sonarqube.utils.common import strip_trailing_slash
from sonarqube import SonarCloudClient
from dotenv import load_dotenv

from utils import createHtmlCode, getProjects

import os
import requests

load_dotenv()

sonarcloud_url = os.getenv("sonarcloud_url")
sonarcloud_token = os.getenv("sonarcloud_token")
sonarcloud_organization = os.getenv("sonarcloud_organization")
sonarcloud_projects = os.getenv("sonarcloud_projects")
LOGICAPP_URL = os.getenv("LOGICAPP_URL")
metric_keys = os.getenv("metric_keys")

if sonarcloud_organization == None or sonarcloud_projects == None or sonarcloud_token == None or sonarcloud_url == None:
    print("Invalid configuration")

else:
    sonarcloud_url = strip_trailing_slash(sonarcloud_url)
    sonar = SonarCloudClient(sonarcloud_url, sonarcloud_token)

    result = []
    for project in getProjects(sonarcloud_projects):
        branch = None
        if project.find(":") != -1:
            branch = project.split(":")[1]
            project = project.split(":")[0]
            
        component = sonar.measures.get_component_with_specified_measures(
            organization=sonarcloud_organization,
            component=project,
            branch=branch,
            fields="metrics,periods",
            metricKeys=metric_keys)

        result.append({"name": project, "metrics": {}, "branch": branch})
        for metric in component["component"]["measures"]:
            result[-1]["metrics"][metric["metric"]] = metric["value"]

    # print(result)

    html = createHtmlCode(result, sonarcloud_url)

    shouldSendEmail = LOGICAPP_URL != None

    if shouldSendEmail:
        res = requests.post(LOGICAPP_URL, data=html, headers={
                            "Content-Type": "text/plain"})
        print(res.status_code)
    else:
        print(html)
        print("LOGIC APP URL not specified. Email not triggered")
