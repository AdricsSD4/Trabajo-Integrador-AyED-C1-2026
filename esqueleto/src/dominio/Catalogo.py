from dominio.Musica import musica

class Catalogo:
    def __init__(self):
        self.canciones = [
            musica(1, "De Música Ligera", "Soda Stereo", "Canción Animal","rock",213),
            musica(2, "Persiana Americana", "Soda Stereo", "Signos","rock",263),
            musica(3,"En la Ciudad de la Furia","Soda Stereo","Doble Vida","rock",351),
            musica(4,"Crimen","Gustavo Cerati","Ahí vamos","rock",239)]

    def playlist(self):
        for x in self.canciones:
            print(f"Este es nuestro Catalogo {x.artista} - {x.titulo}")


        eleccion = int(input(f"Ingresa el número de la canción que queres escuchar esta es nuestra lista: "))
       
        cancion_encontrada = None
        for c in self.canciones:
            if c.id == eleccion:
                cancion_encontrada = c
                print(f"Estás escuchando: {cancion_encontrada.titulo} de {cancion_encontrada.artista}")

    
                
 

mi_catalogo=Catalogo()
mi_catalogo.playlist()


    