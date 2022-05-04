import ast
import operator as op

operations = {
    'Add': op.add,
    'Sub': op.sub, 
    'Mult': op.mul,
    'Div': op.truediv,
    'FloorDiv': op.floordiv,
    'Pow': op.pow,
    'Mod': op.mod,
    'UAdd': op.abs,
    'USub': op.neg,
}

def astTransversal(astObj):
    if isinstance(astObj, ast.Constant):
        return astObj.n
    elif isinstance(astObj, ast.BinOp):
        return operations[type(astObj.op).__name__](astTransversal(astObj.left), astTransversal(astObj.right))
    elif isinstance(astObj, ast.UnaryOp):
        return operations[type(astObj.op).__name__](astTransversal(astObj.operand))
    else:
        raise TypeError(astObj)

def evaluateExpression(expression):
    try:
        result = str(astTransversal(ast.parse(expression, mode='eval').body))
    except (SyntaxError, ZeroDivisionError, TypeError):
        result = "ERROR"

    return result
