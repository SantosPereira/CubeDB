from sql import Sql
class CubicPool:
    def __init__(self) -> None:
        self.__row: dict = {}
        self.__pool: list = []
        self.cube: dict = {}
        self.sql = Sql(self.cube)


    def criarTabela(self, nomeTabela, tabela=[]) -> None:
        self.cube.update({nomeTabela:tabela})
            

    def inserirDados(self, tabela, dados) -> None:
        self.cube[tabela].append(dados)


CubicPool = CubicPool()
CubicPool.criarTabela('Tabela2')
CubicPool.inserirDados(
    'Tabela2',
    {
        'id': 2,
        'Nome': 'Pedro',
        'Idade': 19
    }
)

print(CubicPool.sql.query('SELECT * FROM Tabela2;'))