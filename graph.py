from ascii_graph import Pyasciigraph


def barGraph(title, data):
    """
      Dado un titulo y una tupla de datos formados por (titulo, numero)
      imprime un gráfico de barra en la terminal
    """

    print()
    for line in Pyasciigraph().graph(title, data):
        print(line)
    return
