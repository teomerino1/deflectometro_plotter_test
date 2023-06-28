from tkinter import *
from tkinter.ttk import Label, Frame, Button, Scrollbar
import view
import table
import graphs

# Clase correspondiente a la vista encargada de mostrar los datos y graficos

class Plot():
    def __init__(self,root,plot_callback):

        self.root = root
        self.main_plot_frame = None
        self.second_plot_frame = None
        self.plot_callback = plot_callback

        self.Table = None
        self.Graphs = None

    # Metodo que elimina todo lo que muestra la pagina
    def close(self):
        self.second_plot_frame.destroy()

    def show(self):

        second_plot_frame = Frame(self.root)
        second_plot_frame.grid(ipadx=3, ipady=5)
        self.second_plot_frame = second_plot_frame

        title = Label(second_plot_frame, text="Plantilla general de resultados estadisticos",font=(None, 40))
        title.grid(row = 0, column = 0,columnspan = 3)

        # self.scrollbar()

        Label(second_plot_frame, text= "Temperatura: %s"%(view.temp)).grid(column=0, row=1)
        Label(second_plot_frame, text="Grupos: %s"%(view.muestras)).grid(column=1, row=1)
        Label(second_plot_frame, text="Cantidad de muestras: %s"%(view.grupos)).grid(column=2, row=1)

        self.Table = table.Table(self.second_plot_frame) # instancia de tabla
        self.Graphs = graphs.Graphs(self.second_plot_frame) # instancia de tabla

        Button(second_plot_frame, text="Atras", command=self.plot_callback).grid(column=0, row=2)

    # Metodo que recibe los datos nuevos y manda a actualizar estructuras y plots
    def new_group_data_plot(self,dict_r, dict_l):
        self.Table.insert(dict_r, dict_l)
        self.Graphs.update_gmean(dict_r, dict_l)
        # self.update_data(dict_r, dict_l)
    
    def update_bar_plot(self, hist_dict):
        self.Graphs.update_bar(hist_dict)

    def scrollbar(self):
        # TODO -> SCROLL (funciona mal, no se ve y solo anda con la ruedita si pones el mouse en la esquina inferior derecha)
        main_plot_frame = Frame(self.root)
        main_plot_frame.pack(fill=BOTH, expand=1)

        canvas = Canvas(main_plot_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Scrollbar 
        scrollbar = Scrollbar(self.main_plot_frame, orient = VERTICAL, command=canvas.yview)
        # scrollbar.grid(column=1, row=0, sticky='NS')
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        second_plot_frame = Frame(canvas)

        canvas.create_window((0,0), window=second_plot_frame, anchor="nw")
        return