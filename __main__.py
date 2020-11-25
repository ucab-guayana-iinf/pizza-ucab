# Dependencias de terceros
from pprint import pprint
from PyInquirer import prompt
from pyfiglet import Figlet

# Dependencias propias del proyecto
from db import DB
import config as CONFIG

menuLoop = True
menuOption = None

main_menu_options = {
    'order': order,
    'exit': exitProgram
}

def calculatePrice(order):
    """
        Función para calcular el precio total de una pizza dada una orden
    """

    sizePrice = CONFIG.SIZE_PRICES[order['size']]
    extrasPrice = 0
    for extra in order['extras']:
        extrasPrice += CONFIG.EXTRA_PRICES[extra]
    return sizePrice + extrasPrice


def printSelection(size, extras):
    """
    Función para imprimir el mensaje de la pizza seleccionada por el usuario

    Se muestran además los ingredientes extra elegidos para la pizza, en caso
    de no tener ingredientes extra muestra que es una pizza margarita
    """

    if (not extras):
        print(f'\n Usted seleccionó una pizza {size} Margarita')
    else:
        listaIngredientes = ', '.join(extras)
        print(f'\n Usted seleccionó una pizza {size} con {listaIngredientes}')


def order():
    pizzaLoop = True
    pizzaCount = 1
    totalPrice = 0
    answers = {}

    while(pizzaLoop):
        print(f' Pizza número: {pizzaCount}')

        answers = prompt(CONFIG.menu_questions)
        price = calculatePrice(answers)
        printSelection(answers['size'], answers['extras'])
        print(' Subtotal a pagar por la pizza:', price, '\n')
        totalPrice += price

        pizzaLoop = prompt(CONFIG.continue_question)['continue_question']
        if (pizzaLoop):
            pizzaCount += 1
        print()

    print(
        f' El pedido tiene un total de {pizzaCount} pizza(s) por un monto de {totalPrice}')
    print(' Gracias por su compra, regrese pronto')
    print()


def exitProgram():
    menuLoop = 'exit'
    print("Hasta luego")


if __name__ == "__main__":
    print(Figlet(font='slant').renderText("PIZZA UCAB"))

    while(menuOption != 'exit'):
        menuOption = prompt(CONFIG.main_menu_question)['menu_option']
        selectedMenuOption = main_menu_options.get(menuOption)
        if selectedMenuOption:
            selectedMenuOption()
