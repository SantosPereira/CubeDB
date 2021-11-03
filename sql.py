class Sql:
    def __init__(self, banco) -> None:
        self.banco = banco

    def query(self, consulta):
        consulta = consulta.split()
        if consulta[-1].find(';') != -1:
            return self.banco[consulta[-1][:-1]]
