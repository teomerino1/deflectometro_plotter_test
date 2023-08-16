import tkinter as tk
from tkinter import *
from tkinter.ttk import Scrollbar
import threading
from threading import Thread
from tkinter.ttk import Style
from ttkthemes import ThemedTk
import config
import plot
import plot_2
import plot_3
import plot_4
import plot_5
import queue
import time
import PyPDF2
import os
from time import sleep
import datetime
from reportlab.lib.pagesizes import letter, landscape,A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
from tkinter import messagebox

class View():
    def __init__(self, root,data_instance,reporter_instance):

        self.root=root
        self.temp = None
        self.grupos = None
        self.muestras = None
        self.espesor = None
        self.ft_ntry = None
        self.fh_ntry = None
        self.fc_ntry = None
        self.z_ntry = None
        self.ruta_ntry=None
        self.provincia_ntry=None
        self.tramo_ntry=None
        self.subtramo_ntry=None
        self.pavimento_ntry=None
        self.operador_ntry=None
        self.chofer_ntry=None
        self.apoyo_ntry=None
        self.data_instance = data_instance
        self.reporter_instance = reporter_instance
        self.data_ready=0
        self.reset=None
        
        #Se crean los objetos Plot y Config como atributos de view 
        self.Config = config.Config(self.root,self)
        self.Plot = plot.Plot(self.root, self)
        self.Plot2 = plot_2.Plot2(self.root,self)
        self.Plot3 = plot_3.Plot3(self.root,self)
        self.Plot4 =plot_4.Plot4(self.root,self)
        self.Plot5= plot_5.Plot5(self.root,self)
        self.is_plotting = False
        self.first_time_plot=True
        self.first_time_plot2=True
         # Crear una cola bloqueante para las funciones de transición de interfaz
        self.interface_transition_queue = queue.Queue()
        # Crear un solo hilo para ejecutar las funciones de transición de interfaz
        self.interface_transition_thread = threading.Thread(target=self.interface_transition_function)
        self.interface_transition_thread.start()
        self.start(root)

        # self.Plot.show()

     # Metodo que inicializa la view:
    def start(self,root):

        self.root.title('Deflectómetro')
        self.root.tk.call("source", "azure.tcl")
        self.root.tk.call("set_theme", "light")
        style = Style(root)
        self.root.attributes('-zoomed', True) 
        
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        # self.root.attributes('-fullscreen',True)
        # self.root.geometry(f"{screen_width}x{screen_height}")

        ###############################################

        self.Config.show(0)
        self.Config.show(1)
        self.Plot.show(0)
        self.Plot2.show(0)
        self.Plot3.show(0)
        self.Plot4.show(0)
        self.Plot5.show(0)


     # Metodo que borra el frame Config y abre el Plot1
    def go_to_plot1_from_config(self):
        self.Config.close()
        self.Plot.show(1)
       
    # Metodo que borra el Plot 1 y abre el de Config
    def go_to_config(self):
        self.Plot.close()
        self.Config.show(1)

    # # Metodo que borra el Plot 1 y abre el Plot 2
    def go_to_plot_2_from_plot_1(self):

        if(self.first_time_plot2):
            self.first_time_plot2=False
            self.Plot.close()
            self.Plot2.show(1)

        else:
            self.Plot.close()
            self.Plot2.show(1)

    # Metodo que borra el Plot 2 y abre el Plot 1
    def go_to_plot_1_from_plot_2(self):
        self.Plot2.close()
        self.Plot.show(1) 

    def go_to_plot_3_from_plot2(self):
        self.Plot2.close()
        self.Plot3.show(1)

    def go_to_plot_2_from_plot_3(self):
        self.Plot3.close()
        self.Plot2.show(1)

    def go_to_plot_4_from_plot_3(self):
        self.Plot3.close()
        self.Plot4.show(1)

    def go_to_plot_3_from_plot_4(self):
        self.Plot4.close()
        self.Plot3.show(1)

    def go_to_plot_5_from_plot_4(self):
        self.Plot4.close()
        self.Plot5.show(1)

    def go_to_plot_4_from_plot_5(self):
        self.Plot5.close()
        self.Plot4.show(1)

    def reset_all_plots(self):
        self.Plot.reset_table()
        self.Plot.reset()
        self.Plot2.reset()
        self.Plot3.reset()
        self.Plot4.reset()
        self.Plot5.reset()
        
    def reset_all_data(self):
        self.data_instance.reset_all()
        self.reporter_instance.reset_reporter()
        self.temp=None
        self.grupos=None
        self.muestras=None
        self.espesor=None
        self.ft=None
        self.fh=None
        self.fc=None
        self.z=None
        self.set_data_ready(value=0)

    def set_reset(self,value):
        self.reset=value

    def get_reset(self):
        return self.reset

    def download_pdf(self):
        # self.generar_carátula("caratula.pdf")
        self.Plot.generar_pdf()
        # self.Plot2.download_graphs()
        # self.Plot3.download_graphs()
        # self.Plot4.download_graphs()
        # self.Plot5.download_stats()
        # sleep(1)
        # self.combine_pdf()

    def generar_carátula(self,filename):
        informe = "INFORME DEFLECTOMETRO LACROIX"
        cosas = "DEFLEXIONES, VALORES MEDIOS, CARACTERISTICOS, RADIOS DE CURVATURA Y ANALISIS ESTADISTICO"
        ruta = self.get_ruta()
        provincia = self.get_provincia()
        tramo = self.get_tramo()
        subtramo = self.get_subtramo()
        pavimento = self.get_pavimento()
        
        # prog_max = self.Plot.get_prog_max()
        prog_max=3000
        fecha = datetime.datetime.now()
        chofer = self.get_chofer()
        apoyo = self.get_apoyo()
        operador = self.get_operador()

        doc = SimpleDocTemplate(filename, pagesize=A4)

        styles = getSampleStyleSheet()
        center_style = ParagraphStyle(name='CenterStyle', alignment=1)

        story = []

        # Modificar los tamaños de fuente en los estilos
        styles['Title'].fontSize = 30
        styles['Heading2'].fontSize = 20

        # Agregar el título y subtítulo con espacio en blanco
        title = Paragraph(informe, styles['Title'])
        subtitle = Paragraph(cosas, styles['Heading2'])
        title_subtitle_table = Table([[title], [Spacer(1, 20)], [subtitle]])
        title_subtitle_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (0, 2), 'MIDDLE'),
            ('ALIGN', (0, 0), (0, 2), 'CENTER'),
            ('TEXTCOLOR', (0, 0), (0, 2), colors.black),
            ('FONTNAME', (0, 0), (0, 2), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (0, 0), 10),
            ('BOTTOMPADDING', (0, 1), (0, 1), 30),  # Agregar espacio en blanco
            ('BOTTOMPADDING', (0, 2), (0, 2), 0),
            ('ALIGN', (0, 2), (0, 2), 'CENTER')  # Centrar el subtítulo
        ]))

        story.append(title_subtitle_table)
        story.append(Spacer(1, 50))  # Espacio en blanco

        # Agregar el resto de la información centrada
        centered_info_paragraphs = [
            Paragraph(f"Ruta: {ruta}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Provincia: {provincia}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Tramo: {tramo}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Subtramo: {subtramo}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Pavimento: {pavimento}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Progresiva Inicial: 0", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Progresiva Final: {prog_max}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=20)),
            Spacer(1, 150),
        ]
        story.extend(centered_info_paragraphs)

        down_info_paragraphs=[
            Paragraph(f"Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=15)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Chofer: {chofer}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=15)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Apoyo: {apoyo}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=15)),
            Spacer(1, 20),  # Agregar un espacio en blanco
            Paragraph(f"Operador: {operador}", ParagraphStyle(name='CenterStyle', alignment=1, fontSize=15)),
        ]

        story.extend(down_info_paragraphs
                     )
        doc.build(story)

    def combine_pdf(self):

        output1="pdf2.pdf"
        output2="pdf3.pdf"
        # image_path = 'figure_defl_mean_l.png'
        image_path='figure_rad_l.png'
        if os.path.exists(image_path): 

            self.generar_carátula("informe.pdf")
            c = canvas.Canvas(output1, pagesize=A4)
            c.drawImage('figure_defl_mean_l.png',10, 0)
            c.drawImage('figure_rad_l.png', 10,500)
            c.save()

            c = canvas.Canvas(output2, pagesize=A4)
            c.drawImage('figure_defl_mean_r.png', 10, 0)
            c.drawImage('figure_rad_r.png', 10, 500)
            c.save()

            pdf_files = [
                "informe.pdf",
                "tabla.pdf",    
                "defl_individuales.pdf",
                "pdf2.pdf",
                "pdf3.pdf",
                "radios.pdf",
                "pdf5.pdf"
            ]
            output_filename = "results.pdf"

            pdf_merger = PyPDF2.PdfMerger()
            
            # Combining PDFs
            for pdf_file in pdf_files:
                pdf_merger.append(pdf_file)
            
            # Writing the merged PDF to the output file
            with open(output_filename, "wb") as output_pdf:
                pdf_merger.write(output_pdf)
            
            # Closing the merger
            pdf_merger.close()
            
            # Deleting input PDFs
            for pdf_file in pdf_files:
                os.remove(pdf_file)

            os.remove('figure_defl_mean_l.png')
            os.remove('figure_defl_mean_r.png')
            os.remove('figure_rad_r.png')
            os.remove('figure_rad_l.png')

            messagebox.showinfo("Aviso","PDF generado en Desktop:")

        else:
            print("Detecto que la imagen no existe")
            return


# Metodo que obtiene los datos nuevos y debe mandar a actualizar los ploteos y las estructuras
    def new_group_data_view(self, dict_r, dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos):
        self.Plot.new_group_data_plot(dict_r, dict_l)
        self.Plot2.new_group_data_plot2(dict_r,dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos)
        self.Plot3.new_group_data_plot3(dict_r,dict_l, defl_r_car, defl_l_car, defl_r_max, defl_l_max,grupos)
        self.Plot4.new_group_data_plot4(dict_r, dict_l,grupos)

    # Metodo que manda a actualizar el gafico de barras 
    def update_bar_view(self, defl_r,defl_l):
        self.Plot.update_bar_plot(defl_r,defl_l)

    def show_stats_in_plot(self,media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad):
        self.Plot5.grid_stats(media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad)

    def get_config(self):
        return self.Config.get_config()

    def get_params(self):
        return self.Config.get_params()
    
    def on_plot(self):
        return self.is_plotting
    
    def obtain_values(self):
       return self.temp, self.grupos, self.muestras, self.espesor, self.ft_ntry, self.fh_ntry, self.fc_ntry, self.z_ntry

    def set_temp(self,temp):
        self.data_instance.set_temp(temp)
        self.temp=temp

    def get_temp(self):
        return self.temp

    def set_grupos(self,grupos):
        self.grupos=grupos
        self.data_instance.set_grupos(grupos)
        
    def get_grupos(self):
        return self.grupos

    def set_muestras(self,muestras):
        self.muestras=muestras

    def get_muestras(self):
        return self.muestras

    def set_espesor(self,espesor):
        self.data_instance.set_espesor(espesor)
        self.espesor=espesor

    def get_espesor(self):
        return self.espesor

    def set_ft(self,ft):
        self.data_instance.set_ft(ft)
        self.ft_ntry=ft

    def get_ft(self):
        return self.ft_ntry

    def set_fh(self,fh):
        self.data_instance.set_fh(fh)
        self.fh_ntry=fh

    def get_fh(self):
        return self.fh_ntry

    def set_fc(self,fc):
        self.data_instance.set_fc(fc)
        self.fc_ntry=fc

    def get_fc(self):
        return self.fc_ntry
    
    def set_z(self,z):
        self.data_instance.set_z(z)
        self.z_ntry=z 

    def get_z(self):
        return self.z_ntry
    
    def set_data_ready(self,value):
        self.data_ready=value

    def get_data_ready(self):
        return self.data_ready
    
    def set_ruta(self,ruta):
        self.ruta_ntry=ruta

    def get_ruta(self):
        return self.ruta_ntry
    
    def set_provincia(self,provincia):
        self.provincia_ntry=provincia

    def get_provincia(self):
        return self.provincia_ntry
    
    def set_tramo(self,tramo):
        self.tramo_ntry=tramo

    def get_tramo(self):
        return self.tramo_ntry
    
    def set_subtramo(self,subtramo):
        self.subtramo_ntry=subtramo

    def get_subtramo(self):
        return self.subtramo_ntry
    
    def set_pavimento(self,pavimento):
        self.pavimento_ntry=pavimento

    def get_pavimento(self):
        return self.pavimento_ntry
    
    def set_chofer(self,chofer):
        self.chofer_ntry=chofer

    def get_chofer(self):
        return self.chofer_ntry
    
    def set_operador(self,operador):
        self.operador_ntry=operador

    def get_operador(self):
        return self.operador_ntry
    
    def set_apoyo(self,apoyo):
        self.apoyo_ntry=apoyo

    def get_apoyo(self):
        return self.apoyo_ntry

    
    def interface_transition_function(self):
            while True:
                # Utilizar una cola bloqueante para esperar a que se solicite una función de transición
                target_function = self.interface_transition_queue.get()

                # Ejecutar la función de transición de interfaz correspondiente
                if target_function == 'go_to_config':
                    self.go_to_config()

                if target_function == 'go_to_plot_1_from_config':
                    if(self.get_data_ready()==1):
                        messagebox.showwarning("Aviso","Debe resetear los datos antes de intentar modificarlos")
                        continue
                    self.go_to_plot1_from_config()

                elif target_function == 'go_to_plot_2_from_plot_1':
                    self.go_to_plot_2_from_plot_1()
                
                elif target_function == 'go_to_plot_1_from_plot_2':
                    self.go_to_plot_1_from_plot_2()

                elif target_function == 'go_to_plot_3_from_plot_2':
                    self.go_to_plot_3_from_plot2()

                # Agregar más casos para otras funciones de transición...
                elif target_function == 'go_to_plot_2_from_plot_3':
                    self.go_to_plot_2_from_plot_3()

                elif target_function == 'go_to_plot_4_from_plot_3':
                    self.go_to_plot_4_from_plot_3()

                elif target_function == 'go_to_plot_3_from_plot_4':
                    self.go_to_plot_3_from_plot_4()

                elif target_function == 'go_to_plot_5_from_plot_4':
                    self.go_to_plot_5_from_plot_4()

                elif target_function == 'go_to_plot_4_from_plot_5':
                    self.go_to_plot_4_from_plot_5()

                elif target_function == 'reset_all_plots':
                    self.reset_all_plots()
                    self.reset_all_data()
                    # self.set_reset(1)
                    messagebox.showinfo("Aviso", "Datos reseteados!")

                elif target_function == 'generate_stats':
                    media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,defl_car_der,defl_car_izq,rad_car_der,rad_car_izq, d_r_der,d_r_izq ,d_x_r_der, d_x_r_izq, total_mediciones_defl, total_mediciones_rad =self.data_instance.calculate_stats()
                    if(media_defl_r==0):
                        print("No hago naranja")
                        continue
                    self.show_stats_in_plot(
                        media_defl_r, media_defl_izq,media_rad_der, media_rad_izq,
                        desv_defl_der, desv_defl_l,coef_var_der,coef_var_izq,
                        defl_car_der,defl_car_izq ,rad_car_der, rad_car_izq,
                        d_r_der,d_r_izq,
                        d_x_r_der, d_x_r_izq, 
                        total_mediciones_defl, total_mediciones_rad
                    )
                    # self.set_data_ready(value=0)
                    # self.reset_all_data()
                elif target_function=='download_pdf':
                    # pdf_thread = Thread(target=download_pdf)
                    # pdf_thread.daemon=True
                    # pdf_thread.start()
                    self.download_pdf()

                # Indicar que la función se ha procesado y la cola puede esperar nuevamente
                self.interface_transition_queue.task_done()

                # # Pequeño descanso entre actualizaciones de la interfaz para no sobrecargar la CPU
                # time.sleep()  # Ajusta el tiempo de sleep según tus necesidades


    def enqueue_transition(self, function_name):
        self.interface_transition_queue.put(function_name)














     
    