from collections import namedtuple, OrderedDict

"""
   Conversion is used to store specific forward and inverse functions, specifically for temperature conversions. 
   This is done because the conversion process
   usually isn't just a single operation. Using two dictionaries had been necessary, before introducing this
   method, due to the conversion paradigm. The namedtuple allows a normal dictionary to hold two related
   elements in one value space, so that either the forward or reverse conversion equation can be used.
"""
Conversion = namedtuple('Conversion', ('forward', 'inverse'))

# List of SI prefixes that can be used to modify the given or desired units.
prefix_modifiers = OrderedDict([
    ('G', 1e9),
    ('M', 1e6),
    ('k', 1e3),
    ('', 1e0),
    ('c', 1e-2),
    ('m', 1e-3),
    ('μ', 1e-6),
    ('n', 1e-9)
])

"""
 The conversion paradigm is that any conversion is carried out through a common or base unit. This means that every
   conversion must convert to it, if the base unit is not already the given or desired unit.
                       EX: inches -> ft is actually, inches -> meters -> feet.

 Should any additional units be added, the conversion number listed must be the factor to convert from the base unit to
   the new unit. This is true for all cases, except new temperature units.
                       EX: Adding inches meant using the conversion factor from meters to inches (39.3701)
"""

# Meter is base unit of conversion.
length_conversions = {
    "m": 1.0,
    "mi": 0.000621371,
    "in": 39.3701,
    "ft": 3.28084
}

# psi is base unit of conversion
pressure_conversions = {
    "psi": 1.0,
    "Pa": 6894.76,
    "atm": 0.068046,
    "bar": 0.0689476,
    "mmHg": 51.71484,
    "inH2O": 27.7076
}

"""
 The conversion paradigm for temperature is similar to the other units in that it is carried out through a base unit.
   However, because it requires an equation beyond a single operation, the inverse equation must be defined to allow
   conversion to and from the base unit.
                       EX A: From celsius to fahrenheit is (9*x/5) + 32, where x is the temperature in celsius.
                       EX B: From fahrenheit to celsius is (x-32)*(5/9)), where x is the temperature in fahrenheit.
"""
# Celsius is the base unit for conversionx
temp_conversions = {
    "deg C": Conversion(lambda x: x, lambda x: x),
    "deg F": Conversion(lambda x: (9*x/5) + 32, lambda x: (x-32)*(5/9)),
    "K": Conversion(lambda x: x+273.15, lambda x: x-273.15),
    "R": Conversion(lambda x: ((9*x/5) + 491.67), lambda x: (x-491.67)*(5/9))
}

# Joule is base unit of conversion
energy_conversions = {
    "J": 1.0,
    "gram cal": 0.239006,
    "BTU": 0.000947817,
}

# Kilogram is base unit of conversion
mass_conversions = {
    "g": 1000,
    "oz": 35.274,
    "lb": 2.20462,
    "ton": 0.00110231
}


conversion_maps = {
    'length': length_conversions,
    'pressure': pressure_conversions,
    'temp': temp_conversions,
    'energy': energy_conversions,
    'mass': mass_conversions
}


class ConversionException(Exception):
    pass


class InvalidUnitException(ConversionException):
    pass


class InvalidPrefixException(ConversionException):
    pass


class InvalidInputException(ConversionException):
    pass


def convert_units(initial_value, unit1, unit2, conversion_map, unit1_prefix=None, unit2_prefix=None):
    if not isinstance(initial_value, (float, int)):
        raise InvalidInputException("Input value {0} is not a numeric type.".format(initial_value))

    if unit1 not in conversion_map:
        raise InvalidUnitException("Unit {0} is not a valid unit for this conversion.".format(unit1))

    if unit2 not in conversion_map:
        raise InvalidUnitException("Unit {0} is not a valid unit for this conversion.".format(unit2))

    if unit1_prefix is not None and unit1_prefix not in prefix_modifiers:
        raise InvalidPrefixException("Prefix {0} is not a valid unit prefix.".format(unit1_prefix))

    if unit2_prefix is not None and unit2_prefix not in prefix_modifiers:
        raise InvalidPrefixException("Prefix {0} is not a valid unit prefix.".format(unit2_prefix))

    unit1_conversion = conversion_map[unit1]
    unit2_conversion = conversion_map[unit2]
    current_value = initial_value

    # if unit1_prefix is not None:
    #     current_value *= prefix_modifiers[unit1_prefix]

    current_value *= (prefix_modifiers.get(unit1_prefix, 1.0)/prefix_modifiers.get(unit2_prefix, 1.0))

    if isinstance(unit1_conversion, (float, int)):
        current_value = (current_value / unit1_conversion) * unit2_conversion

    elif isinstance(unit1_conversion, Conversion):
        current_value = initial_value*prefix_modifiers.get(unit1_prefix)
        current_value = unit2_conversion.forward(unit1_conversion.inverse(current_value))/prefix_modifiers.get(unit2_prefix)
    else:
        assert False
    # if unit2_prefix is not None:
    #     current_value /= prefix_modifiers[unit2_prefix]
    return current_value
