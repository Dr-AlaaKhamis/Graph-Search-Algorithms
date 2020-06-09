from inspect import getsource
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from IPython.display import HTML
from IPython.display import display
from pygments import highlight

#
# prints the source code of a list of functions
# in the jupyter notebook
#

def source(*functions):
    source_code = '\n\n'.join(getsource(fn) for fn in functions)        
    display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))

