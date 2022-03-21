from pip import main
import animales
#Menu 
#While
#Funciones
#dibujos 
#Classes

menu = {
    "1" : "1. Perro",
    "2" : "2. Gato",
    "3" : "3. Serpiente",
    "4" : "4. Amoeba",
    "0" : "0. Exit",
}

class Animal():
    def __init__(self, type) :
        self.type = type

    def mostrar_animal(self):
        #Get atributos de aniamles 
        animal_art = getattr(animales,self.type)
        return animal_art

#Ejecición prinipal
if __name__ == '__main__':
    print("Selecciones una opción:")

    #Membership operator
    for option in menu:
        print(menu.get(option))

    while True:
        user_input = input("Ingresa una opción")
        if user_input == "0":
            #Quiere dejar de jugar 
            print("Hasta luego")
            break
        elif user_input in menu:
            #Formato de input en munero a nombre de animal
            menu_value = menu.get(user_input)
            menu_value.split("")
            #animal= Animal(user_input)
            print("animal")
            pass
        else:
            #Opcion invalida
            print ("Opción invalida")
            pass
