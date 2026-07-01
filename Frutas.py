# Programa que agrupa las frutas que les gusta a la gente según un
# formulario. No importa la cantidad de veces que la fruta haya sido votada.

frutas = []

while True:
    frut = input("Fruta favorita: ")
    if frut == "fin":
        break
    else:
        frutas.append(frut)

frutas_sin_repetir = set(frutas)

print(frutas_sin_repetir)

