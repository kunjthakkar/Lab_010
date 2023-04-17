from tkinter import *
from tkinter import ttk
import os
import ctypes
import poke_api
import image_lib


# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

#creating a image cache directory
img_cache_dir = os.path.join(script_dir, 'photos')
if not os.path.isdir(img_cache_dir):
    os.makedirs(img_cache_dir)



# Create the main window
root = Tk()
root.title(" Pokemon Image Viewer ")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(500,600)
# Set the window icon
icon_path = os.path.join(script_dir, 'POKEBALL.ico')

app_id = 'python_Pokemon_ImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(icon_path)
# inserting a frame 
frame_main = ttk.Frame(root)
frame_main.grid(row=0, column=0, sticky=NSEW)
frame_main.columnconfigure(0,weight=100)
frame_main.rowconfigure(0, weight=100)


#insert image into frame 
image_path = os.path.join(script_dir, 'Poke_photo.png')
poke_img = PhotoImage(file=image_path)
lbl_photo = ttk.Label(frame_main, image=poke_img)
lbl_photo.grid(padx=10, pady=10)

#insert the pull-down list of Pokemon names into the frame .
name_list = sorted(poke_api.get_pokemon_name())
cbox_names = ttk.Combobox(frame_main, values=name_list, state='readonly')
cbox_names.set("Select an Pokemon")
cbox_names.grid(padx=10, pady=10)

def handle_pokemon_select(event):
    sel_poke = cbox_names.get()
    global image_path
    image_path = poke_api.download_pokemon_artwork(sel_poke, img_cache_dir)
    
    poke_img['file'] = image_path
    return
    
cbox_names.bind('<<ComboboxSelected>>', handle_pokemon_select)


#Put "Set dekstop" button into frame 
def handle_set_dekstop():
    image_lib.set_desktop_background_image(image_path)
    

btn_set_as_dekstop = ttk.Button(frame_main, text='Set as Dekstop Image', command=handle_set_dekstop)
btn_set_as_dekstop.grid(padx=10, pady=(10,20))


root.mainloop()
