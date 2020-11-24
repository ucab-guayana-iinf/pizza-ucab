"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from pprint import pprint
from PyInquirer import prompt
from pyfiglet import Figlet
from db.core import DB
from questions import questions, anotherPizza

# DB.Instance().query_1()

# TODO:
# - ordenar las preguntas de la forma adecuada
# - computar lo que haya que computar
# - agregar las validaciones pertinentes
# - integrar funcionalidades extra

"""Constantes para los precios de tamaños e ingredientes extras"""
SIZE_PRICES = {
    'Grande': 580,
    'Mediana': 430,
    'Personal': 280
}
EXTRA_PRICES = {
    'Jamón': 40,
    'Champiñones': 35,
    'Pimentón': 30,
    'Doble Queso': 40,
    'Aceitunas': 57.5,
    'Pepperoni': 38.5,
    'Salchichón': 62.5
}

loop = True
answers = {}
pizzaCount = 1
totalPrice = 0


def calculatePrice(order):
    """Función para calcular el precio total de una pizza"""

    sizePrice = SIZE_PRICES[order['size']]
    extrasPrice = 0
    for extra in order['extras']:
        extrasPrice += EXTRA_PRICES[extra]
    return sizePrice + extrasPrice


def printSelection(size, extras):
    """Función para imprimir el mensaje de la pizza seleccionada por el usuario

    Se muestran además los ingredientes extra elegidos para la pizza, en caso
    de no tener ingredientes extra muestra que es una pizza margarita
    """

    if (not extras):
        print(f'\n Usted seleccionó una pizza {size} Margarita')
    else:
        listaIngredientes = ', '.join(extras)
        print(f'\n Usted seleccionó una pizza {size} con {listaIngredientes}')


if __name__ == "__main__":
    """Ciclo principal del programa"""

    print(Figlet(font='slant').renderText("PIZZA UCAB"))
    while(loop):
        print(f' Pizza número: {pizzaCount}')

        answers = prompt(questions)
        price = calculatePrice(answers)
        printSelection(answers['size'], answers['extras'])
        print(' Subtotal a pagar por la pizza:', price, '\n')
        totalPrice += price

        loop = prompt(anotherPizza)['anotherPizza']
        if (loop):
            pizzaCount += 1
        print()

    print(
        f' El pedido tiene un total de {pizzaCount} pizza(s) por un monto de {totalPrice}')
    print(' Gracias por su compra, regrese pronto')
