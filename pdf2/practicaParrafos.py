from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Como siempre, creamos el canvas

canvas = canvas.Canvas("./textos.pdf", pagesize=A4)

# Creamos un array de frases

frases = [
    "Me gusta The Blacklist",
    "Pero vaya mierda de final",
    "Sin pena ni gloria",
    "Así, a lo súper cutre",
    "Es que me cago en mi vida"
]

# Dado que vamos a utilizar un objeto y texto (Array), no crearemos un drawString como en pdf1.

writer = canvas.beginText() # Creamos un objeto writer

writer.setTextOrigin(250, 420) # Indicamos la posición en la que lo vamos a escribir. Teniendo en cuenta que A4 595 x 842, lo ponemos aproximadamente a la mitad

writer.setFont("Courier", 14) # Indicamos la fuente y el tamaño de la letra

# Procedemos con la escritura de las frases en el PDF

for frase in frases:

    writer.textLine(frase)

# Ejecutamos los cambios

canvas.drawText(writer)
canvas.showPage()
canvas.save()