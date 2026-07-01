# Descartar a gente de una lista de invitaciones. Las que no cumplan con cierta
# edad no pueden entrar. Se guardarán en una lista nueva las que sí.


## Definir variables

lista1 = ["Ana","Luis","María","Carlos"]
lista2 = list()

nombre_y_edad = dict()

## Definir funciones internas

def edades():
    for nombre in lista1:
        edad = int(input(f"Edad de {nombre}: "))
        nombre_y_edad[nombre] = edad

def verificar():
    for nombre, edad in nombre_y_edad.items():
        if edad >= 16:
            lista2.append(nombre)
            for n in lista2:
                print(f"{n} sí puede.")

##Definir función principal

def portero_automático():
    print("----Día 1----\n")
    edades()
    print("\n---Reconocimiento completado---\n")
    verificar()
    print("\n---Fin del día---")

portero_automático()