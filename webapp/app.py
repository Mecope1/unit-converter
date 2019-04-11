from flask import Flask, render_template, request, send_from_directory, json, redirect
import os

from webapp.api import api_blueprint
from conversions import convert_units, conversion_maps, prefix_modifiers, ConversionException, __version__

app = Flask(__name__)
static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')


@app.route("/", methods=['GET'])
def index():
    return render_template(
        "index.html.j2",
        unit_types=list(conversion_maps.keys()),
        prefix_types=list(prefix_modifiers.keys()),
        version=__version__,
        json=json,
        result="n/a",
        unit_map={k: list(v.keys()) for k, v in conversion_maps.items()},
        defaults={}
    )


@app.route("/static/<path:path>")
def static_file_handler(path):
    return send_from_directory(static_dir, path)


@app.route("/convert", methods=['GET'])
def convert_redirect():
    return redirect("/")


@app.route("/convert", methods=['POST'])
def convert_result():
    try:
        user_unit_type = request.form["unit_type"]
        user_given_num = float(request.form["given_num"])
        user_given_prefix = request.form["given_prefix"]
        user_given_unit = request.form["given_unit"]
        user_desired_prefix = request.form["desired_prefix"]
        user_desired_unit = request.form["desired_unit"]
        conversion_map = conversion_maps[user_unit_type]
        result = convert_units(
            user_given_num, user_given_unit, user_desired_unit,
            conversion_map, user_given_prefix, user_desired_prefix
        )
        return render_template(
            "index.html.j2",
            unit_types=list(conversion_maps.keys()),
            prefix_types=list(prefix_modifiers.keys()),
            version=__version__,
            json=json,
            result="{0} {1}{2}".format(result, user_desired_prefix, user_desired_unit),
            unit_map={k: list(v.keys()) for k, v in conversion_maps.items()},
            defaults=dict(request.form)
        )
    except Exception as e:
        return str(e), 400


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