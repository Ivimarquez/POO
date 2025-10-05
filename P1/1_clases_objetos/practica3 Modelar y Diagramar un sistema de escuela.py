import os
os.system ("cls")

class Profesores:
    def __init__(self, nombre_Profesores, experiencia, num_profesores):
        self.__nombre_Profesores=nombre_Profesores
        self.__experiencia=experiencia
        self.__num_profesores=num_profesores

    def getNombreProfesores(self):
        return self.__nombre_Profesores

    def setNombreProfesores(self, nombre_Profesores):
        self.__nombre_Profesores=nombre_Profesores

    def getExperiencia(self):
        return self.__experiencia

    def setExperiencia(self, experiencia):
        self.__experiencia=experiencia

    def getnum_profesores(self):
        return self.__num_profesores

    def setnum_profesores(self, num_profesores):
        self.__num_profesores=num_profesores

class Alumnos:
    def __init__(self, nombre_Alumnos, edad, matricula):
        self.__nombre_Alumnos=nombre_Alumnos
        self.__edad=edad
        self.__matricula=matricula

    def getNombreAlumnos(self):
        return self.__nombre_Alumnos

    def setNombreAlumnos(self, nombre_Alumnos):
        self.__nombre_Alumnos=nombre_Alumnos

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad=edad

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula=matricula

class Cursos:   
    def __init__(self, nombre_Cursos, codigo, creditos):
        self.__nombre_Cursos=nombre_Cursos
        self.__codigo=codigo
        self.__creditos=creditos

    def getNombreCursos(self):
        return self.__nombre_Cursos

    def setNombreCursos(self, nombre_Cursos):
        self.__nombre_Cursos=nombre_Cursos

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo=codigo

    def getCreditos(self):
        return self.__creditos

    def setCreditos(self, creditos):
        self.__creditos=creditos



Profesor1=Profesores("Ana Torres Guzman", "40", "123")
Profesor2=Profesores("Daniel Contreras", "35", "124")

Alumno1=Alumnos("Jose", "25", "100123")
Alumno2=Alumnos("Maria Serrano Mata", "22", "100124")

Curso1=Cursos("POO", "100", "6")
Curso2=Cursos("FOSO", "101", "4")