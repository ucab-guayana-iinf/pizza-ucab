"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from pprint import pprint
from PyInquirer import prompt, Separator
from pyfiglet import Figlet
from db.core import DB

# class PhoneNumberValidator(Validator):
#     def validate(self, document):
#         ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
#         if not ok:
#             raise ValidationError(
#                 message='Please enter a valid phone number',
#                 cursor_position=len(document.text))  # Move cursor to end


# class NumberValidator(Validator):
#     def validate(self, document):
#         try:
#             int(document.text)
#         except ValueError:
#             raise ValidationError(
#                 message='Please enter a number',
#                 cursor_position=len(document.text))  # Move cursor to end

# DB.Instance().query_1()

print(Figlet(font='slant').renderText("PIZZA UCAB"))

# TODO:
# - ordenar las preguntas de la forma adecuada
# - computar lo que haya que compuar
# - agregar las validaciones pertinentes
# - integrar funcionalidades extra

questions = [
    {
        'type': 'list',
        'name': 'size',
        'message': 'Opciones:',
        'choices': ['Grande', 'Mediana', 'Personal'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Seleccione los ingredientes adicionales que desea:',
        'name': 'extras',
        'choices': [
            Separator('---Opciones---'),
            {
                'name': 'Jamón'
            },
            {
                'name': 'Champiñones'
            },
            {
                'name': 'Pimentón'
            },
            {
                'name': 'Doble Queso'
            },
            {
                'name': 'Aceitunas'
            },
            {
                'name': 'Pepperoni'
            },
            {
                'name': 'Salchichón'
            }
        ],
        # 'validate': lambda answer: 'You must choose at least one topping.' \
        #     if len(answer) == 0 else True
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
    #     'type': 'input',
    #     'name': 'phone',
    #     'message': 'What\'s your phone number?'
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
    #     'type': 'input',
    #     'name': 'comments',
    #     'message': 'Any comments on your purchase experience?',
    #     'default': 'Nope, all good!'
    # },
    # {
    #     'type': 'list',
    #     'name': 'prize',
    #     'message': 'For leaving a comment, you get a freebie',
    #     'choices': ['cake', 'fries'],
    #     'when': lambda answers: answers['comments'] != 'Nope, all good!'
    # }
]

loop = True
answers = {}
while(loop):
    answers = prompt(questions)
    loop = answers['multiorder']
print('Resumen de orden:')
pprint(answers)
