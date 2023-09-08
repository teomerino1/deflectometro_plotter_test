from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
import datetime
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from io import BytesIO

# Crear un buffer para el PDF
# buffer = BytesIO()

# Crear un objeto Canvas
# Crear un nuevo PDF con ambas figuras
output_pdf = 'defl_individuales.pdf'
c = canvas.Canvas(output_pdf, pagesize=A4)
# Dibuja la imagen de encabezado
c.drawImage('header2.png', 25, 773, width=575, height=60)

c.drawImage('image.png', 0, 0, width=600, height=100)
# Agregar la primera figura en la posición deseada
# c.drawImage('figure_bar_l.png', 10, 0)
c.drawImage('figure_bar_l.png', 100, 200, width=383, height=230)
# Agregar la segunda figura debajo de la primera
c.drawImage('figure_bar_r.png', 100, 500,width=383, height=230)
# Guardar el contenido en el PDF
c.save()




