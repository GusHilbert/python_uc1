class veiculo:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_info(self):
        print(f"{self.marca} {self.modelo} {self.ano} {self.cor}")

class carro(veiculo):
    def __init__(self,marca,modelo,ano,portas,cor,placa):
        super().__init__(marca,modelo,ano,cor)
        self.portas = portas
        self.placa = placa

    def exibir_info(self):
        super().exibir_info()
        print(f"Este carro tem {self.portas} portas. E a placa é {self.placa}")

# meu_carro = carro("Toyota","Corolla",2020,4)


if __name__ == "__main__":
    meu_carro = carro("Toyota","Corolla",2020,4,"Vermelho","Placa")
    meu_carro.exibir_info()