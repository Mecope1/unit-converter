import unittest
from assertpy import assert_that
from conversions import *


class ConversionsTest(unittest.TestCase):
    def test_length_conversions(self):

        # Test 1: non base unit conversions with prefixes
        result1 = convert_units(24000.0, 'in', 'ft', length_conversions, 'c', 'k')
        true_value = 0.02
        assert_that(result1).is_between(0.99999*true_value, 1.00001*true_value)

    def test_pressure_conversions(self):
        # Test 1: non base unit conversions with prefixes
        result1 = convert_units(2.0, 'atm', 'Pa', pressure_conversions, 'c', 'k')
        true_value = 2.0265
        assert_that(result1).is_between(0.99999*true_value, 1.00001*true_value)

    def test_temperature_conversions(self):
        # Test 1: non base unit conversions with prefixes
        result1 = convert_units(100, 'deg C', 'R', temp_conversions, 'c', 'k')
        true_value = 0.49347
        assert_that(result1).is_between(0.99999*true_value, 1.00001*true_value)

    def test_energy_conversions(self):
        # Test 1: non base unit conversions with prefixes
        result1 = convert_units(200000, 'BTU', 'gram cal', energy_conversions, 'c', 'k')
        true_value = 504.3288
        assert_that(result1).is_between(0.99999*true_value, 1.00001*true_value)

    def test_mass_conversions(self):
        # Test 1: non base unit conversions with prefixes
        result1 = convert_units(200.0, 'ton', 'oz', mass_conversions, 'c', 'k')
        true_value = 64
        assert_that(result1).is_between(0.99999*true_value, 1.00001*true_value)

    def test_same_to_same_behavior(self):
        for unit_type, conv_map in conversion_maps.items():
            for unit in conv_map.keys():
                for prefix in prefix_modifiers:
                    for i in range(0, 1000):
                        assert_that(
                            convert_units(float(i), unit, unit, conv_map, unit1_prefix=prefix, unit2_prefix=prefix)
                        ).is_between((0.9999*float(i)) - 1e-4, (1.0001*float(i) + 1e-4))

    def test_exceptions(self):
        self.assertRaises(
            InvalidInputException,
            convert_units, "foo", "m", "m", length_conversions
        )

        self.assertRaises(
            InvalidUnitException,
            convert_units, 1.0, "asd", "m", length_conversions
        )

        self.assertRaises(
            InvalidUnitException,
            convert_units, 1.0, "m", "asd", length_conversions
        )

        self.assertRaises(
            InvalidPrefixException,
            convert_units, 1.0, "m", "m", length_conversions, unit1_prefix="foo"
        )

        self.assertRaises(
            InvalidPrefixException,
            convert_units, 1.0, "m", "m", length_conversions, unit2_prefix="foo"
        )
