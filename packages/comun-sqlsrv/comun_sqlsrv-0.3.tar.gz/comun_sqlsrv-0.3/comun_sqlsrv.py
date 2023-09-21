import pymssql


class Sql:
    def __init__(self, servidor, database, user, passw, as_dict=True):
        self.conexion = pymssql.connect(server=servidor, user=user, password=passw, database=database)
        self.cursor = self.conexion.cursor(as_dict=as_dict)

    def cerrar_conexion(self):
        self.conexion.close()

    def ejecutar(self, texto, *parametros):
        try:
            if len(parametros):
                if type(parametros[0]) == tuple:
                    parametros = parametros[0]
            self.cursor.execute(texto, parametros)
            self.conexion.commit()
        except Exception as e:
            print(texto)
            print(parametros)
            print(e)
            raise Exception(e)

    def consultar(self, consulta, params=None):
        self.cursor.execute(consulta, params)
        return self.cursor.fetchall()

