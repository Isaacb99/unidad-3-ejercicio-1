import csv
from claseFacultad import facultad
from claseCarrera import carrera

class manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
    
    def cargar_archivo(self):
        archivo = open("facultades.csv")
        reader = csv.reader(archivo,delimiter=(','))
        for elem in reader:
            cantidad = int(elem[5])
            f = facultad(int(elem[0]), elem[1], elem[2], elem[3], elem[4], elem[5])
            self.__lista.append(f)
            for elem1 in reader:
                f.agregar_carrera(int(elem1[1]), elem1[2], elem1[3], elem1[4])
                cantidad -= 1
                if cantidad == 0:
                    break
    def __str__(self):
        valorDeRetorno=''
        for elem in self.__lista:
            valorDeRetorno+=str(elem)
            valorDeRetorno+='\n'
        return valorDeRetorno
    def listar(self):
            print(str(self))
    def busqueda(self):
        c = int(input("ingrese codigo de facultad a buscar"))
        i = 0
        while self.__lista[i].get_codigo() != c:
            i += 1
        print("Nombre de facultad:")
        print("{}".format(self.__lista[i].get_carrera()))