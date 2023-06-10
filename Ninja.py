class Ninja:
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota ):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self): # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
        self.mascota.jugar()

    def alimentar(self): #alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
        self.mascota.comer()

    def banar(self): #bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
        self.mascota.sonido()