# Unit Converter



This application will allow you to convert between different units and prefixes for various types of measurement. However, there are some issues with accuracy when you get beyond 1e14, especially for temperature, although it will still give you a response. This is due to how floating point numbers are represented. 

Built with Python 3.5

**Note: These links may take a few seconds to load. They are currently hosted on a free dynamo on Heroku that only spins up when requested.**

Link to application: https://convert-this.herokuapp.com/

Link to swagger doc: http://convert-this.herokuapp.com/api/1.0/

These include:

* Length
  * meter
  * inch
  * feet
  * mile
* Pressure
  * psi
  * pascal
  * atm
  * bar
  * mmHg
  * inH2O
* Temperature
  * degrees Celsius
  * degrees Fahrenheit
  * Kelvin
  * Rankine
* Energy
  * joule
  * gram calorie
  * BTU
* Mass
  * gram
  * ounce
  * pound
  * ton
* Time

Also, you can select different prefixes for the units, including ones that you might not see in common use, if ever, like kilo-fahrenheit. 

These include:

* giga 1e9 
* mega 1e6
* kilo 1e3
* no prefix 1e0
* centi 1e-2
* milli 1e-3
* micro 1e-6
* nano 1e-9


The following command will grab the list of possible arguments:

```curl -X GET "http://convert-this.herokuapp.com/api/1.0/converter" -H  "accept: application/json"```

Returns:

```{
  "prefixes": [
    "G",
    "M",
    "k",
    "",
    "c",
    "m",
    "μ",
    "n"
  ],
  "unit_types": {
    "length": [
      "m",
      "mi",
      "in",
      "ft"
    ],
    "pressure": [
      "psi",
      "Pa",
      "atm",
      "bar",
      "mmHg",
      "inH2O"
    ],
    "temp": [
      "deg C",
      "deg F",
      "K",
      "R"
    ],
    "energy": [
      "J",
      "gram cal",
      "BTU"
    ],
    "mass": [
      "g",
      "oz",
      "lb",
      "ton"
    ],
    "time": [
      "s",
      "min",
      "hr",
      "day",
      "week",
      "month",
      "year"
    ]
  }
}
```

An example command to convert from 10mm to inches is:

```curl -X POST "http://convert-this.herokuapp.com/api/1.0/converter" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"init_value\": 10,  \"unit1\": \"m\",  \"unit2\": \"in\",  \"unit_type\": \"length\",  \"prefix1\": \"m\",  \"prefix2\": \"\"}"```

Returns

```
{"result": 0.393701}
```


