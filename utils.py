from inspect import getsource
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from IPython.display import HTML
from IPython.display import display
from pygments import highlight

def source(*functions):
    source_code = '\n\n'.join(getsource(fn) for fn in functions)        
    display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))

