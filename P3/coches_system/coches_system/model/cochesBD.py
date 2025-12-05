from conexionBD import cursor, conexion
class Autos:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("INSERT INTO autos VALUES(NULL,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas))
            conexion.commit()
            return True
        except: return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM autos"); return cursor.fetchall()
        except: return []
    @staticmethod
    def consultarID(id):
        try:
            cursor.execute("SELECT * FROM autos WHERE id=%s",(id,)); return cursor.fetchall()
        except: return []
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        try:
            cursor.execute("UPDATE autos SET marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s WHERE id=%s",(marca,color,modelo,velocidad,caballaje,plazas,id))
            conexion.commit(); return True
        except: return False
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM autos WHERE id=%s",(id,)); conexion.commit(); return True
        except: return False
