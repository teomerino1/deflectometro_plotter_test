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
# Clase donde se inicializa y actualiza la tabla

class Table():
    def __init__(self, frame):
        self.table = None
        self.frame=frame
        self.show(frame)
        self.original_table_height = None
        self.grupos=None
          

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
        columns = ("Grupos", "Radio_Der.", "Defl_Der.", "R*D_Der.", "R/D_Der.", "Radio_Izq.", "Defl_Izq.", "R*D_Izq.", "R/D_Izq.")

# Crear el marco adicional para los encabezados
        header_frame = Frame(self.frame)
        header_frame.grid(row=0, column=1, columnspan=10, pady=10)

        # Agregar etiquetas para los encabezados "DERECHA" e "IZQUIERDA"
        label_der = Label(header_frame, text="Huella Externa (DER)", font=("Helvetica", 25, "bold"))
        label_der.grid(row=0, column=0,padx=110, pady=0, sticky=NW)

        label_izq = Label(header_frame, text="Huella Interna (IZQ)", font=("Helvetica", 25, "bold"))
        label_izq.grid(row=0, column=1,pady=0, sticky=N)

        # Crear el Treeview
        self.table = Treeview(self.frame, columns=columns, show='headings')
        self.table.grid(row=1, column=1, columnspan=2, pady=0)

        # Configurar el alto del Treeview
        self.table.configure(height=7)

        headers = [
            ("Grupos", "Grupos"),
            ("Radio_Der.", "Radio"),
            ("Defl_Der.", "Defl."),
            ("R*D_Der.", "R*D"),
            ("R/D_Der.", "D/R"),
            ("Radio_Izq.", "Radio"),
            ("Defl_Izq.", "Defl."),
            ("R*D_Izq.", "R*D"),
            ("R/D_Izq.", "D/R")
        ]
        for column, header in headers:
            self.table.heading(column, text=header)
            self.table.column(column, anchor=CENTER, width=110)

        # columns = ("Grupos_r", "Radio_r", "Defl_r", "R*D_r", "R/D_r","Grupos_L", "Radio_L", "Defl_L", "R*D_L", "R/D_L")
        # # columns = ("Grupos_r", "Radio_r", "Defl_r", "R*D_r", "R/D_r", "Radio_L", "Defl_L", "R*D_L", "R/D_L")
        
        # # Crear el Treeview
        # self.table = Treeview(self.frame, columns=columns, show='headings')
        # # self.table.grid(row=1, column=0, columnspan=3)
        # self.table.grid(row=1, column=1,columnspan=2,pady=30)
        # # Configurar el alto del Treeview
        # self.table.configure(height=7)
       
        # # Crear el Scrollbar
        # # scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.table.yview)
        # # scrollbar.grid(row=1, column=3, sticky="ns")
        # # self.table.configure(yscrollcommand=scrollbar.set)
        
        # # headers = [
        # #     ("Grupos_r", "Grupos"),
        # #     ("Radio_r", "Radio Derecha"),
        # #     ("Defl_r", "Defl. Derecha"),
        # #     ("R*D_r", "R*D Derecha"),
        # #     ("R/D_r", "D/R Derecha"),
        # #     ("Radio_L", "Radio Izquierda"),
        # #     ("Defl_L", "Defl. Izquierda"),
        # #     ("R*D_L", "R*D Izquierda"),
        # #     ("R/D_L", "D/R Izquierda")
        # # ]
        
        # # Configurar encabezados y columnas del Treeview
        # headers = [
        #     ("Grupos_r", "Groups R"),
        #     ("Radio_r", "Radio"),
        #     ("Defl_r", "Defl."),
        #     ("R*D_r", "R*D"),
        #     ("R/D_r", "D/R"),
        #     ("Grupos_L", "Groups L"),
        #     ("Radio_L", "Radio"),
        #     ("Defl_L", "Defl."),
        #     ("R*D_L", "R*D"),
        #     ("R/D_L", "D/R")
        # ]
        # for column, header in headers:
        #     self.table.heading(column, text=header)
        #     self.table.column(column, anchor=CENTER, width=100)

    def clear_table(self):
        # Elimina todos los elementos de la tabla
        self.table.delete(*self.table.get_children())

    def donwload_table(self):
        # Obtener los datos del Treeview
        # items = self.table.get_children()
        # if items:  # Si hay al menos un elemento
            print("La tabla tiene elementos.")
            data = []
        
            for item in self.table.get_children():
                data.append(self.table.item(item, 'values'))
            # Obtener los encabezados del Treeview
            headers = self.table['columns']
            # Convertir los datos en una tabla con formato usando tabulate
            table_str = tabulate(data, headers=headers, tablefmt='plain')
            # Generar PDF con la tabla
            pdf = FPDF()
            pdf.add_page()
            # Definir el tamaño y la fuente del texto en el PDF
            pdf.set_font("Arial", size=12)
            # Ajustar el interlineado
            pdf.set_auto_page_break(auto=True, margin=15)
            # Crear la tabla en el PDF
            col_width = 22
            row_height = 6
            for row in table_str.split('\n'):
                for item in row.split(None):
                    pdf.cell(col_width, row_height, txt=item, border=1, align='C')
                pdf.ln(row_height)
            # Guardar el PDF en un archivo
            pdf.output('tabla.pdf')
            
        # else:
        #     print("No hay nada")
        #     return
        
    def reset(self):
        # Agrega aquí cualquier otra lógica específica para reiniciar la tabla
        # Si tienes algún estado inicial para la tabla, puedes restaurarlo aquí
        self.clear_table()
        # Agrega aquí cualquier otro proceso que necesites realizar para reiniciar la tabla
        self.show(self)

