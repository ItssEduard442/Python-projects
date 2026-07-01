# Interfaz en la que puedes pregutnar por información sobre videojuegos.


class Videojuegos:
    def __init__(self, juego, año, tipo):
        self.juego = juego
        self.año = año
        self.tipo = tipo
    
    def saludar(self):
        return f"Hola usuario, este es el {self.juego} que salió el año {self.año}. ¡Soy un juego de {self.tipo}\nque te va a encantar!"

Farcry = Videojuegos("Farcry", "2016", "acción")
Fortnite = Videojuegos("Fortnite", "2019", "shooter")
# .
# .
# .

print(Farcry.saludar())
print(Fortnite.saludar())

# .
# .
# .
