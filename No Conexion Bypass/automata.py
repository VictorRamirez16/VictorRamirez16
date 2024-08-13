import pyautogui
import time
import keyboard
import pyperclip
import webbrowser

time_wait_page = 3
time_wait_click = 0.5
def abrir_y_pegar_codigo(codigo):
    try:
        # Abrir la página web
        url = "https://cej.pj.gob.pe/cej/forms/busquedaform.html"  # Reemplaza con la URL deseada
        webbrowser.open(url)
        time.sleep(time_wait_page)  # Esperar a que la página web se abra

        # Hacer clic en la ubicación especificada
        pyautogui.click(1147, 271)
        time.sleep(time_wait_click)

        # Hacer clic en la ubicación especificada
        pyautogui.click(779, 369)
        time.sleep(time_wait_click)

        # Pegar el código de entrada
        pyperclip.copy(codigo)
        keyboard.send('ctrl+v')
        time.sleep(time_wait_click)

    except Exception as e:
        print(f"Ocurrió un error: {e}")

def automatizar_acciones():
    try:
        # Hacer clic en la primera ubicación
        pyautogui.click(971, 720)
        time.sleep(time_wait_click)  # Esperar después del primer clic

        # Presionar F12
        keyboard.send('F12')
        time.sleep(time_wait_click)  # Esperar después de presionar F12

        # Continuar con los clics en las ubicaciones siguientes
        coordenadas = [
            (998, 245),
            (1011, 313),
            (1022, 363),
            (1036, 468),
            (1542, 484)
        ]

        for coord in coordenadas:
            pyautogui.click(coord[0], coord[1])
            time.sleep(time_wait_click)  # Esperar entre cada clic

            # Verificar si se presionó la tecla Esc para detener la función
            if keyboard.is_pressed('esc'):
                print("Se presionó la tecla Esc. Deteniendo la función...")
                return  # Salir de la función si se presiona Esc

        # Doble clic en la última coordenada
        pyautogui.doubleClick(coordenadas[-1][0], coordenadas[-1][1])
        time.sleep(time_wait_click)

        # Presionar Ctrl + C (copiar)
        keyboard.send('ctrl+c')
        time.sleep(time_wait_click)

        # Presionar F12
        keyboard.send('F12')
        time.sleep(time_wait_click)  # Esperar después de presionar F12

        # Obtener el contenido del portapapeles
        clipboard_content = pyperclip.paste()

        # Hacer clic en 1028, 719 y pegar el contenido del portapapeles
        pyautogui.click(1028, 719)
        time.sleep(time_wait_click)
        keyboard.send('ctrl+v')
        time.sleep(time_wait_click)

        # Hacer clic en 946, 770
        pyautogui.click(946, 770)

        return clipboard_content

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Prueba manual de las funciones (opcional)
if __name__ == "__main__":
    codigo_prueba = "codigo_de_prueba"
    abrir_y_pegar_codigo(codigo_prueba)
    contenido = automatizar_acciones()
    if contenido is not None:
        print("Contenido del portapapeles:")
        print(contenido)
