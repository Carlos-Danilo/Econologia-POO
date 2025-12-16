from database import Database
from models.morador import Morador
from models.coleta import Coleta
from dao.morador_dao import MoradorDAO
from dao.coleta_dao import ColetaDAO
from datetime import datetime

db = Database()
db.criar_tabelas()

# TESTE MORADOR
morador_dao = MoradorDAO()
m = Morador("Carlos", "carlos@email.com", "99999999", "1234", 0)
morador_dao.inserir(m)

print("Moradores:")
for morador in morador_dao.listar():
    print(morador)

# TESTE COLETA
coleta_dao = ColetaDAO()
c = Coleta(0, datetime.now().isoformat(), "Coleta de papel", 10, True)
coleta_dao.inserir(c)

print("\nColetas:")
for coleta in coleta_dao.listar():
    print(coleta)
