import flask
import yaml
import logging
import django
from flask import render_template_string

app = flask.Flask(__name__)
logging.basicConfig(level=logging.INFO)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            font-family: 'Courier New', Courier, monospace; 
            text-align: center; 
            padding-top: 50px; 
            background-color: #f4f4f4;
            color: #333;
        }
        .content { 
            font-size: 14px; 
            line-height: 1.6;
            margin-bottom: 40px; 
        }
        .meta { 
            font-size: 11px; 
            color: #999; 
            border-top: 1px solid #eee; 
            padding-top: 15px;
        }
    </style>
</head>
<body>
        <div class="content">
            <p>Witamy w systemie Archwium.</p>
        </div>

        <div class="meta">
            Flask Framework v{{ flask_v }} | YAML Parser v{{ yaml_v }} | Django Core v{{ django_v }}
        </div>
    </div>
</body>
</html>
"""


@app.route('/', methods=['GET'])
def index():
    logging.info(f"Używane wersje: Flask {flask.__version__}, PyYAML {yaml.__version__}")

    return render_template_string(HTML_TEMPLATE,
                                  flask_v=flask.__version__,
                                  yaml_v=yaml.__version__,
                                  django_v=django.get_version())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
