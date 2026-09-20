from dominio.Catalogo import Catalogo

class playlist:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.canciones_playlist = []

    def mostrar_lista(self):
        # 1. Recorremos las canciones del catálogo recibido
        for x in self.catalogo.canciones:
            print(f"Este es nuestro Catalogo: {x.artista} - {x.titulo}")

        while True:
            eleccion = int(input("\nIngresa el numero de la cancion que quieres escuchar esta es nuestra lista o 0 para terminar: "))

            if eleccion == 0:
                print("Seleccion finalizada:")
                break

            cancion_encontrada = None
            for c in self.catalogo.canciones:
                if c.id == eleccion:
                    cancion_encontrada = c
                    break

            if cancion_encontrada:
                self.canciones_playlist.append(cancion_encontrada)
                print(f"Estas escuchando: {cancion_encontrada.titulo} de {cancion_encontrada.artista}")
            else:
                print("Cancion no encontrada")


mi_catalogo = Catalogo()
mi_playlist = playlist(mi_catalogo)
mi_playlist.mostrar_lista()

