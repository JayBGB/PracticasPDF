from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Clase para posicionar la tabla en el documento

class PositionedTable(Flowable):

    def __init__(self, table, x, y):

        Flowable.__init__(self)
        self.table = table
        self.x = x
        self.y = y

    # Tras crear el constructor para posicionar una tabla al que le pasamos una tabla y su posición XY

    def draw(self):
        self.canv.saveState()  # Guarda el estado del lienzo para poder restaurarlo
        self.canv.translate(self.x, self.y)  # Posiciona la tabla con los valores XY que hayamos indicado
        self.table.wrapOn(self.canv, 0, 0)  # Ajusta el tamaño de la tabla al lienzo PDF
        self.table.drawOn(self.canv, 0, 0)  # Dibuja la tabla en el lienzo
        self.canv.restoreState() # Restaura el estado original del lienzo para poder dibujar más tablas


class Factura:

    def __init__(self):

        # Inicializamos estilos y elementos del documento
        self.hojaEstilo = getSampleStyleSheet()
        self.elementosDoc = []

        # Los elementos necesarios para construir uan factura
        # se programarán a continuación.

        '''
        Hace falta:
            - Borde izquierdo
            - Cabecera
            - Tabla superior
            - Tabla dirección y datos cliente
            - Tabla de productos
            - Total
            - Línea separadora
            - Pie de página
        '''

        self.bordeIzquierdo()
        self.titulo()
        self.nombre_logo()
        self.direccion_Facturacion()
        self.tablaFacturas()
        self.total()
        self.lineaSeparadora()
        self.piePagina()

        # Construimos el documento factura1.pdf

        documento = SimpleDocTemplate("./factura1.pdf", pagesize = A4)
        documento.build(self.elementosDoc)

    def piePagina(self):

        pie_Estilo = self.hojaEstilo["BodyText"]
        pie_Estilo.textColor = colors.darkgreen
        pie_Estilo.alignment = 1 # 0 es izquierda, 1 es centro y 2 es derecha
        pie_Estilo.fontName = "Helvetica-Bold"

        pie = Paragraph("GRACIAS POR SU CONFIANZA", pie_Estilo)
        self.elementosDoc.append(pie)

    def lineaSeparadora(self):

        elementos = [""],
        estilo = [
            ("LINEBELOW", (0,0), (-1, 0), 1, colors.black)
        ]

        tabla = Table(data = elementos, style = estilo, colWidths=[490], rowHeights=35)
        self.elementosDoc.append(Spacer(0, 20))
        self.elementosDoc.append(tabla)

    def total(self):

        elementos = [
            ["", "", "TOTAL", 495.00]
        ]

        estilo = [

            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),

            # Cambiamos el fondo
            ("BACKGROUND", (-2, 0), (-1, 0), colors.darkgreen),

            # Cambiamos el tamaño
            ("FONTSIZE", (0, 0), (-1, -1), 12),

            # Lo ponemos en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            # Alineamos hacia el centro
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            # Ajustamos el espacio entre celdas
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[210, 90, 90, 100], rowHeights=35)
        self.elementosDoc.append(Spacer(0, 25))
        self.elementosDoc.append(tabla)

    def direccion_Facturacion(self):

        elementos=[
            ["Dirección"],
            ["Ciudad y país"],
            ["CIF/NIF", "Fecha de emisión", "DD/MM/AAAA"],
            ["Teléfono", "Número de factura", "A0001"],
            ["Correo electrónico"]
        ]

        estilo = [

            # color de la letra
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.darkgreen),
            # cambiar el tamaño
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            # poner en negrita + cursiva
            ("FONTNAME", (0, 0), (1, -1), "Helvetica-BoldOblique"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia el medio
            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            # align hacia el medio
            ("ALIGN", (2, 0), (-1, -1), "CENTER"),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[300, 100, 100])
        self.elementosDoc.append(Spacer(0, 30))
        self.elementosDoc.append(tabla)

    def tablaFacturas(self):
        elementos = [
            #titulos
            ["Descripción","Importe","Cantidad","Total"],
            #datos
            ["Mushroom Dice Set", "50,00", "2", "100,00"],
            ["D&D Stickers (random)", "5,00", "3", "15,00"],
            ["Dice Tray (Mahogany)", "45,00", "1", "45,00"],
            ["GM Screen (Mahogany)", "250,00", "1", "250,00"],
            ["Initiative Tracker", "1,50", "10", "15,00"],
            ["GM Mug", "35,00", "2", "70,00"],
        ]

        estilo=[
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # color de la letra
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            # cambiar el fondo
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),
            ("BACKGROUND", (0, 1), (-1, -1), colors.lightgreen),
            # poner en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # align hacia el centro
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
            # espacio entre celdas
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[210, 90, 90, 100])
        self.elementosDoc.append(Spacer(0,30))
        self.elementosDoc.append(tabla)

    def nombre_logo(self):
        imagen = Image('./dice.png', 40,40)

        EstiloTitulo = self.hojaEstilo["Heading4"]
        titulo = Paragraph("Nåyheim S.L.", style=EstiloTitulo)
        cabeceraEmpresa= [
            ["Nombre de la empresa", [imagen,titulo]]
        ]
        estilo = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.darkgreen),
            # cambiar el tamaño
            ("FONTSIZE", (0, 0), (0, -1), 18),
            # cambiar el tamaño de la otra columna
            ("FONTSIZE", (-1, 0), (-1, -1), 14),
            # poner en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
            # vertical align
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM")
        ]

        tabla = Table(data=cabeceraEmpresa,style=estilo,colWidths=[400,100])
        self.elementosDoc.append(tabla)

    def titulo(self):
        estilo_titulo = self.hojaEstilo["Heading1"]
        estilo_titulo.alignment = 2 # 0 izquierda 1 centro 2 derecha
        estilo_titulo.textColor = colors.darkgreen
        estilo_titulo.fontSize = 16

        titulo = Paragraph("FACTURA SIMPLIFICADA", estilo_titulo)
        self.elementosDoc.append(titulo)

    def bordeIzquierdo(self):
        elementos = [
            [""],
            [""],
            [""],
            [""]
        ]

        estilo = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # background
            ("BACKGROUND", (0, 0), (0, 0), colors.darkgreen),
            ("BACKGROUND", (0, 1), (0, 1), colors.lightgreen),
            ("BACKGROUND", (0, 2), (0, 2), colors.white),  # para que haya espacio en blanco
            ("BACKGROUND", (0, 3), (0, 3), colors.lightgreen),

        ]

        tablaIzquierda = Table(data=elementos, style=estilo, colWidths=27, rowHeights=[50, 340, 5, 200])
        tabla = PositionedTable(tablaIzquierda, -60, -600)
        self.elementosDoc.append(tabla)


if __name__ == "__main__":
    factura = Factura()
    print("Factura creada")