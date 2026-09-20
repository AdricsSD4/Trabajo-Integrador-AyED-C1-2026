from esqueleto.src.dominio.Catalogo import Catalogo
def main():
    
    mi_catalogo = Catalogo()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar versiones derivadas de una canción (Recursión)")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                
                id_buscar = int(input("Ingresa el ID de la canción (ej: 1 o 4): "))
                
                
                resultado_versiones = mi_catalogo.versiones_de(id_buscar)
                
                if resultado_versiones:
                    print(f"\n¡Se encontraron estas versiones derivadas!: {resultado_versiones}")
                else:
                    print("\nEsta canción original no tiene versiones derivadas. (Se ejecutó el caso base).")
            except ValueError:
                print("Por favor, ingresa un número de ID válido.")
                
        elif opcion == "0":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()