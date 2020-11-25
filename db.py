from tinydb import TinyDB, Query


class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class DB:
    def __init__(self):
        """Crea y retorna una conexión con a BD local"""

    def connection(self):
        return TinyDB('./local_db.json')

    def get_orders(self):
        return self.connection().all()

    def create_order(self, order):
        return self.connection().insert(order)
