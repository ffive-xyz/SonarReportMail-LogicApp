def createHtmlCode(data):
    lines = []
    lines.append(
        f'<table style="border:1px solid black; border-collapse:collapse;">')
    
    metrices = list(data[0]['metrics'].keys());

    lines.append(
        f"<tr><th>Project</th><th>{'</th><th>'.join(metrices)}</th></tr>")
    for project in data:
        line = f"<tr><td>{project['name']}</td>"
        for m in metrices:
            line += f"<td>{project['metrics'][m]}</td>"
        line += '</tr>'
        lines.append(line)
    
    lines.append(f'</table>')

    return lines
