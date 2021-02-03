import urllib.parse


def createHtmlCode(data, sonarcloud_url):
    lines = []
    metrices = list(data[0]['metrics'].keys())

    for project in data:
        projectName = project['name']
        projectLines = []

        displayProjectName = projectName
        branch = project['branch']
        if branch is not None:
            displayProjectName = f"{projectName}:{branch}"

        projectLines += [f'<div class="card">']

        projectLines += [
            f'<div class="name"><a href="{sonarcloud_url}/dashboard?id={projectName}">{displayProjectName}</a></div>']

        projectLines += ['''<table class="stats">
                    <tr class="stat">
                    ''']

        line = ''
        for m in metrices:
            line += f"<td><a href='{sonarcloud_url}/component_measures?id={projectName}&metric={m}&view=list'>{project['metrics'][m]}</a></td>"
        projectLines += [line]

        projectLines += ['</tr>']
        projectLines += ['<tr class="stat">']

        line = ''
        for m in metrices:
            line += f"<th>{m}</th>"
        projectLines += [line]

        projectLines += ['</tr>']
        projectLines += ['</table>']
        projectLines += ['</div><br />']

        if branch is not None:
            branch = urllib.parse.quote(branch, safe='')
            projectLines = list(
                map(lambda x: addBranch(branch, x), projectLines))

        lines.extend(projectLines)

    lines = list(map(makeHumanHeaders, lines))

    template = getEmailTemplate()
    return insertDataInTemplate(template, ''.join(lines))


def makeHumanHeaders(line):
    line = line.replace(">coverage<", ">Test Coverage<")
    line = line.replace(">complexity<", ">Complexity<")
    line = line.replace(">bugs<", ">Bugs<")
    line = line.replace(">code_smells<", ">Code Smells<")
    line = line.replace(">duplicated_lines_density<", ">Duplicated Lines<")
    line = line.replace(">duplicated_blocks<", ">Duplicated Blocks<")
    line = line.replace(">ncloc<", ">#LOC<")
    line = line.replace(">violations<", ">Violations<")
    line = line.replace(">vulnerabilities<", ">Vulnerabilities<")
    line = line.replace(">security_hotspots<", ">Security Hotspots<")
    line = line.replace(">sqale_index<", ">Debt<")

    return line


def addBranch(branch, line):
    return line.replace("?id=", f"?branch={branch}&id=")


def getEmailTemplate():
    html = ''
    with open('emailTemplate.html') as f:
        html = ''.join(f.readlines())
    return html


def insertDataInTemplate(template, data):
    return template.replace("</body>", f'{data}</body>')


def getProjects(rawString):
    l = rawString.split(',')
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l
