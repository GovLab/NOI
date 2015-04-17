import glob
import os
import yaml
from slugify import slugify

from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'

CONTENT = yaml.load(open('data/content.yaml'))

def Main():
	env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), extensions=['jinja2.ext.with_'])

	template = env.get_template('index.html')
	html = template.render({ 'EXPERTISES': CONTENT['expertises'], 'SECTORS': CONTENT['sectors'],
		'OPENDATA': CONTENT['open-data']})
	with open('index.html', 'w') as f:
		f.write(html.encode('utf8'))
		f.close()

if __name__ == '__main__':
  Main()