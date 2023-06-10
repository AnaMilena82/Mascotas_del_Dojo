class Mascota:
    def __init__(self, name , tipo , golosinas, energia, salud):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = energia
        self.salud = salud
        

    def dormir(self):  # dormir() - incrementa la energía de la mascota en 25
        self.energia += 25

    def comer(self): #comer() - incrementa la energía de la mascota en 5 y la salud en 10
        self.energia += 5
        self.salud += 10

    def jugar(self):  # jugar() - incrementa la salud de la mascota en 5
        self.salud +=5

    def sonido(self): #ruido() - imprime el sonido que produce la mascota
        print("La mascota hace un sonido")

class Perro(Mascota):
    def __init__(self, nombre, golosinas, energia, salud):
        super().__init__(nombre, "Perro", golosinas, energia, salud)

    def ladrar(self):
        print("¡Guau guau!")

    def jugar(self):
        super().jugar()
        self.salud += 10


