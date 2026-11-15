import json
from datetime import datetime

#class Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False #hasta que nosotros no le demos indicacion de que esta completado
        #debe mantenerse en falso (sin completar)


    def marcar_completada (self):
        self.completado = True

    def editar_tarea (self, nuevo_titulo, nueva_descripcion, nueva_fecha)
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha