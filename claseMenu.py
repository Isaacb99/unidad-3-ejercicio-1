from manejaFacultades import manejador

class menu:
    __op = 0
    def __init__(self, op=0):
        self.__op = op
    
    def opciones(self):
        f = manejador()
        f.cargar_archivo()
        f.listar()
        salir = True
        while salir:
            print("/// menu de opciones ///")
            print("opcion 1: buscar facultad")
            print("opcion 2:")
            print("opcion 3: salir del programa")
            self.__op = int(input("ingrese opcion"))
            if self.__op == 1:
                f.busqueda()
            elif self.__op == 2:
                print()
            elif self.__op == 3:
                salir = not salir
            else: print("--- opcion incorrecta ---")