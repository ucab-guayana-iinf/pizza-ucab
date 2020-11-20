"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from pprint import pprint
from PyInquirer import prompt
from pyfiglet import Figlet
from db.core import DB
from questions import questions

# DB.Instance().query_1()

# TODO:
# - ordenar las preguntas de la forma adecuada
# - computar lo que haya que computar
# - agregar las validaciones pertinentes
# - integrar funcionalidades extra

"""
    Constantes para los precios de tamaños e ingredientes extras
"""
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
pizzas = []


def calculatePrice(order):
    sizePrice = SIZE_PRICES[order['size']]
    extrasPrice = 0
    for extra in order['extras']:
        extrasPrice += EXTRA_PRICES[extra]
    return sizePrice + extrasPrice


if __name__ == "__main__":
    # print(Figlet(font='slant').renderText("PIZZA UCAB"))
    while(loop):
        print(f'Pizza número: {pizzaCount}')
        answers = prompt(questions)
        price = calculatePrice(answers)
        print('Subtotal: ', price)
        loop = answers['multiorder']
        print('Resumen de orden:')
        pprint(answers)
