import os, re
lines = ["<ul class='list-group'>"]
if not path.startswith("index"):
	lines.append("<li class='list-group-item'><a href='./index.html'>Back to Home</a></li>")
for item in sorted(os.listdir("in")):
	if item=="index.md": continue
	with open("in/"+item) as f:
		title = re.search(re.escape("<!-- attrib title: ")+"(.*)"+re.escape(" -->"),f.read()).group(1).replace(" - PICO-8 Wiki","")
	if item==path or item==path.replace(".html",".md"): lines.append("<li class='list-group-item'><b>{}</b></li>".format(title))
	else:
		lines.append("<li class='list-group-item'><a href='./{}'>{}</a></li>".format(item.replace(".md",".html"),title))
lines.append("</ul>")

template = template.replace("[#sidebar#]","\n".join(lines))
