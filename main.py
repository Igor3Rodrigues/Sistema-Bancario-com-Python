class contabancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.depositos = []
        self.saques = []
        
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            return f"\nDepósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}\n"
        else:
            return "\nValor do depósito deve ser positivo.\n"


    def saque(self, valor):
        if valor > self.saldo:
            return "\nSaldo insuficiente.\n"
        else:
            self.saldo -= valor
            self.saques.append(valor)
            return f"\nSaque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}\n"
        
    
    def extrato(self):
        print("\n====Extratos====\n")
        extrato = "\nDepósitos:\n"
        for deposito in self.depositos:
            extrato += f"R$ {deposito:.2f}\n"
        extrato += "\nSaques:\n"
        for saque in self.saques:
            extrato += f"R$ {saque:.2f}\n"
        extrato += f"\nSaldo atual: R${self.saldo:.2f}\n"
        return extrato
    
def menu():
    print("====Menu====\n")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    
def main():
    conta = contabancaria()
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção: \n")
        
        if opcao == "1":
            valor = float(input("\nDigite o valor a ser depositado: \n"))
            print(conta.deposito(valor))
        elif opcao == "2":
            valor = float(input("\nDigite o valor a ser sacado: \n"))
            print(conta.saque(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4":
            print("\nSaindo do programa...\n")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.\n")


if __name__ == "__main__":
    main()