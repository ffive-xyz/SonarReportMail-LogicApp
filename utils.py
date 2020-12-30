def createHtmlCode(data):
    lines = []
    lines.append(
        f'<table style="border:1px solid black; border-collapse:collapse;">')

    metrices = list(data[0]['metrics'].keys())

    lines.append(
        f"<tr><th>Project</th><th>{'</th><th>'.join(metrices)}</th></tr>")
    for project in data:
        line = f"<tr><td>{project['name']}</td>"
        for m in metrices:
            line += f"<td>{project['metrics'][m]}</td>"
        line += '</tr>'
        lines.append(line)

    lines.append(f'</table>')

    lines = list(map(makePretty, lines))

    return lines


def addStyle(line):
    line = line.replace(
        "<th>", "<th style='border:1px solid black; padding: 5px; text-align: center;'>")
    line = line.replace(
        "<td>", "<td style='border:1px solid black; padding: 5px;  text-align: center;'>")
    return line


def makeHumanHeaders(line):
    line = line.replace("coverage", "Coverage")
    line = line.replace("complexity", "Complexity")
    line = line.replace("complexity", "Complexity")
    line = line.replace("bugs", "Bugs")
    line = line.replace("code_smells", "Code Smells")
    line = line.replace("duplicated_lines_density", "Duplicated Lines")
    line = line.replace("tests", "Unit Tests")
    line = line.replace("duplicated_blocks", "Duplicated Blocks")
    line = line.replace("ncloc", "#LOC")
    line = line.replace("violations", "Violations")
    line = line.replace("vulnerabilities", "Vulnerabilities")
    line = line.replace("security_hotspots", "Security Hotspots")
    line = line.replace("sqale_index", "Debt")

    return line


def makePretty(line):
    line = addStyle(line)
    line = makeHumanHeaders(line)
    return line
