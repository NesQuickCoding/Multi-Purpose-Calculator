import re

def decValidator(stringNumber, limit):
    inputValidation = re.split(r"[^0-9]+", stringNumber)
    validDecNumber = ''.join(inputValidation)
    if validDecNumber == '':
        validDecNumber = "0"
    elif int(validDecNumber) > limit:
        validDecNumber = str(limit)
    return validDecNumber

def decFormatter(stringNumber):
    try:
        return f"{int(stringNumber):,}"
    except ValueError:
        return stringNumber

def hexValidator(stringNumber, limit):
    inputValidation = re.split(r"[^0-9a-fA-F]+", stringNumber)
    validHexNumber = ''.join(inputValidation)
    if validHexNumber == '':
        validHexNumber = "0"
    elif int(validHexNumber, 16) > limit:
        validHexNumber = hex(limit)
    return validHexNumber

def hexFormatter(stringNumber):
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

def binValidator(stringNumber, limit):
    inputValidation = re.split(r"[^0-1]+", stringNumber)
    validBinNumber = ''.join(inputValidation)
    if validBinNumber == '':
        validBinNumber = "0"
    elif int(validBinNumber, 2) > limit:
        validBinNumber = bin(limit)
    return validBinNumber
    
def binFormatter(stringNumber):
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
