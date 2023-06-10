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
    
#crear instancias 
mascota = Mascota("Fluffy", "Perro", 5, 100, 80)

#Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.
ninja = Ninja("Hiro", "Sakura", 3, "Croquetas", mascota)
   
#Haz que el ninja alimente, pasee y bañe a su mascota.
ninja.alimentar()
ninja.caminar()
ninja.banar()
