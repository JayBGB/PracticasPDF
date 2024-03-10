from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Image, Drawing

# Creamos una lista que contendrá los objetos Drawing

imagenes = []

# Creamos el objeto de tipo Drawing

drawing = Drawing()

# Tamaño máximo de un A4 = 595 x 842

imagen = Image(200, 400, 160, 160, "./biologia.png")
drawing.add(imagen)

# Posible modificación: trasladar la imagen 200 hacia la derecha y arriba
# drawing.translate(200, 200)

# Guardamos el objeto Drawing en una lista (se debería añadir "drawing", no "imagen")

imagenes.append(drawing)

# Creamos un nuevo objeto Drawing con el tamaño de un A4

drawing = Drawing(A4[0], A4[1])

# Añadimos cada objeto Drawing individualmente a la nueva página A4

drawing.add(imagenes[0])

# Creamos el archivo PDF y añadimos el objeto Drawing con la lista de objetos Drawing

renderPDF.drawToFile(drawing, "./imagenes.pdf")