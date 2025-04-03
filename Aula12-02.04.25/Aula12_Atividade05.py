import random

class conta:
    def __init__(self,numero_conta,nome,saldo):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
        print(f"A conta {numero_conta} do {nome} tem um saldo de R$ {saldo:.2f}")

    def deposito(self,valor):
        self.valor = valor
        self.saldo = self.saldo + valor
        print(f"Seu deposito foi de R${valor:.2f}, ficando com o saldo de: R${self.saldo:.2f}")


    def saque(self,valor,limite):
        self.valor = valor
        self.limite = limite
        if (valor+limite) > cc1.saldo:
                print(f"Você não pode sacar essa quantidade, o seu saldo {self.saldo:.2f} com o seu limite R$ {limite} é menor do que o valor desejado")        
        else:    
            self.saldo = self.saldo - valor 
            print(f"Você sacou {valor_saque:.2f}, seu saldo é de: {self.saldo:.2f} é menor do que o valor desejado")    



    def exibir(self):
        print(f"A conta {self.numero_conta} do {self.nome} tem um saldo de R${self.saldo:.2f}")
    

class banco:
    def __init__(self):
        contas = {}
        pass

    def adicionar_contas():
        pass

if __name__ == "__main__":
    cc1 = conta("000001","Gustav",1500)
    # nome = input("Qual é o seu nome? ")
    # saldo = float(input("Qual é o saldo da sua conta? "))
    # conta_ = random.randint(1,1000000)
    
    valor_deposito = float(input("Qual é o valor do seu deposito? "))
    cc1.deposito(valor_deposito)

    valor_saque = float(input("Qual é o valor do seu saque? "))
    limite1 = float(input("Qual é o valor do seu limite? "))
    cc1.saque(valor_saque,limite1)
    