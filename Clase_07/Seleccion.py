


class Seleccion:
    def __init__(self,pais,confederacion):
        self.pais = pais
        self.confederacion = confederacion
        self.jugadores = []
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador) 
    
    def eliminar_jugador(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)
                break
                    
argentina = Seleccion("Argentina", "Conmebol")
brasil= Seleccion("Brasil", "Conmebol")

argentina.agregar_jugador("Messi")
brasil.agregar_jugador("Neymar")
argentina.agregar_jugador("Di Maria")

print(argentina.jugadores)
print(brasil.jugadores)
argentina.eliminar_jugador("Di Maria")

