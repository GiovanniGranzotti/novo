"""Soma dois números para dar um número"""

lista_de_num = [1, 2, 3, 4, 5, 6]
alvo = [5]


def two_sum_func(lista_de_num, alvo):
    """Soma dois numeros de uma lista que dê o valor do alvo

    Ex:
    >>> two_sum_func()

    :param lista_de_num: list
    :param alvo: list
    :return: int
    """
    result = 0
    conta = 0
    for numero in lista_de_num:
        result += numero
        conta += 1
        if result == alvo and conta == 2:
            print(numero)
            return result
        elif conta == 2:
            print(numero)
            result = 0
            conta = 0
        else:
            print(numero)


print(two_sum_func)