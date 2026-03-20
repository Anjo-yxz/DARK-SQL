import time
from model.ModelDatabase import Model

class main:
    def __init__(self):
        self.user = []

    def database(self, database: str):
        try:
            with open(database, "r", encoding="utf-8") as user:
                self.separa = user.read().splitlines()
                for self.sep in self.separa:
                    self.dados = self.sep.split(":")
                    self.baseUser = Model(email=self.dados[0], senha=self.dados[1])
                    self.user.append(self.baseUser)
        except FileNotFoundError:
            print(f"arquivo nao encontrado -> {database}")
            self.user = []
        except Exception as e:
            print(f"erro ao ler o arquivo: {e}")
            self.user = []