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
    """
    Abstract syntax tree transversal for basic math/eval expressions.
    Recursive function that calculates an expression based on end nodes,
    then returns its value for higher nodes to calcuate their expressions.

    Parameters
    ----------
    astObj : Abstract syntax tree object
        Expected ast.Constant, ast.BinOp, and ast.UnaryOp types

    Raises
    ------
    TypeError
        If astObj is not a constant, binOp or unaryOp, thus not
        a basic eval math expression

    Returns
    -------
    int, float
        Final evaluated expression
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
    """
    Driver for abstract syntax tree transversal for basic math/eval expressions.
    ast.parses expression with eval mode, sending it's body to astTransversal
    for safe math evaluation.

    If SyntaxErorr, ZeroDivisionError, or TypeError, sends results as "ERROR"

    Parameters
    ----------
    express : str
        Full math expression in str form

    Returns
    -------
    str
        Final evaluated expression
    """
    try:
        result = str(astTransversal(ast.parse(expression, mode='eval').body))
    except (SyntaxError, ZeroDivisionError, TypeError):
        result = "ERROR"

    return result
