
class Pelota():
    tipo = "Basket"
    talla = 7
    liga = "ACB"
    def hablar(self):
        return f"Hola, soy una pelota de {self.tipo} que juega en la liga {self.liga}!! La talla que soy es {self.talla}.\nEscoge una accción."
    
    def lanzar (self):
        quiz = input("Me has lanzado, pero para determinar el resultado tienes que responder a la siguiente pregunta:\n¿Quién es el mejor jugador de todos los tiempos de baloncesto? ")
        if quiz in {"Michael Jordan", "Jordan", "michael jordan"}:
            return f"El tiro ha sido un éxito, y ahora puedes jugar en la {self.liga}."
        else:
            return f"Respuesta incorreta, parece que no tienes mucha idea del básquet, y así \nlo has demostrado con tu juego: has errado el tiro,\nasí que mejor no te dediques al {self.tipo}."
            
    

Eduard = Pelota()
def main():
    iniciar = input("Para iniciar el juego, pulse enter. ")
    if iniciar == "":
        print(Eduard.hablar())
        
    print(Eduard.lanzar())

main()