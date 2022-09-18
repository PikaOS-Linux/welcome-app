import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Switch(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        switch = Gtk.Switch()
        switch.connect("notify::active", self.on_switch_toggled)
        switch.set_active(self)
        self.add(switch)

    def on_switch_toggled(self, switch, state):
        if switch.get_active():
            print("Switch toggled to on")
        else:
            print("Switch toggled to off")

window = Switch()
window.show_all()

Gtk.main()
