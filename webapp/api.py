from flask import Blueprint
from flask_restplus import Resource, Api, fields
from conversions import conversion_maps, prefix_modifiers, convert_units, ConversionException

api_blueprint = Blueprint('api', __name__, url_prefix="/api/1.0")
api = Api(api_blueprint, version="1.0", title="Simple Unit Converter")


conversion = api.model(
    "Conversion",
    {
        "init_value": fields.Float(description="The input value"),
        "unit1": fields.String(description="The input units"),
        "unit2": fields.String(description="The output units"),
        "unit_type": fields.String(description="The unit type to convert", enum=list(conversion_maps.keys())),
        "prefix1": fields.String(description="The scientific prefix for the input", enum=list(prefix_modifiers.keys())),
        "prefix2": fields.String(description="The scientific prefix for the output", enum=list(prefix_modifiers.keys()))
     }
)

conversion_result = api.model(
    "ConversionResult",
    {
        "result": fields.Float()
    }
)

empty_model = api.model("Empty", {})

conversion_info = api.model(
    "ConversionInfo",
    {
        "prefixes": fields.List(fields.String()),
        "unit_types": fields.Nested(empty_model)
    }
)


@api.route("/converter", methods=["POST", "GET"])
@api.doc(get={'tags': ["Conversion"]}, post={'tags': ["Conversion"]})
class Converter(Resource):
    def get(self):
        return {
            "prefixes": list(prefix_modifiers.keys()),
            "unit_types": {k: list(v.keys()) for k, v in conversion_maps.items()}
        }

    @api.expect(conversion)
    @api.marshal_with(conversion_result)
    def post(self):
        # , init_value, unit1, unit2, conversion_map, prefix1, prefix2
        try:
            new_conversion = api.payload

            conversion_map = conversion_maps[new_conversion["unit_type"]]

            result = convert_units(
                new_conversion["init_value"], new_conversion["unit1"],
                new_conversion["unit2"], conversion_map,
                unit1_prefix=new_conversion["prefix1"], unit2_prefix=new_conversion["prefix2"]
            )
            return {"result": result}, 200
        except ConversionException as e:
            return {"error": str(e)}, 400
