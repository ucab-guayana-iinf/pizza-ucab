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
    'grande': 580,
    'mediana': 430,
    'personal': 280
}
EXTRA_PRICES = {
    'jamón': 40,
    'champiñones': 35,
    'pimentón': 30,
    'doble queso': 40,
    'aceitunas': 57.5,
    'pepperoni': 38.5,
    'salchichón': 62.5
}

loop = True
answers = {}
pizzaCount = 1

if __name__ == "__main__":
    # print(Figlet(font='slant').renderText("PIZZA UCAB"))
    while(loop):
        print(f'Pizza número: {pizzaCount}')
        answers = prompt(questions)
        loop = answers['multiorder']
        print('Resumen de orden:')
        pprint(answers)
