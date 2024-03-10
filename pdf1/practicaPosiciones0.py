from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Meter reportlab en el Interpreter

# En primer lugar, creamos un canvas al que meteremos todos los elementos que creemos.

canvas = canvas.Canvas("./practicaPosiciones0.pdf", pagesize=A4) # Nombramos al futuro PDF y establecemos tamaño

# Y ahora codificamos lo que se va a escribir

canvas.drawString(0, 0, "Hello, how you doin'?")# Esto escribe una sola línea, a la que indicamos la posición X e Y
                                                           # X es el eje horizontal. Para moverlo a la derecha, aumentamos su valor
                                                           # Y es el eje vertical. Para moverlo hacia arriba, aumentamos su valor

canvas.drawString(100, 0, "Texto hacia la derecha 100 puntos, misma altura.")
canvas.drawString(100, 100, "Texto movido a la derecha 100 puntos, elevado 100 puntos")

# Por supuesto, también podemos añadir imágenes a nuestro PDF

canvas.drawImage("./biologia.png",25,200, 100,100) # Indicamos la ruta y su posición en X e Y
                                                                            # Indicamos también el tamaño de la imagen, valores width y height
                                                                            # De esta forma se puede modificar para ajustar el tamaño

# Guardamos los cambios para aplicarlos al canvas

canvas.save()