# Creando un programa en el que se busque a un trabajador en un puesto de trabajo
# a través de criterios como los años de experiencia, edad y disponibilidad. El
# programa va haciendo preguntas al solicitante y revisa si coinciden sus datos con
# aquello que busca la empresa contratista.

#Definición de variables:

## Preguntas:

nombre = input("Nombre: ")
experiencia = int(input("Experiencia (años): "))

def disponibilidad():
    while True:
        print("Seleccione el horario que mejor le convenga según el orden en que salen:")
        print("1. Entre semana (mañanas).")
        print("2. Entre semana (tardes).")
        print("3. Entre semana (noches).")
        print("4. Ninguna de las anteriores.\n")
        elección = int(input("Opción nº: \n"))
        if elección == 4:
            print(f"Lo siento, pero no eres apto/a, {nombre}.")
            break
        else:
            print("Gracias por rellenar el formulario,\nnos pondremos en contacto contigo pronto.")
            break
## Determinación de apto:

if experiencia >= 3:
    disponibilidad()
else:
    print(f"Lo siento, pero no eres apto/a, {nombre}.")