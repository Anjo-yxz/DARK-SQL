import time
from logo.logo import Logo
from full.databaseUser import main as DBMain

class execute(DBMain):
    def execute(self, database: str):
        print(Logo.logo())
        time.sleep(1)
        self.database(database)
        for baseUser in self.user:
            print(f"Email: {baseUser.email}  |  Senha: {baseUser.senha}")
        print(f"Total de contas: {len(self.user)}")