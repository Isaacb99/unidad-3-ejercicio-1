from claseCarrera import carrera


class facultad:
    __codigo =0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __cant_carreras = 0
    __lista_carreras = []
    def __init__(self, c, n, d, l, t, cant):
        self.__codigo = c
        self.__nombre = n
        self.__direccion = d
        self.__localidad = l
        self.__telefono = t
        self.__cant_carreras = cant
        self.__lista_carreras = []
    def __str__(self):
        valorDeRetorno = ''
        valorDeRetorno = "{}  {}  {}  {}  {}  {} \n \n".format(self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono, self.__cant_carreras)
        val = ''
        for carrera in self.__lista_carreras:
            val += str(self.__codigo) + '   '
            val += str(carrera)
        return  valorDeRetorno+val
    
    def agregar_carrera(self, c, n, d, t):
        self.__lista_carreras.append(carrera(c,n,d,t))

    def get_codigo(self):
        return self.__codigo
    
    def get_carrera(self):
        v = ''
        v = self.__nombre + '\n'
        valor = ''
        valor += 'Carreras: \n'
        for carrera in self.__lista_carreras:
            valor += carrera.get_nom() + '  '
            valor += carrera.get_duracion()
            valor += '\n'
        return v+'\n'+valor