from sonarqube import SonarCloudClient
from dotenv import load_dotenv

from utils import createHtmlCode

import os

load_dotenv()

sonarcloud_url = os.getenv("sonarcloud_url")
sonarcloud_token = os.getenv("sonarcloud_token")
sonarcloud_organization = os.getenv("sonarcloud_organization")
sonarcloud_projects = os.getenv("sonarcloud_projects")

if sonarcloud_organization == None or sonarcloud_projects == None or sonarcloud_token == None or sonarcloud_url == None:
    print("Invalid configuration")

else:
    sonar = SonarCloudClient(sonarcloud_url, sonarcloud_token)

    result = []
    for project in sonarcloud_projects.split(','):
        component = sonar.measures.get_component_with_specified_measures(
            organization=sonarcloud_organization,
            component=project,
            fields="metrics,periods",
            metricKeys="code_smells,bugs,vulnerabilities,ncloc,complexity,violations,security_hotspots,sqale_index,coverage,tests,duplicated_lines_density,duplicated_blocks")

        result.append({"name": project, "metrics": {}})
        for metric in component["component"]["measures"]:
            result[-1]["metrics"][metric["metric"]] = metric["value"]

    # print(result)

    print(*createHtmlCode(result), sep='\n')
