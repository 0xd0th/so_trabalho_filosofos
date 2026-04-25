
class Filosofo:
    """ CLASSE PARA SIMULAR UM FILOSOFO QUE ESTA COM MUITA FOME :) :)"""

    def __init__(self, id: int ):
        self.id: int = id
        self.estado: str = "INICIADO" 

    def pensar(self):
        print(f"FILOSOFO {self.id} ESTA PENSANDO!")

    def comer(self):
        print(f"FILOSOFO {self.id} ESTA COMENDO")

    def pegar(self):
        pass

    def devolver(self):
        pass
