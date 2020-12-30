def createHtmlCode(data, sonarcloud_url):
    lines = []
    metrices = list(data[0]['metrics'].keys())

    for project in data:
        projectName = project['name']

        lines += [f'<div class="card">']

        lines += [
            f'<div class="name"><a href="{sonarcloud_url}/dashboard?id={projectName}">{projectName}</a></div>']

        lines += ['''<table class="stats">
                    <tr class="stat">
                    ''']

        line = ''
        for m in metrices:
            line += f"<td><a href='{sonarcloud_url}/component_measures?id={projectName}&metric={m}&view=list'>{project['metrics'][m]}</a></td>"
        lines += [line]

        lines += ['</tr>']
        lines += ['<tr class="stat">']

        line = ''
        for m in metrices:
            line += f"<th>{m}</th>"
        lines += [line]

        lines += ['</tr>']
        lines += ['</table>']
        lines += ['</div><br />']

    lines = list(map(makePretty, lines))

    template = getEmailTemplate()
    return insertDataInTemplate(template, ''.join(lines))


def makeHumanHeaders(line):
    line = line.replace(">coverage<", ">Coverage<")
    line = line.replace(">complexity<", ">Complexity<")
    line = line.replace(">complexity<", ">Complexity<")
    line = line.replace(">bugs<", ">Bugs<")
    line = line.replace(">code_smells<", ">Code Smells<")
    line = line.replace(">duplicated_lines_density<", ">Duplicated Lines<")
    line = line.replace(">tests<", ">Unit Tests<")
    line = line.replace(">duplicated_blocks<", ">Duplicated Blocks<")
    line = line.replace(">ncloc<", ">#LOC<")
    line = line.replace(">violations<", ">Violations<")
    line = line.replace(">vulnerabilities<", ">Vulnerabilities<")
    line = line.replace(">security_hotspots<", ">Security Hotspots<")
    line = line.replace(">sqale_index<", ">Debt<")

    return line


def makePretty(line):
    line = makeHumanHeaders(line)
    return line


def getEmailTemplate():
    html = ''
    with open('emailTemplate.html') as f:
        html = ''.join(f.readlines())
    return html


def insertDataInTemplate(template, data):
    return template.replace("</body>", f'{data}</body>')
