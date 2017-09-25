#!/usr/bin/python
import os
import shutil
from dateutil.parser import parse as parse_date

from jinja2 import FileSystemLoader, Environment, contextfilter


TEMPLATES_PATH = 'templates'
STATIC_PATH = 'static'
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'


@contextfilter
def relative_url(context, targetpath):
    basepath = context['page']
    basedir = os.path.dirname(basepath)
    targetdir = os.path.dirname(os.path.join('.', targetpath))
    diff = os.path.relpath(targetdir, basedir)
    return os.path.join(diff, os.path.basename(targetpath))


def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format)


class Genja(object):
    def __init__(self, *, templates=None, static=None, content=None, output=None):
        self._templates = TEMPLATES_PATH if templates is None else templates
        self._static = STATIC_PATH if static is None else static
        self._content = CONTENT_PATH if content is None else content
        self._output = OUTPUT_PATH if output is None else output
        
    def clean(self):
        # Remove output directory content if it exists
        if os.path.exists(self._output):
            for (dirpath, dirnames, filenames) in os.walk(self._output):
                for filename in filenames:
                    os.unlink(os.path.join(dirpath, filename))
                for dirname in dirnames:
                    shutil.rmtree(os.path.join(dirpath, dirname))
        else:
            os.makedirs(self._output, exist_ok=True)
    
    def build(self):
        self._build_content()
        self._build_static()
        
    def watch(self):
        pass
    
    def serve(self):
        pass
    
    def _build_static(self):
        # Copy static content
        for item in os.listdir(self._static):
            source = os.path.join(self._static, item)
            destination = os.path.join(self._output, item)
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)
        
    
    def _build_content(self):
        # Create environment for Jinja2
        env = Environment(
            loader=FileSystemLoader([self._templates, self._content]),
        )
        
        # Configure environment
        env.globals.update({
        
        })
        env.filters.update({
            'relative': relative_url,
            'parse_date': parse_date,
            'date': format_date,
        })
        
        # Render all *.html pages if the name does not start with an underscore
        for (dirpath, dirnames, filenames) in os.walk(self._content):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)[len(self._content) + 1:]
                
                if filepath.startswith('_') or not filepath.endswith('.html'):
                    print('Ignoring {}'.format(filepath))
                    continue
                print('Rendering {}'.format(filepath))
                template = env.get_template(filepath)
                
                # Create output file
                output_filepath = os.path.join(self._output, filepath)
                os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                with open(output_filepath, 'w') as f:
                    rendered = template.render(
                        page=filepath,
                    )
                    f.write(rendered)


if __name__ == '__main__':
    genja = Genja()
    genja.clean()
    genja.build()
