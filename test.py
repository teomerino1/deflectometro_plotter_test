from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas

output_pdf = 'caratula.pdf'
c = canvas.Canvas(output_pdf, pagesize=A4)

# Agregar la primera figura en la posición deseada
# c.drawImage('figure_bar_l.png', 10, 0)
c.drawImage('INFAS.bmp', 220, 780, width=149, height=55)
# c.save()
c.drawImage('test.png', 30, 550, width=540, height=170)
c.drawImage('Cordoba.png', 235, 0, width=127, height=49)

c.save()