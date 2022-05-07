def length_conversion(input_value, input_index, output_index):
    if input_index == output_index:
        return input_value
    unit_key = [
        "Inches", "Feet", "Yards", "Miles",
        "Millimeters", "Centimeters", "Meters", "Kilometers"]

    input_unit = unit_key[input_index]
    output_unit = unit_key[output_index]

    # Metric
    if input_unit == "Inches":
        if output_unit == "Feet":
            return input_value / 12
        elif output_unit =="Yards":
            return input_value / 36
        elif output_unit == "Miles":
            return input_value / 63360
        elif output_unit == "Millimeters":
            return input_value * 25.4
        elif output_unit == "Centimeters":
            return input_value * 2.54
        elif output_unit == "Meters":
            return input_value / 39.370
        elif output_unit == "Kilometers":
            return input_value / 39370.0787

    if input_unit == "Feet":
        if output_unit == "Inches":
            return input_value * 12
        elif output_unit =="Yards":
            return input_value / 3
        elif output_unit == "Miles":
            return input_value / 5280
        elif output_unit == "Millimeters":
            return input_value * 304.8
        elif output_unit == "Centimeters":
            return input_value * 30.48
        elif output_unit == "Meters":
            return input_value * 0.3048
        elif output_unit == "Kilometers":
            return input_value / 3280.84

    if input_unit == "Yards":
        if output_unit == "Feet":
            return input_value * 3
        elif output_unit =="Inches":
            return input_value * 36
        elif output_unit == "Miles":
            return input_value / 1760
        elif output_unit == "Millimeters":
            return input_value * 914.4
        elif output_unit == "Centimeters":
            return input_value * 91.44
        elif output_unit == "Meters":
            return input_value * 0.9144
        elif output_unit == "Kilometers":
            return input_value * 0.0009144

    if input_unit == "Miles":
        if output_unit == "Feet":
            return input_value * 5280
        elif output_unit =="Yards":
            return input_value * 1760
        elif output_unit == "Inches":
            return input_value * 63360
        elif output_unit == "Millimeters":
            return input_value * 1609344
        elif output_unit == "Centimeters":
            return input_value * 160934.4
        elif output_unit == "Meters":
            return input_value * 1609.344
        elif output_unit == "Kilometers":
            return input_value * 1.609344

    # Imperial   
    if input_unit == "Millimeters":
        if output_unit == "Feet":
            return input_value / 304.8
        elif output_unit =="Yards":
            return input_value / 914.4
        elif output_unit == "Miles":
            return input_value / 1609344
        elif output_unit == "Inches":
            return input_value / 25.4
        elif output_unit == "Centimeters":
            return input_value / 10
        elif output_unit == "Meters":
            return input_value / 1000
        elif output_unit == "Kilometers":
            return input_value / 1000000

    if input_unit == "Centimeters":
        if output_unit == "Inches":
            return input_value / 2.54
        elif output_unit =="Yards":
            return input_value / 91.44
        elif output_unit == "Miles":
            return input_value / 160934.4
        elif output_unit == "Millimeters":
            return input_value * 10
        elif output_unit == "Feet":
            return input_value / 30.48
        elif output_unit == "Meters":
            return input_value / 100
        elif output_unit == "Kilometers":
            return input_value / 100000

    if input_unit == "Meters":
        if output_unit == "Feet":
            return input_value / 0.3048
        elif output_unit =="Inches":
            return input_value * 39.370
        elif output_unit == "Miles":
            return input_value / 1609.344
        elif output_unit == "Millimeters":
            return input_value * 1000
        elif output_unit == "Centimeters":
            return input_value * 100
        elif output_unit == "Yards":
            return input_value / 0.9144
        elif output_unit == "Kilometers":
            return input_value / 1000

    if input_unit == "Kilometers":
        if output_unit == "Feet":
            return input_value * 3280.84
        elif output_unit == "Yards":
            return input_value * 1093.6132983
        elif output_unit == "Inches":
            return input_value * 39370.0787
        elif output_unit == "Millimeters":
            return input_value * 1000000
        elif output_unit == "Centimeters":
            return input_value * 100000
        elif output_unit == "Meters":
            return input_value * 1000
        elif output_unit == "Miles":
            return input_value / 1.609344

def weight_conversion(input_value, input_index, output_index):
    if input_index == output_index:
        return input_value
    # Rows are input, column are output
    conversion_map = [
        1,	            1/16,	     1/224,	     1/32000,	       28349.5249, 28.3495249, 0.0283495249,
        16,	            1,	         1/14,	     1/2000,	       453592.4,   453.5923,   0.4535923,
        224,	        16,	         1,	         7/1000,	       6350293,	   6350.293,   6.350293,
        32000,	        2000,	     1/(7/1000), 1,	               907184740,  907184.7,   907.1847,
        1/28349.5249,	1/453592.4,	 1/6350293,	 1/907184740,	   1,	       0.001,      0.000001,
        1/28.3495249,	1/453.5923,	 1/6350.293, 1/907184.7,       1000,       1,          0.001,
        1/0.0283495249,	1/0.4535923, 1/6.350293, 1/907.1847000022, 1000000,	   1000,       1
    ]
    return input_value * conversion_map[input_index][output_index]
