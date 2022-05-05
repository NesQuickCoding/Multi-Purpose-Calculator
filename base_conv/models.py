import re
import string

def decValidator(stringNumber):
    inputValidation = re.split(r"[^0-9]+", stringNumber)
    validDecNumber = ''.join(inputValidation)
    return validDecNumber

def decFormatter(stringNumber):
    try:
        return f"{int(stringNumber):,}"
    except ValueError:
        return stringNumber

def hexValidator(stringNumber):
    inputValidation = re.split(r"[^0-9a-fA-F]+", stringNumber)
    validHexNumber = ''.join(inputValidation)
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

def binValidator(stringNumber):
    inputValidation = re.split(r"[^0-1]+", stringNumber)
    validBinNumber = ''.join(inputValidation)
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
