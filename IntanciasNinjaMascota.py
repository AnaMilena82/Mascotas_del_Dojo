from Ninja import Ninja
from Mascota import Mascota, Perro


#crear instancias 
mascota = Mascota("Fluffy", "Perro", 5, 100, 80)

#Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.
ninja = Ninja("Hiro", "Sakura", 3, "Croquetas", mascota)
   
#Haz que el ninja alimente, pasee y bañe a su mascota.
ninja.alimentar()
ninja.caminar()
ninja.banar()

perro = Perro("PuPy", 3, 100, 80)
perro.ladrar()
perro.jugar()
print(perro.salud)
