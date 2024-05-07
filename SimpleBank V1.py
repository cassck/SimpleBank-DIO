class Conta:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_saques:
            print("Operação falhou! Você atingiu o número máximo de 3 saques diários.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
            return
        while excedeu_limite:  # Loop para solicitar um novo valor de saque até que seja válido
            print("O valor excede o limite de R$500,00 por saque. Tente Novamente!")
            novo_valor = float(input("Digite um novo valor de saque: "))
            excedeu_limite = novo_valor > self.limite
            if not excedeu_limite:
                self.saque(novo_valor)

    def saldo_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

def main():
    conta = Conta()
    menu = """
    Escolha a opção desejada

    [1] Deposito
    [2] Saque
    [3] Saldo/Extrato
    [4] Sair

    =>"""

    while True:
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Insira o valor que você deseja depositar: "))
            conta.deposito(valor)

        elif opcao == "2":
            valor = float(input("Quanto você deseja sacar: "))
            conta.saque(valor)

        elif opcao == "3":
            conta.saldo_extrato()
            voltar_menu = input("Pressione Enter para voltar ao menu principal.")
            if voltar_menu == "":
                break

        elif opcao == "4":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
