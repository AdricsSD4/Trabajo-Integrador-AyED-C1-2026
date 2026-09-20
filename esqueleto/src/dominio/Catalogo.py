from esqueleto.src.dominio.Musica import musica
class Catalogo:
    def __init__(self):

        self.canciones = [
            musica(1, "De Música Ligera", "Soda Stereo", "Canción Animal", "rock", 213),
            musica(2, "Persiana Americana", "Soda Stereo", "Signos", "rock", 263),
            musica(3, "En la Ciudad de la Furia", "Soda Stereo", "Doble Vida", "rock", 351),
            musica(4, "Crimen", "Gustavo Cerati", "Ahí vamos", "rock", 239),
            
         
            musica(5, "De Música Ligera (Último Concierto)", "Soda Stereo", "El Último Concierto", "rock", 250),
            musica(6, "De Música Ligera (Cover)", "Coldplay", "Live In Buenos Aires", "rock", 240),
            musica(7, "De Música Ligera (Cover del Cover)", "Banda Local", "Demo", "rock", 200)
        ]
        
    
        self.relaciones = {
            1: [5, 6],
            6: [7]
        }

    
    def buscar_versiones_directas(self, id_cancion):
       
        if id_cancion in self.relaciones:
            return self.relaciones[id_cancion]
        return []

    def versiones_de(self, id_cancion):
        directas = self.buscar_versiones_directas(id_cancion) 
        
        if not directas:
            return [] 
            
        resultado = list(directas)
        
        for v in directas:
            resultado += self.versiones_de(v)
            
        return resultado
    