
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
    """Retorna el factorial del numero dado. Si es menor a 0 retorna 1.

    Args:
        numeroFactorial (int): es el numero que deceamos retorna el factorial

    Returns:
        int: un numeroFactorial, el resultado de hacer el factorial de #numeroFactorial

    Requirement: Ninguno.
    """
    numeroActual = numeroFactorial
    factorial = 1
    while ( numeroActual >= 0 ):
        factorial = factorial * numero_SiEsMayorA0EnCasoContrario1(numeroActual)
        numeroActual -= 1

    return factorial


def numero_SiEsMayorA0EnCasoContrario1(numero:int):
    """Describe el numero dado como parametro unicamente si ese número es mayor a 0. En caso contrario 
        devuelve un 1.

    Args:
        numero (int): es el numero que deceamos que devuelva si es mayor a 1
    
    returns:
        int: el numero pasado como parametro si es mayor a cero o 1 si es igual a cero.
        
    Requeriments:
        Ninguno.
    """
    if(numero > 0):
        return numero
    else:
        return 1




print(factorialDe_(5))
