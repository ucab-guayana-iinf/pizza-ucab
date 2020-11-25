# Dependencias de terceros
import datetime
from pprint import pprint
from PyInquirer import prompt
from pyfiglet import Figlet
from ascii_graph import Pyasciigraph


# Dependencias propias del proyecto
from db import DB
import config as CONFIG

menuLoop = True
menuOption = None


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


def orderPizza():
    pizzaLoop = True
    pizzaCount = 1
    totalPrice = 0
    answers = {}
    order = {
        'created_at': None,
        'total': 0,
        'pizzas': []
    }

    while(pizzaLoop):
        print(f' Pizza número: {pizzaCount}')

        answers = prompt(CONFIG.menu_questions)
        price = calculatePrice(answers)
        printSelection(answers['size'], answers['extras'])
        print(' Subtotal a pagar por la pizza:', price, '\n')
        totalPrice += price

        order['pizzas'].append(answers)
        pizzaLoop = prompt(CONFIG.continue_question)['continue_question']
        if (pizzaLoop):
            pizzaCount += 1

        print()

    order['created_at'] = datetime.datetime.now().timestamp()
    order['total'] = totalPrice

    DB.Instance().create_order(order)

    print(
        f' El pedido tiene un total de {pizzaCount} pizza(s) por un monto de {totalPrice}')
    print(' Gracias por su compra, regrese pronto 👋')
    print()


def watchHistoric():
    orders_historic = DB.Instance().get_orders()
    print(orders_historic)  # TODO: pretty print
    return


def barGraph(data):
    print()
    for line in Pyasciigraph().graph('Pizzas ordenadas por tamaño', data):
        print(line)
    return


def showAnalytics():
    orders_historic = DB.Instance().get_orders()
    all_pizzas = []
    all_ingredients = []
    for order in orders_historic:
        for pizza in order['pizzas']:
            all_pizzas.append(pizza)
            for ingredient in pizza['extras']:
                all_ingredients.append(ingredient)

    pizzas_by_size_stats = list(map(
        lambda size: (
            size,
            len(list(filter(lambda pizza: pizza['size'] == size, all_pizzas)))
        ),
        CONFIG.SIZE_PRICES.keys()
    ))
    ingredients_stats = list(map(
        lambda ingredient: (
            ingredient,
            len(list(filter(lambda ing: ing == ingredient, all_ingredients)))
        ),
        CONFIG.EXTRA_PRICES.keys()
    ))

    barGraph(pizzas_by_size_stats)
    barGraph(ingredients_stats)
    return


def exitProgram():
    menuLoop = 'exit'
    print("Hasta luego 🙋")


main_menu_options = {
    'order': orderPizza,
    'historic': watchHistoric,
    'analytics': showAnalytics,
    'exit': exitProgram


}

if __name__ == "__main__":
    print(Figlet(font='slant').renderText("PIZZA UCAB"))

    while(menuOption != 'exit'):
        menuOption = prompt(CONFIG.main_menu_question)['menu_option']
        selectedMenuOption = main_menu_options.get(menuOption)
        if selectedMenuOption:
            selectedMenuOption()
