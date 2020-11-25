
main_menu_question = {} # TODO

"""
    Lista de preguntas que se presentarán al usuario.
    En estas se maneja la validación para que solo se puedan escoger una de las opciones propuestas.
"""
menu_questions = [
    {
        'type': 'list',
        'qmark': '',
        'name': 'size',
        'message': 'Seleccione el tamaño:',
        'choices': [
            {
                'name': 'Grande (580)',
                'value': 'Grande'
            },
            {
                'name': 'Mediana (430)',
                'value': 'Mediana'
            },
            {
                'name': 'Personal (280)',
                'value': 'Personal'
            }
        ]
    },
    {
        'type': 'checkbox',
        'qmark': '',
        'message': 'Seleccione los ingredientes adicionales que desea:',
        'name': 'extras',
        'choices': [
            {
                'name': 'Jamón (40)',
                'value': 'Jamón'
            },
            {
                'name': 'Champiñones (35)',
                'value': 'Champiñones'
            },
            {
                'name': 'Pimentón (30)',
                'value': 'Pimentón'
            },
            {
                'name': 'Doble Queso (40)',
                'value': 'Doble Queso'
            },
            {
                'name': 'Aceitunas (57.5)',
                'value': 'Aceitunas'
            },
            {
                'name': 'Pepperoni (38.5)',
                'value': 'Pepperoni'
            },
            {
                'name': 'Salchichón (62.5)',
                'value': 'Salchichón'
            }
        ]
    }
]

"""
    Pregunta para confirmar si el usuario desea ordenar alguna otra pizza antes de
    finalizar la ejecución del programa
"""
continue_question = [
    {
        'type': 'confirm',
        'qmark': '',
        'message': 'Desea ordenar otra pizza?',
        'name': 'continue_question',
        'default': False,
    },
]
