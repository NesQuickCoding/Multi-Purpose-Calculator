def length_conversion(input_value, input_unit, output_unit):
    if input_unit == output_unit:
        return input_value
    
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
            return input_value / 39370
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
