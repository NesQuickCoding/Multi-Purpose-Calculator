def length_conversion(input_value : float, input_index : int, output_index : int) -> float:
    """
    Calculates the conversion rate for length distances based on the input_index and 
    output_index from from the MetricConvWidget.

    The different units include Inches, Feet, Yards, Miles, Millimeters, Centimeters,
    Meters, Kilometers

    Parameters
    ----------
    input_value : float
        The original numerical length value before conversion
    input_index: int
        The index of the length unit of the input value.
    output_index: int
        The index of the length unit that the input value will be converted to
    Returns
    -------
    float
        The converted length measurement from input units to output's units
    """
    if input_index == output_index:
        return input_value
        
    conversion_map = [
        # Inches   Feet     Yards     Miles        Millime. Centimet.  Meters       Kilometers
        [1,        1/12,    1/36,     1/63360,     25.4,    2.54,      1/39.37008, 1/39370.08], # Inches
        [12,       1,       1/3,      1/5280,      304.8,   30.48,     1/3.28084,  1/3280.84],  # Feet
        [36,       3,       1,        1/1760,      914.4,   91.44,     1/1.09361,  1/1093.613], # Yards
        [63360,    5280,    1760,     1,           1609344, 160934.40, 1609.344,   1.609344],   # Miles
        [1/25.4,   1/304.8, 1/914.4,  1/1609344,   1,       1/10,      1/1000,     1/1000000],  # Millimeters
        [1/2.54,   1/30.48, 1/91.44,  1/160934.40, 10,      1,         1/100,      1/100000],   # Centimeters
        [39.37008, 3.28084, 1.09361,  1/1609.344,  1000,    100,       1,          1/1000],     # Meters
        [39370.08, 3280.84, 1093.613, 1/1.609344,  1000000, 100000,    1000,       1]           # Kilometers
    ]
    return input_value * conversion_map[input_index][output_index]

def weight_conversion(input_value, input_index, output_index):
    """
    Calculates the conversion rate for different weights based on the input_index and 
    output_index from from the MetricConvWidget.

    The different units are Ounces, Pounds, Stone, Tons (Short), Milligrams, Grams,
    Kilograms

    Parameters
    ----------
    input_value : float
        The original numerical weight value before conversion
    input_index: int
        The index of the weight unit of the input value.
    output_index: int
        The index of the weight unit that the input value will be converted to
    Returns
    -------
    float
        The converted weight measurement from input units to output's units
    """
    if input_index == output_index:
        return input_value
    # Rows are input, column are output
    conversion_map = [
        # Ounces         Pounds       Stone       Tons (Short)      Milligrams  Grams       Kilograms
        [1,	             1/16,	      1/224,	  1/32000,	        28349.5249, 28.3495249, 0.0283495249], # Ounces
        [16,	         1,	          1/14,	      1/2000,	        453592.4,   453.5923,   0.4535923],    # Pounds
        [224,	         16,	      1,	      7/1000,	        6350293,	6350.293,   6.350293],     # Stone
        [32000,	         2000,	      1/(7/1000), 1,	            907184740,  907184.7,   907.1847],     # Tons (Short)
        [1/28349.5249,	 1/453592.4,  1/6350293,  1/907184740,	    1,	        0.001,      0.000001],     # Milligram
        [1/28.3495249,	 1/453.5923,  1/6350.293, 1/907184.7,       1000,       1,          0.001],        # Gram
        [1/0.0283495249, 1/0.4535923, 1/6.350293, 1/907.1847000022, 1000000,	1000,       1]             # Kilogram
    ]
    return input_value * conversion_map[input_index][output_index]

def time_conversion(input_value, input_index, output_index):
    """
    Calculates the conversion rate for different time units based on the input_index and 
    output_index from from the MetricConvWidget.

    The different units are Milliseconds, Seconds, Minutes, Hours, Days, Months, and Years

    Parameters
    ----------
    input_value : float
        The original numerical time value before conversion
    input_index: int
        The index of the time unit of the input value.
    output_index: int
        The index of the time unit that the input value will be converted to
    Returns
    -------
    float
        The converted time measurement from input units to output's units
    """
    if input_index == output_index:
        return input_value

    conversion_map = [
        # MillisecondsSeconds   Minutes  Hours      Days        Months        Years
        [1,           1/1000,   1/60000, 1/3600000, 1/86400000, 1/2629800000, 1/31557600000], # Milliseconds
        [1000,        1,        1/60,    1/3600,    1/86400,    1/2629800,    1/31557600],    # Seconds
        [60000,       60,       1,       1/60,      1/1440,     1/43830,      1/525960],      # Minutes
        [3600000,     3600,     60,      1,         1/24,       1/730.5,      1/8766],        # Hours
        [86400000,    86400,    1440,    24,        1,          1/30.4375,    1/365.25],      # Days
        [2629800000,  2629800,  43830,   730.5,     30.4375,    1,            1/12],            # Months
        [31557600000, 31557600, 525960,  8766,      365.25,     12,           1]              # Years
    ]
    return input_value * conversion_map[input_index][output_index]

def digital_space_conversion(input_value, input_index, output_index):
    """
    Calculates the conversion rate for different digital space units based on the input_index
    and output_index from from the MetricConvWidget.

    The different units are Bits, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Petabytes,
    Exabytes, Zettabytes, Yottabytes

    Parameters
    ----------
    input_value : float
        The original numerical space value before conversion
    input_index: int
        The index of the space unit of the input value.
    output_index: int
        The index of the space unit that the input value will be converted to
    Returns
    -------
    float
        The converted digital spacce measurement from input units to output's units
    """
    if input_index == output_index:
        return input_value
    
    # Since all the conversions outside of bits are different exponents of 1000,
    # and the storage options are put in ascending order, the difference of the indexes
    # will return the proper exponent for the conversion
    if input_index > 0 and output_index > 0:
        return input_value * 1000**(input_index - output_index)
    
    # If converting from bits, calculate the difference then divide by 8
    if input_index == 0:
        return input_value * 1000**(input_index - output_index + 1) / 8

    # If converting to bits, calculate the difference then multiply by 8
    if output_index == 0:
        return input_value * 1000**(input_index - output_index - 1) * 8
