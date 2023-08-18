from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from matplotlib.backends.backend_pdf import FigureCanvasPdf
import io
import PyPDF2
from tabulate import tabulate
from tkinter import ttk
from fpdf import FPDF
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Image, Spacer,Paragraph
# Clase donde se inicializa y actualiza la tabla

class Table():
    def __init__(self, frame):
        self.table = None
        self.frame=frame
        self.show(frame)
        self.original_table_height = None
        self.grupos=None
        self.fecha=None
        self.ruta=None

    # Metodo que inserta valores en el diccionario
    # TODO -> Falta compensar los valores con respecto a la temperatura
    def insert(self, dict_r, dict_l):

        last_index_r = dict_r['Grupo'][len(dict_r['Grupo'])-1] # ultimo valor del array
        last_defl_mean_r = dict_r['Defl.'][len(dict_r['Defl.'])-1] # ultimo valor del array
        last_radio_mean_r = dict_r['Radio'][len(dict_r['Radio'])-1] # ultimo valor del array
        last_rd_r = dict_r['R*D'][len(dict_r['R*D'])-1] # ultimo valor del array
        last_r_d_r = dict_r['D/R'][len(dict_r['D/R'])-1] # ultimo valor del array

        last_index_l = dict_l['Grupo'][len(dict_l['Grupo'])-1] # ultimo valor del array
        last_defl_mean_l = dict_l['Defl.'][len(dict_l['Defl.'])-1] # ultimo valor del array
        last_radio_mean_l = dict_l['Radio'][len(dict_l['Radio'])-1] # ultimo valor del array
        last_rd_l = dict_l['R*D'][len(dict_l['R*D'])-1] # ultimo valor del array
        last_r_d_l = dict_l['D/R'][len(dict_l['D/R'])-1] # ultimo valor del array


        self.table.insert('', END, values = (
            last_index_r,
            last_radio_mean_r, 
            last_defl_mean_r,
            last_rd_r, 
            last_r_d_r, 
            # last_index_l,
            last_radio_mean_l,
            last_defl_mean_l, 
            last_rd_l, 
            last_r_d_l
            )) 

    def show(self,frame):
        columns = ("Grupos", "Radio.", "Defl.", "R*D.", "R/D.", ".Radio.", ".Defl.", ".R*D.", ".R/D.")

        # Crear el Treeview
        self.table = Treeview(self.frame, columns=columns, show='headings')
        self.table.grid(row=2, column=0, columnspan=2, pady=0)

        # Configurar el alto del Treeview
        self.table.configure(height=7)

        headers = [
            ("Grupos", "Grupos"),
            ("Radio.", "Radio"),
            ("Defl.", "Defl."),
            ("R*D.", "R*D"),
            ("R/D.", "D/R"),
            (".Radio.", "Radio"),
            (".Defl.", "Defl."),
            (".R*D.", "R*D"),
            (".R/D.", "D/R")
        ]
        for column, header in headers:
            self.table.heading(column, text=header)
            self.table.column(column, anchor=CENTER, width=110)

    def clear_table(self):
        # Elimina todos los elementos de la tabla
        self.table.delete(*self.table.get_children())

    def donwload_table(self):
        items = self.table.get_children()

        if items:  
            fecha= self.get_fecha().strftime("%d-%m-%Y")
            ruta=self.get_ruta()
            data = []

            for item in self.table.get_children():
                data.append(self.table.item(item, 'values'))

            headers = self.table['columns']
            table_str = tabulate(data, headers=headers, tablefmt='plain')

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.set_auto_page_break(auto=True, margin=15)
                    # Agregar el texto "Fecha" y la fecha actual al PDF
            pdf.set_x((pdf.w - pdf.get_string_width("Fecha: " + fecha)) / 2)
            pdf.cell(0, 10, "Fecha: " + fecha, ln=True)

            
            pdf.set_x((pdf.w - pdf.get_string_width("Ruta: " + ruta)) / 2)
            pdf.cell(0, 10, "Ruta: " + ruta, ln=True)
    
            pdf.ln(3)  # Add some spacing between tables
            
            first_table_data = [["Huella Externa (DER)", "Huella Interna (IZQ)"]]
            col_width_first = 88
            row_height_first = 10
            left_margin = 22  # Margin in points

            for row in first_table_data:
                pdf.cell(left_margin)  # Add left margin
                for item in row:
                    pdf.cell(col_width_first, row_height_first, txt=item, border=1, align='C')
                pdf.ln(row_height_first)

           
            col_width = 22
            row_height = 6
            for row in table_str.split('\n'):
                for item in row.split(None):
                    pdf.cell(col_width, row_height, txt=item, border=1, align='C')
                pdf.ln(row_height)

            pdf.output('tabla.pdf')
            
        else:
            print("No hay nada")
            return
        
    def reset(self):
        self.clear_table()
        self.show(self)

    def set_fecha(self,fecha):
        self.fecha=fecha

    def get_fecha(self):
        return self.fecha
    
    def set_ruta(self,ruta):
        self.ruta=ruta

    def get_ruta(self):
        return self.ruta
