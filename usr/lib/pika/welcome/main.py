import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import subprocess
import os
import os.path
from pathlib import Path

import time
import threading
import subprocess

settings = Gio.Settings.new("org.pika.welcome")

proc1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
proc2 = subprocess.Popen(['grep', '/usr/lib/pika/welcome/main.py'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc3 = subprocess.Popen(['grep', '-v', 'grep'], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc4 = subprocess.Popen(['wc', '-l'], stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
result = proc4.stdout.read()
print(int(result))
if int(result) > 1:
    quit()

class Application:
    
    ### MAIN WINDOW ###
    def __init__(self):
        
        self.column_names = False
        self.drop_nan = False
        self.df = None
        application_id="org.pika.welcome"
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/lib/pika/welcome/main.ui")
        self.builder.connect_signals(self)
        win = self.builder.get_object("main_Window")
        win.connect("destroy", Gtk.main_quit)
        
        self.window = self.builder.get_object("main_Window")
        self.window.show()
        
        
        theme_box = self.builder.get_object("theme_box")
        layout_box = self.builder.get_object("layout_box")
        extension_box = self.builder.get_object("extension_box")
        
        desktop_output = subprocess.run(["echo $XDG_SESSION_DESKTOP | grep -i ubuntu"], shell=True)
        if (desktop_output.returncode) != 0:
            theme_box.hide()
            layout_box.hide()
            extension_box.hide()
            self.builder.get_object("layout_button_2").hide()
            self.builder.get_object("layout_text_2").hide()
            
            
        ### Hidden Entries ###
        self.builder.get_object("dm_box").hide()
        
        
        self.main_Sidebar = self.builder.get_object("main_Sidebar")
        

        ### app state refresh ###
        global app_state_refresh
        app_state_refresh = True
        global window_state_refresh
        window_state_refresh = True

        
        
        def app_state_refresh_func(): 
            blender_install_button = self.builder.get_object("blender_install_button")
            blender_remove_button = self.builder.get_object("blender_remove_button")
#            discord_install_button = self.builder.get_object("discord_install_button")
#            discord_remove_button = self.builder.get_object("discord_remove_button")
            kdenlive_install_button = self.builder.get_object("kdenlive_install_button")
            kdenlive_remove_button = self.builder.get_object("kdenlive_remove_button")
            obs_install_button = self.builder.get_object("obs_install_button")
            obs_remove_button = self.builder.get_object("obs_remove_button")
            gameutils_install_button = self.builder.get_object("gameutils_install_button")
            gameutils_remove_button = self.builder.get_object("gameutils_remove_button")
            msttf_install_button = self.builder.get_object("msttf_install_button")
            msttf_remove_button = self.builder.get_object("msttf_remove_button")
            krita_install_button = self.builder.get_object("krita_install_button")
            krita_remove_button = self.builder.get_object("krita_remove_button")
            libreoffice_install_button = self.builder.get_object("libreoffice_install_button")
            libreoffice_remove_button = self.builder.get_object("libreoffice_remove_button")
            gameextra_install_button = self.builder.get_object("gameextra_install_button")
            gameextra_remove_button = self.builder.get_object("gameextra_remove_button")
            fabiscafe_install_button = self.builder.get_object("fabiscafe_install_button")
            fabiscafe_remove_button = self.builder.get_object("fabiscafe_remove_button")
            
            while app_state_refresh == True:
                blender_output = subprocess.run(["dpkg -s blender"], shell=True, stdout=subprocess.DEVNULL)
                if (blender_output.returncode) == 0:
                    blender_install_button.set_sensitive(False)
                    blender_remove_button.set_sensitive(True)
                else:
                    blender_install_button.set_sensitive(True)
                    blender_remove_button.set_sensitive(False)
#                discord_output = subprocess.run(["dpkg -s discord"], shell=True, stdout=subprocess.DEVNULL)
#                if (discord_output.returncode) == 0:
#                    discord_install_button.set_sensitive(False)
#                    discord_remove_button.set_sensitive(True)
#                else:
#                    discord_install_button.set_sensitive(True)
#                    discord_remove_button.set_sensitive(False)
                kdenlive_output = subprocess.run(["dpkg -s kdenlive"], shell=True, stdout=subprocess.DEVNULL)
                if (kdenlive_output.returncode) == 0:
                    kdenlive_install_button.set_sensitive(False)
                    kdenlive_remove_button.set_sensitive(True)
                else:
                    kdenlive_install_button.set_sensitive(True)
                    kdenlive_remove_button.set_sensitive(False)
                obs_output = subprocess.run(["dpkg -s obs-studio"], shell=True, stdout=subprocess.DEVNULL)
                if (obs_output.returncode) == 0:
                    obs_install_button.set_sensitive(False)
                    obs_remove_button.set_sensitive(True)
                else:
                    obs_install_button.set_sensitive(True)
                    obs_remove_button.set_sensitive(False)       
                gameutils_output = subprocess.run(["dpkg -s pika-gameutils-meta"], shell=True, stdout=subprocess.DEVNULL)
                if (gameutils_output.returncode) == 0:
                    gameutils_install_button.set_sensitive(False)
                    gameutils_remove_button.set_sensitive(True)
                else:
                    gameutils_install_button.set_sensitive(True)
                    gameutils_remove_button.set_sensitive(False)
                krita_output = subprocess.run(["dpkg -s krita"], shell=True, stdout=subprocess.DEVNULL)
                if (krita_output.returncode) == 0:
                    krita_install_button.set_sensitive(False)
                    krita_remove_button.set_sensitive(True)
                else:
                    krita_install_button.set_sensitive(True)
                    krita_remove_button.set_sensitive(False)  
                msttf_output = subprocess.run(["dpkg -s ttf-mscorefonts-installer"], shell=True, stdout=subprocess.DEVNULL)
                if (msttf_output.returncode) == 0:
                    msttf_install_button.set_sensitive(False)
                    msttf_remove_button.set_sensitive(True)
                else:
                    msttf_install_button.set_sensitive(True)
                    msttf_remove_button.set_sensitive(False)  
                libreoffice_output = subprocess.run(["dpkg -s pika-libreoffice-meta"], shell=True, stdout=subprocess.DEVNULL)
                if (libreoffice_output.returncode) == 0:
                    libreoffice_install_button.set_sensitive(False)
                    libreoffice_remove_button.set_sensitive(True)
                else:
                    libreoffice_install_button.set_sensitive(True)
                    libreoffice_remove_button.set_sensitive(False)
                gameextra_output = subprocess.run(["dpkg -s pika-gameutils-meta-extra"], shell=True, stdout=subprocess.DEVNULL)
                if (gameextra_output.returncode) == 0:
                    gameextra_install_button.set_sensitive(False)
                    gameextra_remove_button.set_sensitive(True)
                else:
                    gameextra_install_button.set_sensitive(True)
                    gameextra_remove_button.set_sensitive(False)  
                fabiscafe_output = subprocess.run(["dpkg -s fabiscafe-devices"], shell=True, stdout=subprocess.DEVNULL)
                if (fabiscafe_output.returncode) == 0:
                    fabiscafe_install_button.set_sensitive(False)
                    fabiscafe_remove_button.set_sensitive(True)
                else:
                    fabiscafe_install_button.set_sensitive(True)
                    fabiscafe_remove_button.set_sensitive(False)  
                time.sleep(10)
        
        t1 = threading.Thread(target=app_state_refresh_func)
        t1.start()
        
        self.main_Sidebar = self.builder.get_object("main_Sidebar")
        self.Stack = self.builder.get_object("Stack")
        self.sidebar_btn = self.builder.get_object("sidebar_btn")
        
        def resolution_refresh_func():
            while window_state_refresh == True:
                        time.sleep(1)
                        if self.window.get_size()[0] < 650:
                                                self.sidebar_btn.show()
                                                if self.sidebar_btn.get_active() == False:
                                                        self.Stack.show()
                                                        self.main_Sidebar.hide()
                                                else:
                                                        self.main_Sidebar.show()
                                                        self.Stack.hide()
                                                        self.main_Sidebar.set_hexpand(True)
                        else:
                                                        self.sidebar_btn.hide()
                                                        self.Stack.show()
                                                        self.main_Sidebar.show()
                                                        self.main_Sidebar.set_hexpand(False)
        
        t2 = threading.Thread(target=resolution_refresh_func)
        t2.start()
        
        def app_state_refresh_kill(self):
            global app_state_refresh
            global window_state_refresh
            app_state_refresh = False
            window_state_refresh = False
            
        
        win.connect("destroy", app_state_refresh_kill)
        
    ### Start up Switch ###
        
        startup_switch = self.builder.get_object("startup_switch")
        
        startup_switch.set_active(settings.get_boolean("startup-show"))
    
        startup_switch.connect("toggled", lambda btn: settings.set_boolean("startup-show", btn.get_active()))
        
    ### Hardcoded icons ###
        if (settings.get_boolean("use-system-icons")) == True:
            update_logo = self.builder.get_object("distrosync_logo_2")
            codec_install_logo = self.builder.get_object("codec_install_logo")
            nvidia_logo = self.builder.get_object("nvidia_logo")
            software_logo = self.builder.get_object("software_logo")
            webapps_logo = self.builder.get_object("webapps_logo")
            layout_logo_2 = self.builder.get_object("layout_logo_2")
            
            blender_install_logo = self.builder.get_object("blender_install_logo")
            kdenlive_install_logo = self.builder.get_object("kdenlive_install_logo")
            obs_install_logo = self.builder.get_object("obs_install_logo")
#            discord_install_logo = self.builder.get_object("discord_install_logo")
            gameutils_install_logo = self.builder.get_object("gameutils_install_logo")
            msttf_install_logo = self.builder.get_object("msttf_install_logo")
            krita_install_logo = self.builder.get_object("krita_install_logo")
            libreoffice_install_logo = self.builder.get_object("libreoffice_install_logo")
            gameextra_install_logo = self.builder.get_object("gameextra_install_logo")
            fabiscafe_install_logo = self.builder.get_object("fabiscafe_install_logo")

            amd_logo = self.builder.get_object("amd_logo")
            rocm_logo = self.builder.get_object("rocm_logo")
            xone_logo = self.builder.get_object("xone_logo")
            protonup_logo = self.builder.get_object("protonup_logo")
            
            dm_logo = self.builder.get_object("dm_logo")
            pling_logo = self.builder.get_object("pling_logo")
            layout_logo = self.builder.get_object("layout_logo")
            theme_logo = self.builder.get_object("theme_logo")
            extension_logo = self.builder.get_object("extension_logo")
            
#            troubleshoot_logo = self.builder.get_object("troubleshoot_logo")
#            doc_logo = self.builder.get_object("doc_logo")
#            distrosync_logo = self.builder.get_object("distrosync_logo")
            
#            discord_logo = self.builder.get_object("discord_logo")
#            reddit_logo = self.builder.get_object("reddit_logo")
            
#            patreon_logo = self.builder.get_object("patreon_logo")
#            design_logo = self.builder.get_object("design_logo")
#            ge_gitlab_logo = self.builder.get_object("ge_gitlab_logo")
#            ge_github_logo = self.builder.get_object("ge_github_logo")
#            cosmo_github_logo = self.builder.get_object("cosmo_github_logo")
            
            ###
            
            update_logo.set_from_icon_name("system-software-update", 80)
            codec_install_logo.set_from_icon_name("media-tape", 80)
            nvidia_logo.set_from_icon_name("nvidia", 80)
            software_logo.set_from_icon_name("media-floppy", 80)
            webapps_logo.set_from_icon_name("applications-internet", 80)
            layout_logo_2.set_from_icon_name("desktop", 24)
            
            blender_install_logo.set_from_icon_name("blender", 80)
            kdenlive_install_logo.set_from_icon_name("kdenlive", 80)
            obs_install_logo.set_from_icon_name("obs", 80)
#            discord_install_logo.set_from_icon_name("discord", 80)
            gameutils_install_logo.set_from_icon_name("input-gaming", 80)
            krita_install_logo.set_from_icon_name("krita", 80)
            libreoffice_install_logo.set_from_icon_name("libreoffice", 80)
            msttf_install_logo.set_from_icon_name("fonts", 80)
            gameextra_install_logo.set_from_icon_name("input-gaming", 80)

            amd_logo.set_from_icon_name("amd", 80)
            rocm_logo.set_from_icon_name("amd", 80)
            xone_logo.set_from_icon_name("input-gaming", 80)
            protonup_logo.set_from_icon_name("net.davidotek.pupgui2", 80)
            
            dm_logo.set_from_icon_name("applications-graphics", 80)
            pling_logo.set_from_icon_name("applications-graphics", 80)
            layout_logo.set_from_icon_name("desktop", 80)
            theme_logo.set_from_icon_name("applications-graphics", 80)
            extension_logo.set_from_icon_name("application-x-addon", 80)
            
#            troubleshoot_logo.set_from_icon_name("applications-graphics", 80)
#            doc_logo.set_from_icon_name("applications-graphics", 80)
#            distrosync_logo.set_from_icon_name("system-software-update", 80)
            
#            discord_logo.set_from_icon_name("discord", 80)
#            reddit_logo.set_from_icon_name("reddit", 80)


        pass
        
    ### ENTER LOOK WINDOW ###
    def enter_add_software(self, widget):
        install_window =  self.builder.get_object("install_Window")
        install_window.show()
    ### EXIT LOOK WINDOW ###
    def close_add_software(self, widget, event):
        return self.builder.get_object("install_Window").hide_on_delete()
    
    ##### FIRST STEPS ENTRIES #####
    
    def on_sidebar_btn_pressed(self, widget):
        time.sleep(1)
        if self.window.get_size()[0] < 650:
                if self.Stack.get_visible() == True:
                        self.sidebar_btn.set_active(False) 
                        self.main_Sidebar.show()
                        self.Stack.hide()
                else:
                        self.sidebar_btn.set_active(True)
                        self.Stack.show()
                        self.main_Sidebar.hide()
    
    
    #### DRIVER ENTRIES ####
    
    ### CODEC ###
    def enter_install_codec(self, widget):
        subprocess.Popen(["/usr/lib/pika/welcome/codec.sh"], shell=True)
    ### NVIDIA ###
    def enter_nvidia(self, widget):
        subprocess.Popen(["/usr/lib/pika/welcome/nvidia.sh"], shell=True)
    ### AMD PRO ###
    def enter_amd(self, widget):
        subprocess.Popen(["/usr/bin/pika-amdgpu-config"], shell=True)
    ### ROCm ###
    def enter_rocm(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install pika-rocm-meta'"], shell=True)
    ### XONE ###
    def enter_xone(self, widget):
        subprocess.Popen(["/usr/bin/pika-controller-config"], shell=True)
    ### PROTONUP ###
    def enter_protonup(self, widget):
        flatpak_protonup_output = subprocess.run(["flatpak info net.davidotek.pupgui2"], shell=True)
        if (flatpak_protonup_output.returncode) != 0:
            subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c 'pkexec flatpak -y install net.davidotek.pupgui2'"], shell=True)
        else:
            subprocess.Popen(["flatpak run net.davidotek.pupgui2"], shell=True)
   
   
    #### Apps Entries ####
   
    ### APPS ###
    def enter_apps(self, widget):
        subprocess.Popen(["/usr/lib/pika/welcome/apps.sh"], shell=True)
    ### WEBAPPS ###
    def enter_webapps(self, widget):
        subprocess.Popen(["/usr/bin/webapp-manager"], shell=True)

    ##### QUICK SETUP ENTRIES #####
    
    ### LOGIN MANAGER ###
    def enter_dm(self, widget):
        subprocess.Popen(["/usr/bin/pika-login-config"], shell=True)
    ### LAYOUTS ###
    def enter_layout(self, widget):
        layouts_file = Path('/usr/bin/pika-gnome-layouts')
        if layouts_file.is_file():
            subprocess.Popen(["/usr/bin/pika-gnome-layouts"], shell=True)
        else:
            subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install pika-gnome-layouts'"], shell=True)
        pass
    ### THEMES ###
    def enter_theme(self, widget):
        subprocess.Popen(["/usr/bin/gnome-tweaks"], shell=True)
    ### PLING ###
    def enter_pling(self, widget):
        subprocess.Popen(["xdg-open https://pling.com/"], shell=True)
    ### EXTENSION ###
    def enter_extension(self, widget):
        subprocess.Popen(["/usr/bin/extension-manager"], shell=True)

    #### TROUBLESHOOT ENTRIES ####
    
    ### Troubleshoot ###
    def enter_troubleshoot(self, widget):
        subprocess.Popen(["xdg-open https://pikaproject.org/docs/upgrade-troubleshooting/"], shell=True)
    ### Docs ###
    def enter_doc(self, widget):
        subprocess.Popen(["xdg-open https://pikaproject.org/docs/"], shell=True)
    ### Distro Sync ###
    def enter_distrosync(self, widget):
        subprocess.Popen(["update-manager"], shell=True)


    #### COMMUNITY ENTRIES ####
    
    ### discord ###
    def enter_discord(self, widget):
        subprocess.Popen(["xdg-open https://discord.gg/6y3BdzC"], shell=True)
    ### reddit ###
    def enter_reddit(self, widget):
        subprocess.Popen(["xdg-open https://www.reddit.com/r/pikaProject/"], shell=True)
        
    #### Contribute ENTRIES ####
    
    ### patreon ###
    def enter_patreon(self, widget):
        subprocess.Popen(["xdg-open https://www.patreon.com/gloriouseggroll"], shell=True)
    ### design ###
    def enter_design(self, widget):
        subprocess.Popen(["xdg-open https://discord.com/channels/110175050006577152/1015154123114549309"], shell=True)
    ### GE GITLAB ###
    def enter_ge_gitlab(self, widget):
        subprocess.Popen(["xdg-open https://gitlab.com/GloriousEggroll"], shell=True)
    ### GE GITHUB ###
    def enter_ge_github(self, widget):
        subprocess.Popen(["xdg-open https://github.com/GloriousEggroll"], shell=True)
    ### COSMO GITHUB ###
    def enter_cosmo_github(self, widget):
        subprocess.Popen(["xdg-open https://github.com/CosmicFusion"], shell=True)
    ###############################################################
    #### Install Window ####
    
    ### Blender ###
    def enter_install_blender(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install blender'"], shell=True)
    def enter_remove_blender(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove blender'"], shell=True)
    
    ### KDENLIVE ###
    def enter_install_kdenlive(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install kdenlive'"], shell=True)
    def enter_remove_kdenlive(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove kdenlive'"], shell=True)
    ### OBS STUDIO ###
    def enter_install_obs(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install obs-studio'"], shell=True)
    def enter_remove_obs(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove obs-studio'"], shell=True)
    ### DISCORD ###
    def enter_install_discord(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install discord'"], shell=True)
    def enter_remove_discord(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove discord'"], shell=True)
    ### GAME UTILS ###
    def enter_install_gameutils(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install pika-gameutils-meta'"], shell=True)
    def enter_remove_gameutils(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove pika-gameutils-meta'"], shell=True)
    ### MSTTF ###
    def enter_install_msttf(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c 'pkexec apt install ttf-mscorefonts-installer'"], shell=True)
    def enter_remove_msttf(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c 'pkexec apt remove ttf-mscorefonts-installer'"], shell=True)
    ### LIBREOFFICE ###
    def enter_install_libreoffice(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install pika-libreoffice-meta'"], shell=True)
    def enter_remove_libreoffice(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove pika-libreoffice-meta'"], shell=True)
    ### KRITA ###
    def enter_install_krita(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install krita'"], shell=True)
    def enter_remove_krita(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove krita'"], shell=True)
    ### GAMEEXTRA ###
    def enter_install_gameextra(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install pika-gameutils-meta-extra'"], shell=True)
    def enter_remove_gameextra(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove pika-gameutils-meta-extra'"], shell=True)
    ### FABISCAFE ###
    def enter_install_fabiscafe(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh install fabiscafe-devices'"], shell=True)
    def enter_remove_fabiscafe(self, widget):
        subprocess.Popen(["/usr/bin/x-terminal-emulator -e bash -c '/usr/lib/pika/welcome/pkcon-install.sh remove fabiscafe-devices'"], shell=True)

Application()
Gtk.main()
