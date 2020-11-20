from PyInquirer import Separator
"""
    Lista de preguntas que se presentarán al usuario.
    En estas se maneja la validación para que solo se puedan escoger una de las opciones propuestas.
"""
questions = [
    {
        'type': 'list',
        'name': 'size',
        'message': 'Seleccione el tamaño:',
        'choices': ['Grande (580)', 'Mediana (430)', 'Personal (280)'],
        'filter': lambda val: val.lower().split(' ')[0]
    },
    {
        'type': 'checkbox',
        'qmark': '?',
        'message': 'Seleccione los ingredientes adicionales que desea:',
        'name': 'extras',
        'choices': [
            # Separator('---Opciones---'),
            {
                'name': 'Jamón (100)'
            },
            {
                'name': 'Champiñones (35)'
            },
            {
                'name': 'Pimentón (30)'
            },
            {
                'name': 'Doble Queso (40)'
            },
            {
                'name': 'Aceitunas (57.5)'
            },
            {
                'name': 'Pepperoni (38.5)'
            },
            {
                'name': 'Salchichón (62.5)'
            }
        ],
        'filter': lambda values: [val.lower().split(' ')[0] for val in values]
    },
    {
        'type': 'confirm',
        'message': 'Desea ordenar otra pizza?',
        'name': 'multiorder',
        'default': False,
    },
    # {
    #     'type': 'confirm',
    #     'name': 'toBeDelivered',
    #     'message': 'Is this for delivery?',
    #     'default': False
    # },
    # {
    #     'type': 'list',
    #     'name': 'size',
    #     'message': 'What size do you need?',
    #     'choices': ['Large', 'Medium', 'Small'],
    #     'filter': lambda val: val.lower()
    # },
    # {
    #     'type': 'input',
    #     'name': 'quantity',
    #     'message': 'How many do you need?',
    #     # 'validate': NumberValidator,
    #     'filter': lambda val: int(val)
    # },
    # {
    #     'type': 'expand',
    #     'name': 'toppings',
    #     'message': 'What about the toppings?',
    #     'choices': [
    #         {
    #             'key': 'p',
    #             'name': 'Pepperoni and cheese',
    #             'value': 'PepperoniCheese'
    #         },
    #         {
    #             'key': 'a',
    #             'name': 'All dressed',
    #             'value': 'alldressed'
    #         },
    #         {
    #             'key': 'w',
    #             'name': 'Hawaiian',
    #             'value': 'hawaiian'
    #         }
    #     ]
    # },
    # {
    #     'type': 'rawlist',
    #     'name': 'beverage',
    #     'message': 'You also get a free 2L beverage',
    #     'choices': ['Pepsi', '7up', 'Coke']
    # },
    # {
    #     'type': 'list',
    #     'name': 'prize',
    #     'message': 'For leaving a comment, you get a freebie',
    #     'choices': ['cake', 'fries'],
    #     'when': lambda answers: answers['comments'] != 'Nope, all good!'
    # }
]
