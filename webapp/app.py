from flask import Flask, render_template, request, send_from_directory
import os

from webapp.api import api_blueprint
from conversions import convert_units, conversion_maps, prefix_modifiers, ConversionException

app = Flask(__name__)
static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')


@app.route("/", methods=['GET'])
def index():
    return render_template(
        "index.html.j2",
        unit_types=list(conversion_maps.keys()),
        prefix_types=list(prefix_modifiers.keys())
    )


@app.route("/static/<path:path>")
def static_file_handler(path):
    return send_from_directory(static_dir, path)


@app.route("/convert", methods=['POST'])
def convert_result():
    pass


app.register_blueprint(api_blueprint)


def conversion_app():
    user_given_num = request.form["given_num"]
    user_given_prefix = request.form["given_prefix"]
    user_given_unit = request.form["given_unit"]
    user_desired_prefix = request.form["desired_prefix"]
    user_desired_unit = request.form["desired_unit"]
    print(user_given_num)
    print(user_given_prefix)
    print(user_given_unit)
    print(user_desired_prefix)
    print(user_desired_unit)


if __name__ == '__main__':
    app.run(debug=True)