from tinydb import TinyDB, Query

# TODO: create utils folder & move this class over there
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
        """Crea y retorna una conexión con la BD local"""
        TinyDB('./local_db.json')

    def get_order(self):
        print("TODO")

    def get_orders(self):
        print("TODO")

    def delete_order(self):
        print("TODO")

    def update_order(self):
        print("TODO")

    # TODO:
    # CRUD clients?
    # CRUD ingredients?

