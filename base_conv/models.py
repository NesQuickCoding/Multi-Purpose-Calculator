import re

def signedIntToBase(value, bits, base):
  return base((value + (1 << bits)) % (1 << bits))

def decValidator(stringNumber, limit, isSigned):
    storeMinus = True if stringNumber[0] == "-" and stringNumber[0:1] != "--" else False
    # expression = r"[^-0-9]+" if isSigned else r"[^0-9]+"
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
    expression = r"[^-0-9a-fA-F]+" if isSigned else r"[^0-9a-fA-F]+"
    inputValidation = re.split(expression, stringNumber)
    validHexNumber = ''.join(inputValidation)
    if validHexNumber == '' or validHexNumber == "-":
        validHexNumber = "0"
    elif int(validHexNumber, 16) > limit:
        validHexNumber = hex(limit)
    elif isSigned and int(validHexNumber, 16) < -(limit + 1):
        print(int(validHexNumber, 16), limit)
        validHexNumber = hex(-(limit + 1))
    print("from validator: ", validHexNumber)
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
