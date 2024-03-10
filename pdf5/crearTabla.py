from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Comenzamos a crear una tabla.
# Lo primero es crear una hoja de estilos en la que vamos a situar la tabla.

stylesheet = getSampleStyleSheet()

# Esta tabla constará de una imagen y otros títulos diferentes en cada fila

imagen = Image("./biologia.png", 20, 50)

bodyTextStyle = stylesheet["BodyText"] # Obtenemos el estilo de la tabla en una variable
bodyTextStyle.textColor = Color(0, 0, 250, 0.5) # Indicamos el color que tendrá el texto de la tabla

# Editamos el estilo del título

titleStyle = stylesheet["Heading1"] # Podemos indicar, igual que en HTML, si es 1, 2, 3 o 4

# Creamos un párrafo con el estilo del Body, ya que será un campo de la tabla

companyData1 = Paragraph("Tesla", style=bodyTextStyle)
companyTitle1 = Paragraph("ELON MUSK", titleStyle)

tableElements = [] # En este Array meteremos los elementos de la tabla

# La información de la tabla la almacenamos en otro Array

tableInfo = [
    # Cabecera
    ["Company", "Product", "Price", "Offer"],

    #Datos
    ["Microsoft", "Windows X", "$500 M", "A chocolate bar"],
    [[companyData1, companyTitle1], "Ultra Pluto Rocket", "$5000M", "Two smiles and Twitter"],
    [[companyData1, imagen], "Biology Xpress", "$3", "Half of Ukraine"]
]

# Ahora le daremos un poco de estilo a la tabla para mejorar la estética

style = [
    # Estilo, (inicio de columna, inicio de fila), (final de columna, final de fila), color

    # Color de texto
    ("TEXTCOLOR", (0,0), (0,-1), colors.blue),
    ("TEXTCOLOR", (1,0), (-1,0), colors.red),
    ("TEXTCOLOR", (1,1), (-1,-1), colors.yellowgreen),

    # Borde exterior (celdas)
    ("BOX", (0,0), (-1, -1), 2, colors.gray),

    # Borde interior (celdas)
    ("INNERGRID", (0, 0), (-1, -1), 1, colors.gray),

    # Alineamos los elementos de la tabla (izquierda, medio, derecha)
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]

# Ahora, con los datos de la tabla creados, creamos el estilo que tendrá la tabla

tabla = Table(data=tableInfo, style=style, colWidths=[150, 100, 100, 120], rowHeights=[30, 30, 100, 100])

# Añadimos la tabla a nuestro Array de elementos

tableElements.append(tabla)

documento = SimpleDocTemplate("./tabla.pdf", pagesize = A4, showBoundary = 0)
documento.build(tableElements)