from pylatex.utils import escape_latex, bold, italic, NoEscape

def link(section, text):
    text = escape_latex(text)
    return NoEscape(r'\hyperref[' + section + ']{' + text + '}')

def label(text, section='subsec'):
    return section + ':' + text.replace(' ', '').replace('_', '').replace('-', '{-}')

def format_def(k, v):
    return bold(k) + NoEscape(' - ') + NoEscape(v)

def add_text(section, title, text):
    with section.create(MiniPage(align='l')):
        section.append(bold(title))
        section.append(LineBreak())
        section.append(text)
    section.append(LineBreak())
    section.append(LineBreak())