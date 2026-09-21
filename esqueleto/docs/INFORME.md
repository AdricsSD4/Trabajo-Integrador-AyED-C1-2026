# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:musica
- Por qué lo eligieron (5–8 líneas):Elegimos este tema porque casualmente es un interes compartido, ademas de llamar nuestra atencion la posibilidad de comprender como funciona la logica de varias aplicaciones de repruduccion musical construyendo nuestra propia playlist

## 2. Modelo

Qué es un ítem del catálogo(Es el objeto musica completo que permite mover todos los datos juntos para usarlos). Qué es mutable y qué no (Los datos iniciales del catalago son inmutables ya que no se puede modificar una vez que se los declara dentro del catalogo.Si es mutable las listas de reproduccion, agregando y sacando canciones) (E1). Cómo se relacionan catálogo, colección principal, pila y cola(Musica proporciona los atributos a catalogo el cual permite clasificar las canciones y crea una lista que genera una pila y una cola de reproduccion que selecciona las canciones que quieran escuchar).

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función:"versiones_de(self, id_cancion)" en la clase "Catalogo"
- Caso base: Cuando la función consulta por un ID que no tiene versiones registradas, recibe una lista vacía []. Como ya no hay más canciones para seguir explorando, corta la recursión ahi y retorna el resultado
- Caso recursivo: Si encuentra covers de la canción, guarda sus IDs y vuelve a revisar uno por uno para ver si esos covers tienen a su vez más versiones
- Traza de un ejemplo real del dataset: Probamos la busqueda arrancando desde la canción original "De Música Ligera" (ID 1). En nuestro catalogo, esta cancion se conecta directamente con el ID 5 (El Último Concierto) y con el ID 6 (Cover de Coldplay). A su vez, el ID 6 se conecta con el ID 7 (Cover del Cover)

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
