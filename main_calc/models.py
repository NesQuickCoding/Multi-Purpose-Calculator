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
    """Abstract synthax grammar checker, checking for constants, unary, or binary operations.

    Args:
        astObj (_type_): _description_

    Raises:
        TypeError: raise error if not a constant, binary operator, or unary op.

    Returns:
        result: the code with the correct grammar rules
    """
    if isinstance(astObj, ast.Constant):
        return astObj.n
    elif isinstance(astObj, ast.BinOp):
        return operations[type(astObj.op).__name__](astTransversal(astObj.left), astTransversal(astObj.right))
    elif isinstance(astObj, ast.UnaryOp):
        return operations[type(astObj.op).__name__](astTransversal(astObj.operand))
    else:
        raise TypeError(astObj)

def evaluateExpression(expression):
    """Evaluate the expression typed into the calculator.

    Args:
        expression (str): Expression given to evaluate

    Returns:
        result (str): answer to the given expression
    """
    try:
        result = str(astTransversal(ast.parse(expression, mode='eval').body))
    except (SyntaxError, ZeroDivisionError, TypeError):
        result = "ERROR"

    return result
