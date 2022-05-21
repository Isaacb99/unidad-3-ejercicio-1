

class carrera:
    __codigo = 0
    __nombre = ""
    __duracion = ""
    __titulo = ""
    def __init__(self, c, n, d, t):
        self.__codigo = c
        self.__nombre = n
        self.__duracion = d
        self.__titulo = t
    def __str__(self):
        return  "{}  {}  {}  {} \n".format(self.__codigo, self.__nombre, self.__duracion, self.__titulo)
    def get_nom(self):
        return self.__nombre
    def get_duracion(self):
        return self.__duracion
    def get_nom(self):
        return self.__nombre
    def get_duracion(self):
        return self.__duracion
