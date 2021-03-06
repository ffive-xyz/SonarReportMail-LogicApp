# Sonar Report Mail

A simple python script to email sonarcloud analysis metrics.

_Note:_ This script requires logic app to function properly.

## How to use

Execute `run.bash`

To use this script you need to provide some environment variables either in `dotenv` file or set variables in environment

## .dotenv file sample

```dotenv
sonarcloud_url="https://sonarcloud.io/"
sonarcloud_token="YOUR TOKEN"
sonarcloud_organization="ORGANIZATION_NAME"
sonarcloud_projects="Comma separated project names eg (projectKey, projectKey:branch)"
LOGICAPP_URL="Logic app post url"
metric_keys="code_smells,bugs,vulnerabilities,ncloc,complexity,violations,security_hotspots,sqale_index,coverage,duplicated_lines_density"
```

## setting in pipeline

**Azure pipelines**
``` yaml
steps:
- script: ./run.bash
  displayName: 'Command Line Script'
  env:
    sonarcloud_url: https://sonarcloud.io/
    sonarcloud_organization: ORGANIZATION_NAME
    sonarcloud_projects: Comma separated project names eg (projectKey, projectKey:branch)
    sonarcloud_token: $(sonarcloud_token)
    LOGICAPP_URL: "Logic app post url"
    metric_keys: "code_smells,bugs,vulnerabilities,ncloc,complexity,violations,security_hotspots,sqale_index,coverage,duplicated_lines_density"
```

## Linking with Azure Logic App

- Logic app should be triggered from `http post` request.
- Do not set any request payload data.
- Send email with `http request body` as dynamic property in body.

![sample email](./docs/sampleEmail.png)
