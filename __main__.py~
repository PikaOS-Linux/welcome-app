import gi
import pandas as pd
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg
import  matplotlib.pyplot as plt

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Application:
    def __init__(self):
        self.column_names = False
        self.drop_nan = False
        self.df = None
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("nobara-welcome.glade")
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object("main_Window")
        self.window.show_all()
