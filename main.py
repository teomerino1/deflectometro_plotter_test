import view
import tkinter as tk
from tkinter import ttk
import data
import reporter
from threading import Thread
import threading
from ttkthemes import ThemedTk
from tkinter import *
from time import sleep



"""
La clase main instancia los objetos que se utilizan en la ejecución
El hilo main queda ejecutando la interfaz principal 'root' mientras
que todo el resto sucede en las otras clases
"""
def main():
    
    root=ThemedTk(theme='radiance')
    root.set_theme_advanced('radiance',hue=0.1)
    Reporter = reporter.Reporter()
    Data = data.Data()
    View = view.View(root,Data,Reporter)
    root.mainloop()

if __name__ == "__main__":
    main()