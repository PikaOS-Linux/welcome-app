import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Application:
    
    ### MAIN WINDOW ###
    def __init__(self):
        self.column_names = False
        self.drop_nan = False
        self.df = None
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("nobara-welcome.glade")
        self.builder.connect_signals(self)
        win = self.builder.get_object("main_Window")
        win.connect("destroy", Gtk.main_quit)
        
        self.window = self.builder.get_object("main_Window")
        self.window.show()
    ### ENTER LOOK WINDOW ###
    def enter_look(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ### EXIT LOOK WINDOW ###
    def close_look(self, widget, event):
        return self.builder.get_object("look_Window").hide_on_delete()
    ### DRIVER WINDOW ###
    def enter_driver(self, widget):
        driver_window =  self.builder.get_object("driver_Window")
        driver_window.show()
    ### APP WINDOW ###
    def enter_apps(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ### DOC WINDOW ###
    def enter_doc(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ### PROB WINDOW ###
    def enter_prob(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ### WEBSITE WINDOW ###
    def enter_website(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ###
    
    
    
    
Application()
Gtk.main()
