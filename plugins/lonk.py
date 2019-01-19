import json, re

with open("lonk.json") as f:
	global lonk
	lonk = json.load(f)

def repl(m):
	print("Linking {}".format(m.group(0)))
	function_name = m.group(1)
	print(" - Function name {}".format(function_name))
	function_page = lonk["substitutions"][function_name] if function_name in lonk["substitutions"] else function_name
	print(" - Function page {}.html".format(function_page))
	return "<a href='./{}.html'><code>{}()</code></a>".format(function_page,function_name)

template = re.sub(re.escape("[[<code>")+"([^()]+)"+re.escape("()</code>]]"),repl,template)
