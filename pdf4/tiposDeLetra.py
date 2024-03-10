from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Creamos un canvas

canvas = canvas.Canvas("./tiposDeLetra.pdf", pagesize=A4)

#Creamos el objeto Writer

writer = canvas.beginText()
writer.setTextOrigin(25, 421) # X e Y
writer.setFont("Helvetica", 14)

writer.setFillColorRGB(0, 0, 1) # RGB 0 o 1

# Ahora recorremos todas las letras y escribir una frase con un tipo de letra diferente

space = 0
for letra in canvas.getAvailableFonts():
    writer.setCharSpace(space) # Ajustamos el espacio entre caracteres
    writer.setFont(letra, space)
    writer.textLine(letra + " - Tipo de letra")
    space += 1
    writer.moveCursor(space, space)
    # Ahora debemos mover el cursor para que no se sobrepongan las letras
    # (No pasa eso, ya que el textLine pone un salto de línea al final, pero con el cursor podemos mover la posición de las letras, por ejemplo...
    #writer.moveCursor(cursor -20, cursor +40)


# Como siempre, aplicamos
canvas.drawText(writer)
canvas.save()