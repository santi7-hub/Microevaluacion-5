import tkinter as tk

print("Iniciando la aplicación...")

# Crear la ventana principal
root = tk.Tk()
root.title("Triángulo Rojo")

# Definir el tamaño de la ventana
root.geometry("400x400")

# Crear un canvas donde dibujaremos el triángulo
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Dibujar un triángulo (en las coordenadas x1, y1, x2, y2, x3, y3)
canvas.create_polygon(200, 50, 50, 350, 350, 350, fill="red", outline="black", width=2)

# Mostrar la ventana
print("Mostrando la ventana...")
root.mainloop()  # Esta línea asegura que la ventana se quede abierta
