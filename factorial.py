
def factorialDe_(numero):
    """Retorna el factorial del numero dado. En caso de ser menor que 0 da error.

    Args:
        numero (int): es el numero que deceamos retornal el factorial

    Returns:
        int: un número, el resultado de hacer el factorial de #numero

    Requirement:
        El parametro otorgado debe ser mayor o igual a 0.
    """
    if (numero>=0):
        return factorialDe_Osino1(numero)
    else:
        raise Exception("No se puede es Menor a 0 ")


def factorialDe_Osino1(numeroFactorial):
    """retorna el factorial del numero dado. Si es menor a 0 retorna 1.

    Args:
        numeroFactorial (int): es el numero que deceamos retornal el factorial

    Returns:
        int: un numeroFactorial, el resultado de hacer el factorial de #numeroFactorial

    Requirement: Ninguno.
    """
    numeroActual = numeroFactorial
    factorial = 1
    while ( numeroActual > 0 ):
        factorial = factorial * numeroActual
        numeroActual -= 1

    return factorial


print(factorialDe_(0))
