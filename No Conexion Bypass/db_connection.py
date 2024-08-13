import pymysql

def obtener_datos_casos():
    try:
        # Conectar a la base de datos
        conexion = pymysql.connect(
            host=
            port=
            user=
            password=
            database=
        )

        cursor = conexion.cursor()

        # Consultar los datos de Numero, Cliente, Demanda_Solicitud, Materia, Expediente, Juzgado_Institucion y Sede
        cursor.execute("""
            SELECT Numero, Cliente, Demanda_Solicitud, Materia, Expediente, Juzgado_Institucion, Sede
            FROM DataCaptcha
        """)

        # Obtener todos los registros
        casos = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        return casos

    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []


# Prueba manual de la conexión (opcional)
if __name__ == "__main__":
    datos = obtener_datos_casos()
    for numero, cliente, demanda, materia, expediente, juzgado, sede in datos:
        print(f"Numero: {numero}, Cliente: {cliente}, Demanda_Solicitud: {demanda}, Materia: {materia}, Expediente: {expediente}, Juzgado_Institucion: {juzgado}, Sede: {sede}")
