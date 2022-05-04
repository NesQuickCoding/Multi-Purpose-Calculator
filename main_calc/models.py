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
    'USub': op.neg,
}

def nodeTransversal(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operations[type(node.op).__name__](nodeTransversal(node.left), nodeTransversal(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operations[type(node.op).__name__](nodeTransversal(node.operand))
    else:
        raise TypeError(node)

def evaluateExpression(expression):
    try:
        result = str(nodeTransversal(ast.parse(expression, mode='eval').body))
    except (SyntaxError, ZeroDivisionError):
        result = "ERROR"

    return result
