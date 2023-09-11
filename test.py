from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

# Datos de ejemplo
datos = [["Dato " + str(i) for i in range(9)] for _ in range(100)]  # Cambia esto con tus datos reales

# Definir el estilo de la tabla
table_style = [
    ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
    ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)),
    ('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0)),
]

# Crear un buffer de bytes para almacenar el PDF
buffer = BytesIO()

# Crear un objeto canvas
c = canvas.Canvas(buffer, pagesize=A4)

# Altura máxima de la página
altura_maxima = 720  # Ajusta según tus necesidades

# Número de filas por página
num_filas_por_pagina = 33

# Variable para rastrear la página actual
pagina_actual = 1

# Variable para rastrear la posición vertical
y = 720  # Empieza desde la parte superior de la página A4

while datos:
    # Extraer datos para la página actual
    datos_pagina_actual = datos[:num_filas_por_pagina]
    datos = datos[num_filas_por_pagina:]

    # Crear la tabla
    tabla = c.beginText(50, y)
    tabla.setFont("Helvetica-Bold", 12)

    # Agregar encabezado de tabla
    for encabezado in datos_pagina_actual[0]:
        tabla.textLine(encabezado)

    # Agregar filas de datos
    for fila in datos_pagina_actual[1:]:
        for dato in fila:
            tabla.textOut(dato + " " * (10 - len(dato)))
        tabla.textLine("")

    # Aplicar estilo a la tabla
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.rect(50, y, 450, -18 * len(datos_pagina_actual[1:]), fill=True)
    c.setFillColorRGB(0, 0, 0)

    # Agregar la tabla al canvas
    c.drawText(tabla)

    # Verificar si se necesita una nueva página
    y -= 18 * len(datos_pagina_actual[1:])
    if y < 50:
        c.showPage()
        y = altura_maxima

    pagina_actual += 1

# Guardar el contenido del buffer en un archivo PDF
c.save()

# Guardar el contenido del buffer en un archivo PDF
buffer.seek(0)
with open('test.pdf', 'wb') as f:
    f.write(buffer.read())
