from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
import datetime
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from io import BytesIO

# Crear un buffer para el PDF
# Crear un objeto Canvas
c = canvas.Canvas("mi_archivo.pdf")

# Agregar contenido a la primera página
c.drawString(100, 750, "Página 1")

# Mostrar la primera página y prepararse para la siguiente página
c.showPage()

# Agregar contenido a la segunda página
c.drawString(100, 750, "Página 2")

# Mostrar la segunda página y prepararse para la siguiente página
c.showPage()

# Agregar contenido a la tercera página
c.drawString(100, 750, "Página 3")

# Mostrar la tercera página y prepararse para la siguiente página
c.showPage()

# Cerrar el objeto Canvas para finalizar el PDF
c.save()




