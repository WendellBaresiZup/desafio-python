class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data
    
    def resumo(self):
        return f"{self.descricao} | {self.valor} | {self.categoria} | {self.data}"
    
transacao1 = Transacao("Salário", +2500 , "Alimentação", "15/04/2025")
print(transacao1.resumo())