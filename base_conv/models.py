import re

def signedIntToBase(value, bits, base):
    """
    Takes an int value and performs a bit shift by bits value
    Then convert it to the base unit

    Parameters
    ----------
    value : int
        integer value to convert to specified base
    bits : int
        number of bit shift to perform
        will be either 8, 16, 32, or 64
    base : hex()/bin()
        Used to convert to either of the two bases
    
    Returns
    -------
    str
        Returns value converted to hex or binary in str form
    """
    return base((value + (1 << bits)) % (1 << bits))

def signedBaseToInt(value, bits):
    """
    Takes an int value in hex or bin representation and performs a bit shift by bits value
    to achive the int value with base 10

    Parameters
    ----------
    value : int
        integer value with hex or bin base to convert to decimal
    bits : int
        number of bit shift to perform
        will be either 8, 16, 32, or 64

    Returns
    -------
    int
        Returns value converted to decimal
    """
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

def rightToLeftInsertion(string, position, insertChar):
    """
    Formats a string to insert a character at every <position> place

    Parameters
    ----------
    string : str
        Original string to manipulate
    position : int
        Every nth space, insert a character into that space
    insertChar : str
        The character or str to insert at that place
    
    Returns
    -------
    str
        Newly moddified string
    """
    if len(string) > position:
        formattedString = ""
        count = 0
        for i in range(len(string) - 1, -1, -1):
            formattedString = string[i] + formattedString
            count += 1
            if count == position and i != 0:
                formattedString = insertChar + formattedString
                count = 0
        return formattedString
    else:
        return string

def decValidator(stringNumber, limit, isSigned):
    """
    Validates a decimal number in string form:
    - If a negative sign in the beginning only if isSigned is enabled
    - Uses RegExp to confirm input is only digits
    - Splits at the commas and merges into a legal int number
    - Checks if it's in the limit bounds and manipulates based on limit:
        if signed: floor is negative of limit minus 1
        if unsigned: floor is zero

    Parameters
    ----------
    stringNumber : str
        string representation of an decimal number with thousandths place commas
    limit : int
        roof limit of the number based on signage and bit-width
    isSigned : int
        0 for false, 1 for true
    
    Returns
    -------
    int
        A valid int number that can be used for formatting and conversion
        to other bases
    """
    storeMinus = False
    try:
        if stringNumber[0] == "-" and stringNumber[0:2] != "--" and isSigned:
            storeMinus = True
    except IndexError:
        pass
    inputValidation = re.split(r"[^0-9]+", stringNumber)
    validDecNumber = ''.join(inputValidation)
    if storeMinus:
        validDecNumber = "-" + validDecNumber
    if validDecNumber == '' or validDecNumber == '-':
        validDecNumber = "0"
    elif int(validDecNumber) > limit:
        validDecNumber = str(limit)
    elif isSigned and int(validDecNumber) < -(limit + 1):
        validDecNumber = str(-(limit + 1))
    return validDecNumber

def decFormatter(stringNumber):
    """
    Formats a decimal number in string form have commas

    Parameters
    ----------
    stringNumber
        decimal number in string form
    
    Returns
    -------
    str
        Integer with commas (ie, 104,532)
    """
    try:
        return f"{int(stringNumber):,}"
    except ValueError:
        return stringNumber

def hexValidator(stringNumber, limit, isSigned):
    """
    Validates a hexadecimal number in string form:
    - If a negative sign in the beginning only if isSigned is enabled
    - Uses RegExp to confirm input is only digits
    - Splits at the spaces and merges into a legal hex number
    - Checks if it's in the limit bounds and manipulates to the limit

    Parameters
    ----------
    stringNumber : str
        string representation of an hexadecimal number with a space every four digits
    limit : int
        roof limit of the number based on signage and bit-width
    isSigned : int
        0 for false, 1 for true
    
    Returns
    -------
    str
        A valid hex number that can be used for formatting and conversion
        to other bases
    """
    storeMinus = False
    try:
        if stringNumber[0] == "-" and stringNumber[0:2] != "--" and isSigned:
            storeMinus = True
    except IndexError:
        pass
    inputValidation = re.split(r"[^0-9a-fA-F]+", stringNumber)
    validHexNumber = ''.join(inputValidation)
    if storeMinus:
        validHexNumber = "-" + validHexNumber
    if validHexNumber == '' or validHexNumber == "-":
        return "0"
    elif int(validHexNumber, 16) > limit:
        validHexNumber = hex(limit)
    return validHexNumber
    
def hexFormatter(stringNumber, bit):
    """
    Formats a hexadecimal string to have a space every 4 digits

    Parameters
    ----------
    stringNumber : str
        string number to convert to int, base 16, then to convert to hex
    bit : int
        number of bit-width for bit shifting
    
    Returns
    -------
    str
        Hexadecimal with spaces (ie 10 1FA9 032A)
    """
    stringNumber = signedIntToBase(int(stringNumber, 16), bit, hex)[2:]
    return rightToLeftInsertion(stringNumber, 4, " ").upper()

def binValidator(stringNumber, limit, isSigned):
    """
    Validates a binary number in string form:
    - If a negative sign in the beginning only if isSigned is enabled
    - Uses RegExp to confirm input is only digits
    - Splits at the spaces and merges into a legal binary number
    - Checks if it's in the limit bounds and manipulates to the limit

    Parameters
    ----------
    stringNumber : str
        string representation of an binary number with a space every four digits
    limit : int
        roof limit of the number based on signage and bit-width
    isSigned : int
        0 for false, 1 for true
    
    Returns
    -------
    str
        A valid hex number that can be used for formatting and conversion
        to other bases
    """
    storeMinus = False
    try:
        if stringNumber[0] == "-" and stringNumber[0:2] != "--" and isSigned:
            storeMinus = True
    except IndexError:
        pass
    inputValidation = re.split(r"[^0-1]+", stringNumber)
    validBinNumber = ''.join(inputValidation)
    if storeMinus:
        validBinNumber = "-" + validBinNumber
    if validBinNumber == '' or validBinNumber == "-":
        return "0"
    elif int(validBinNumber, 2) > limit:
        validBinNumber = bin(limit)
    return validBinNumber
    
def binFormatter(stringNumber, bit):
    """
    Formats a binarystring to have a space every 4 digits

    Parameters
    ----------
    stringNumber : str
        string number to convert to int, base 2, then to convert to bin
    bit : int
        number of bit-width for bit shifting
    
    Returns
    -------
    str
        Binary number with spaces (ie 10 1010 1100)
    """
    stringNumber = signedIntToBase(int(stringNumber, 2), bit, bin)[2:]
    return rightToLeftInsertion(stringNumber, 4, " ")
