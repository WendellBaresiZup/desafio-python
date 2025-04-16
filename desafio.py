class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data
    
    def resumo(self):
        return f"{self.descricao} | {self.valor} | {self.categoria} | {self.data}"
    
transacao = Transacao("Salário", +2500 , "Alimentação", "15/04/2025")
print(transacao.resumo())

class Carteira:
    def __init__(self):
        self.transacoes = []
    
    def adicionar(self, transacao : Transacao):
        self.transacoes.append(transacao)

    def exibir_transacoes(self):
        print("Transações:" if self.transacoes else "Não houve Transação")
        for transacao in self.transacoes:
            print(transacao.resumo())
    
    def saldo(self):
        return sum(transacao.valor for transacao in self.transacoes)
    
    def filtrar_por_categoria(self, categoria):
        filtradas = [t for t in self.transacoes if t.categoria == categoria]
        if not filtradas:
            print(f"Nenhuma transação encontrada na categoria '{categoria}'.")
        else:
            print(f"Transações na categoria '{categoria}':")
            for transacao in filtradas:
                print(transacao.resumo())

    def gastos_totais(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor < 0)

    def renda_total(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor > 0)
    
    def resumo_geral(self):
        total_transacoes = len(self.transacoes)
        renda_total = self.renda_total()
        gastos_totais = self.gastos_totais()
        saldo_final = self.saldo()

        print("== Resumo geral == ", f"\nTotal de transações: {total_transacoes}" , f"\nRenda Total: {renda_total}", f"\nGastos Totais: {gastos_totais}", f"\nSaldo Final: {saldo_final}")

carteira = Carteira()
carteira.adicionar(Transacao("Salário", 2500, "Renda", "15/04/2025"))
carteira.adicionar(Transacao("Sorvete", -20, "Alimentação", "16/04/2025"))
carteira.adicionar(Transacao("Arroz", -30, "Alimentação", "16/04/2025"))
carteira.adicionar(Transacao("Dipirona", -50, "Farmacia", "16/04/2025"))
carteira.adicionar(Transacao("Creme", -80, "Farmacia", "16/04/2025"))

carteira.filtrar_por_categoria("Alimentação")
carteira.filtrar_por_categoria("Farmacia")

print(f"Saldo atual: {carteira.saldo()}")

carteira.resumo_geral