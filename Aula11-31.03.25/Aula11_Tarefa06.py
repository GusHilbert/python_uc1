class Carro:

    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    
    def exibir_info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} {self.ano}")

    def ligar_carro(self):
        self.ligado = True
        print(f"O carro está ligado")
    
    def desligar_carro(self):
        self.ligado = False
        print(f"O carro está desligado")

if __name__ == "__main__":
    print(f"Criando um objeto em Python")
    meu_carro = Carro("Toyota","Corolla",2022)
    carro_luis = Carro("Nissan","370z",2011)
    carro_professor = Carro("VW","Passat",2020)
    meu_carro.desligar_carro()

    print (meu_carro.ano)


    if carro_luis != carro_professor:
        print(f"O carro do professor ({modelo(carro_luis)}) é diferente do carro do luis: ({carro_luis})")


    # meu_carro.exibir_info()
    # carro_luis.exibir_info()
    # carro_professor.exibir_info()


    