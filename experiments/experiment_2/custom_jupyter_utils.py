import base64
from IPython.display import display, Javascript
from urllib.parse import quote

import snowballing.jupyter_utils


def display_cell(text):
    encoded_code = base64.b64encode(quote(text.encode()).encode()).decode()
    display(Javascript("""
        $('span:contains("# Temp")').closest('.cell').remove();
        var code = IPython.notebook.insert_cell_{0}('code');
        var prompt = code.element.find(".input_prompt");
        prompt.append('<br><button style="height: 100%; width: 54px;">Run</button>');
        prompt.on("click", "button", function(){{
            code.execute();
        }});
        code.set_text(decodeURIComponent(window.atob("{1}")));
    """.format('below', encoded_code)))
    
snowballing.jupyter_utils.display_cell = display_cell
import snowballing.snowballing
snowballing.snowballing.display_cell = display_cell