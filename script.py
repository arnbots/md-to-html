# -*- coding: utf-8 -*-

'''
CLI tool to transform given files from markdown to html
Example of use:
	script.py *.md
	(this command converts all files in current working directory)

Requirements:
- Pandoc (http://pandoc.org/)
- Python (https://www.python.org/)

'''

import sys
from subprocess import call

for element in sys.argv:
	if(element != __file__):
		newelement = element[:-2] + "html"
		call(["pandoc", element, "-f", "markdown", "-t", "html5", "-s", "-o", newelement])

sys.exit(0)
