import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess
import os

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
    ### ENTER DRIVER WINDOW ###
    def enter_driver(self, widget):
        driver_window =  self.builder.get_object("driver_Window")
        driver_window.show()
    ### EXIT DRIVER WINDOW ###
    def close_driver(self, widget, event):
        return self.builder.get_object("driver_Window").hide_on_delete()
    
    ### Simple Entries
    
    ### APP WINDOW ###
    def enter_apps(self, widget):
        os.system("/etc/nobara/scripts/apps.sh")
    ### DOC WINDOW ###
    def enter_doc(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/")
    ### PROB WINDOW ###
    def enter_prob(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/upgrade-troubleshooting/")
    ### WEBSITE WINDOW ###
    def enter_website(self, widget):
        os.system("xdg-open https://nobaraproject.org/")
    
    
    
    ### LOOK ENTRIES ###
    
    ### DRIVER ENTRIES ###
    
    ### NVIDIA ###
    def enter_nvidia(self, widget):
        os.system("/etc/nobara/scripts/nvidia.sh")
    ### AMD PRO ###
    def enter_amd(self, widget):
        os.system("/usr/bin/nobara-amdgpu-config")
    ### ROCm ###
    def enter_rocm(self, widget):
        os.system("/etc/nobara/scripts/rocm.sh")
    
    
Application()
Gtk.main()
