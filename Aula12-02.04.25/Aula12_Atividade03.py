class Animal:
    def fazer_som(self):
        pass

class cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class gato(Animal):
    def fazer_som(self):
        print("Miau!")

def fazer_barulho(Animal):
    Animal.fazer_som()

meu_cachorro = cachorro()
meu_gato = gato()

if __name__ == "__main__":
    animal1 = input("Qual animal vc quer ouvir o som? ").lower()
    print(animal1)
    if animal1 == "cachorro":
        fazer_barulho(meu_cachorro)
    else:
        fazer_barulho(meu_gato)