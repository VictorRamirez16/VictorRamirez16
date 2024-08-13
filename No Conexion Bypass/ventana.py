import tkinter as tk
from tkinter import ttk
import automata
import db_connection

def ejecutar_automatizacion(expediente):
    # Llamar a la función de abrir página y pegar código
    automata.abrir_y_pegar_codigo(expediente)

    # Llamar a la función para ejecutar las acciones automatizadas
    contenido_portapapeles = automata.automatizar_acciones()

    # Imprimir el contenido del portapapeles
    if contenido_portapapeles is not None:
        print("Contenido del portapapeles:")
        print(contenido_portapapeles)

def mostrar_ventana():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Selección de Expediente")

    # Establecer el tamaño de la ventana
    root.geometry("1000x600")  # Ancho x Alto en píxeles

    # Obtener los datos de la base de datos
    datos_casos = db_connection.obtener_datos_casos()

    # Crear la tabla
    columnas = ("Numero", "Cliente", "Demanda_Solicitud", "Materia", "Expediente", "Juzgado_Institucion", "Sede")
    tabla = ttk.Treeview(root, columns=columnas, show="headings")
    tabla.heading("Numero", text="Numero")
    tabla.heading("Cliente", text="Cliente")
    tabla.heading("Demanda_Solicitud", text="Demanda/Solicitud")
    tabla.heading("Materia", text="Materia")
    tabla.heading("Expediente", text="Expediente")
    tabla.heading("Juzgado_Institucion", text="Juzgado/Institucion")
    tabla.heading("Sede", text="Sede")

    # Insertar los datos en la tabla
    for numero, cliente, demanda, materia, expediente, juzgado, sede in datos_casos:
        tabla.insert("", "end", values=(numero, cliente, demanda, materia, expediente, juzgado, sede))

    # Definir el evento de doble clic en un expediente
    def on_double_click(event):
        item = tabla.selection()[0]
        expediente = tabla.item(item, "values")[4]
        ejecutar_automatizacion(expediente)

    tabla.bind("<Double-1>", on_double_click)
    tabla.pack(fill="both", expand=True)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

if __name__ == "__main__":
    mostrar_ventana()
