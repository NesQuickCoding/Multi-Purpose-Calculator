import re

def signedIntToBase(value, bits, base):
    return base((value + (1 << bits)) % (1 << bits))

def signedBaseToInt(value ,bits):
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

def decValidator(stringNumber, limit, isSigned):
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
    try:
        return f"{int(stringNumber):,}"
    except ValueError:
        return stringNumber

def hexValidator(stringNumber, limit, isSigned):
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
    stringNumber = signedIntToBase(int(stringNumber, 16), bit, hex)[2:]
    validHexNumber = ""
    try:
        count = 0
        if len(stringNumber) > 4:
            for i in range(len(stringNumber) - 1, -1, -1):
                validHexNumber = stringNumber[i] + validHexNumber
                count += 1
                if count == 4 and i != 0:
                    validHexNumber = " " + validHexNumber
                    count = 0
        else:
            validHexNumber = stringNumber
    except ValueError:
        pass
    return validHexNumber.upper()

def binValidator(stringNumber, limit, isSigned):
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
    stringNumber = signedIntToBase(int(stringNumber, 2), bit, bin)[2:]
    validBinNumber = ""
    try:
        count = 0
        if len(stringNumber) > 4:
            for i in range(len(stringNumber) - 1, -1, -1):
                validBinNumber = stringNumber[i] + validBinNumber
                count += 1
                if count == 4 and i != 0:
                    validBinNumber = " " + validBinNumber
                    count = 0
        else:
            validBinNumber = stringNumber
    except ValueError:
        pass
    return validBinNumber
