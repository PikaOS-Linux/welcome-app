import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import subprocess
import os
import os.path
from pathlib import Path

import time
import threading

settings = Gio.Settings.new("org.nobara.welcome")

class Application:
    
    ### MAIN WINDOW ###
    def __init__(self):
        
        self.column_names = False
        self.drop_nan = False
        self.df = None
        application_id="org.nobara.welcome"
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/etc/nobara/scripts/nobara-welcome/nobara-welcome.ui")
        self.builder.connect_signals(self)
        win = self.builder.get_object("main_Window")
        win.connect("destroy", Gtk.main_quit)
        
        self.window = self.builder.get_object("main_Window")
        self.window.show()
        
        
        theme_box = self.builder.get_object("theme_box")
        layout_box = self.builder.get_object("layout_box")
        extension_box = self.builder.get_object("extension_box")
        
        desktop_output = subprocess.run(["echo $XDG_SESSION_DESKTOP | grep -i gnome"], shell=True)
        if (desktop_output.returncode) != 0:
            theme_box.hide()
            layout_box.hide()
            extension_box.hide()
        

        ### app state refresh ###
        
        global app_state_refresh
        app_state_refresh = True
        
        def app_state_refresh_func(): 
            while app_state_refresh == True:
                codec_install_button = self.builder.get_object("codec_install_button")
                codec_remove_button = self.builder.get_object("codec_remove_button")
                codec_output = subprocess.run(["/etc/nobara/scripts/nobara-welcome/rpm-check.sh | grep 1Affmpeg-libs1A "], shell=True, stdout=subprocess.DEVNULL)
                if (codec_output.returncode) == 0:
                    codec_install_button.set_sensitive(False)
                    codec_remove_button.set_sensitive(True)
                else:
                    codec_install_button.set_sensitive(True)
                    codec_remove_button.set_sensitive(False)        

                blender_install_button = self.builder.get_object("blender_install_button")
                blender_remove_button = self.builder.get_object("blender_remove_button")
                blender_output = subprocess.run(["/etc/nobara/scripts/nobara-welcome/rpm-check.sh | grep 1Ablender1A "], shell=True, stdout=subprocess.DEVNULL)
                if (blender_output.returncode) == 0:
                    blender_install_button.set_sensitive(False)
                    blender_remove_button.set_sensitive(True)
                else:
                    blender_install_button.set_sensitive(True)
                    blender_remove_button.set_sensitive(False)

                discord_install_button = self.builder.get_object("discord_install_button")
                discord_remove_button = self.builder.get_object("discord_remove_button")
                discord_output = subprocess.run(["/etc/nobara/scripts/nobara-welcome/rpm-check.sh | grep  1Adiscord1A "], shell=True, stdout=subprocess.DEVNULL)
                if (discord_output.returncode) == 0:
                    discord_install_button.set_sensitive(False)
                    discord_remove_button.set_sensitive(True)
                else:
                    discord_install_button.set_sensitive(True)
                    discord_remove_button.set_sensitive(False)


                kdenlive_install_button = self.builder.get_object("kdenlive_install_button")
                kdenlive_remove_button = self.builder.get_object("kdenlive_remove_button")
                kdenlive_output = subprocess.run(["/etc/nobara/scripts/nobara-welcome/rpm-check.sh | grep  1Akdenlive1A "], shell=True, stdout=subprocess.DEVNULL)
                if (kdenlive_output.returncode) == 0:
                    kdenlive_install_button.set_sensitive(False)
                    kdenlive_remove_button.set_sensitive(True)
                else:
                    kdenlive_install_button.set_sensitive(True)
                    kdenlive_remove_button.set_sensitive(False)
                    
                obs_install_button = self.builder.get_object("obs_install_button")
                obs_remove_button = self.builder.get_object("obs_remove_button")                
                obs_output = subprocess.run(["/etc/nobara/scripts/nobara-welcome/rpm-check.sh | grep  1Aobs-studio1A "], shell=True, stdout=subprocess.DEVNULL)
                if (obs_output.returncode) == 0:
                    obs_install_button.set_sensitive(False)
                    obs_remove_button.set_sensitive(True)
                else:
                    obs_install_button.set_sensitive(True)
                    obs_remove_button.set_sensitive(False)                
                time.sleep(10.0)
        
        t1 = threading.Thread(target=app_state_refresh_func)
        t1.start()
        
        def app_state_refresh_kill(self):
            global app_state_refresh
            app_state_refresh = False
        
        win.connect("destroy", app_state_refresh_kill)
        
    ### Start up Switch ###
        
        startup_switch = self.builder.get_object("startup_switch")
        
        startup_switch.set_active(settings.get_boolean("startup-show"))
    
        startup_switch.connect("toggled", lambda btn: settings.set_boolean("startup-show", btn.get_active()))
    
    ### ENTER LOOK WINDOW ###
    def enter_add_software(self, widget):
        install_window =  self.builder.get_object("install_Window")
        install_window.show()
    ### EXIT LOOK WINDOW ###
    def close_add_software(self, widget, event):
        return self.builder.get_object("install_Window").hide_on_delete()
    
    ##### FIRST STEPS ENTRIES #####
    
    #### DRIVER ENTRIES ####
    
    ### NVIDIA ###
    def enter_nvidia(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/nvidia.sh")
    ### AMD PRO ###
    def enter_amd(self, widget):
        os.system("/usr/bin/nobara-amdgpu-config")
    ### ROCm ###
    def enter_rocm(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/rocm.sh")
    ### XONE ###
    def enter_xone(self, widget):
        os.system("/usr/bin/nobara-controller-config")
   
    #### Apps Entries ####
   
    ### APPS ###
    def enter_apps(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/apps.sh")
    ### WEBAPPS ###
    def enter_webapps(self, widget):
        os.system("/usr/bin/webapp-manager")

    ##### QUICK SETUP ENTRIES #####
    
    ### LOGIN MANAGER ###
    def enter_dm(self, widget):
        os.system("/usr/bin/nobara-login-config")
    ### LAYOUTS ###
    def enter_layout(self, widget):
        os.system("/usr/bin/nobara-gnome-layouts")
    ### THEMES ###
    def enter_theme(self, widget):
        os.system("/usr/bin/gnome-tweaks")
    ### PLING ###
    def enter_pling(self, widget):
        os.system("xdg-open https://pling.com/")
    ### EXTENSION ###
    def enter_extension(self, widget):
        os.system("/usr/bin/extension-manager")

    #### TROUBLESHOOT ENTRIES ####
    
    ### Troubleshoot ###
    def enter_troubleshoot(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/upgrade-troubleshooting/")
    ### Docs ###
    def enter_doc(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/")
    ### Distro Sync ###
    def enter_distrosync(self, widget):
        os.system("/usr/bin/nobara-sync")


    #### COMMUNITY ENTRIES ####
    
    ### discord ###
    def enter_discord(self, widget):
        os.system("xdg-open https://discord.gg/6y3BdzC")
    ### reddit ###
    def enter_reddit(self, widget):
        os.system("xdg-open https://www.reddit.com/r/NobaraProject/")
        
    #### Contribute ENTRIES ####
    
    ### patreon ###
    def enter_patreon(self, widget):
        os.system("xdg-open https://www.patreon.com/gloriouseggroll")
    ### design ###
    def enter_design(self, widget):
        os.system("xdg-open https://discord.com/channels/110175050006577152/1015154123114549309")
    ### GE GITLAB ###
    def enter_ge_gitlab(self, widget):
        os.system("xdg-open https://gitlab.com/GloriousEggroll")
    ### GE GITHUB ###
    def enter_ge_github(self, widget):
        os.system("xdg-open https://github.com/GloriousEggroll")
    ### COSMO GITHUB ###
    def enter_cosmo_github(self, widget):
        os.system("xdg-open https://github.com/CosmicFusion")
    ###############################################################
    #### Install Window ####
    
    ### CODEC ###
    def enter_install_codec(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-welcome/xdg-terminal pkexec bash -c 'dnf install -y ffmpeg ffmpeg-libs.x86_64 ffmpeg-libs.i686'' "], shell=True)
    def enter_remove_codec(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-welcome/xdg-terminal 'pkexec dnf install -y ffmpeg ffmpeg-libs.x86_64 ffmpeg-libs.i686'"], shell=True)
        
    
    
    ### Blender ###
    def enter_install_blender(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    def enter_remove_blender(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    
    ### KDENLIVE ###
    def enter_install_kdenlive(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    def enter_remove_kdenlive(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    
    ### OBS STUDIO ###
    def enter_install_obs(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    def enter_remove_obs(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    
    ### DISCORD ###
    def enter_install_discord(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
    def enter_remove_discord(self, widget):
        subprocess.run(["/etc/nobara/scripts/nobara-layouts/settings-scripts/pop.sh disable"], shell=True)
        
Application()
Gtk.main()
