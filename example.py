import os, sys
from pylatex import *
from pylatex.utils import *
from util.util import *

def generate(path):
    document_options = ['a4']
    geometry_options = {
        'tmargin': '0.5in',
        'bmargin': '0.5in',
        'lmargin': '0.5in',
        'rmargin': '0.5in'
    }
    doc = Document(
        path,
        geometry_options=geometry_options,
        document_options=document_options,
        page_numbers=False
    )
    doc.packages.append(Package('lastpage'))
    doc.packages.append(Package('chngcntr'))
    doc.packages.append(Package('float'))
    doc.packages.append(Package('array'))
    doc.packages.append(NoEscape(r'\counterwithin{figure}{section}'))
    doc.packages.append(NoEscape(r'\usepackage[hidelinks]{hyperref}'))
    doc.packages.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=black, urlcolor=blue}'))
    doc.packages.append(NoEscape(r'\urlstyle{same}'))

    with doc.create(Section("Hello World")) as section:
        section.append("abc123")

    doc.append(NewPage())

    print(f'Generating PDF: {path}')
    doc.generate_pdf(path, clean=True, compiler='latexmk')

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./Example")) if len(sys.argv) < 2 else sys.argv[1]
    generate(path)