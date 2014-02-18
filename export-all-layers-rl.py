#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *
import os

# unique_filename from http://stackoverflow.com/questions/183480/is-this-the-best-way-to-get-unique-version-of-filename-w-python
def unique_filename(file_name):
    counter = 1
    file_name_parts = os.path.splitext(file_name) # returns ('/path/file', '.ext')
    while os.path.isfile(file_name):
        file_name = file_name_parts[0] + '_' + str(counter) + file_name_parts[1]
        counter += 1
    return file_name

# MAIN PART
def python_export_all_layers(image, path):
    print "python_save_all_layers START: \n"
    #first choose the path to safe the images:
    #(path is input parameter "path" given from gui function PF_DIRNAME)
    print "save layers in \n %s \n" %path
    
    # 2.: Choose File-Format (later - for now its png)
    print "file format selection not yet implemented \n"
    
    # 3.: get layers
    print "image has following layers:\n", image.layers, "\n"
    
    # 4.: loop through layers
    # we don't want the image to be called "image.jpg.png", so...
    false_file_extensions = [".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".psd"]
    for layer in image.layers:
        layer_name = layer.name
        print "current layer: %s \n" %layer_name
        
        # 5.: ...check for right file extension (assume, that there is no "image.png-weird.name"
        if not ".png" in layer_name:
            #if file does not end with .png, check for false extension...
            print "add .png file extension to layer %s...\n" %layer_name
            for e in false_file_extensions:
                if e in layer_name:
                    print "replace", e
                    #...and cut the string plus concatenate .png
                    layer_name = layer_name[:layer_name.find(e)]
                    print "new name:", layer_name
                    break
            layer_name = layer_name + ".png"
        
        # 6.: build the full path and ensure that it is unique
        file_path = unique_filename(path + "/" + layer_name)
        print "file path/name for that layer:\n %s \n" %file_path
        
        # 7.: and FINALLY save that layer!
        pdb.file_png_save_defaults(image, layer, file_path, file_path)
    
    
        
    print "all layers saved \n ------END------ \n"
    return


register(
        "python-fu-export-all-layers-rl",
         "Export all layers based on their names as .png",
         """-Filenames are based on each layers names \n
         -if there are file-extensions (.jpg, .jpeg, .bmp, .gif, .psd, .tif, .tiff), they will be replaced with .png
         -saves images with default preferences for PNG-Format""",
         "Breaker222 <lexon222@gmx.de",
         "GNU",
         "2014",
         "export all layers as .png",
         "*",
         [
            (PF_IMAGE, "image", "takes current image", None),
            (PF_DIRNAME, "directory", "the desired directory where to save", os.getcwd())
         ],
         [],
         python_export_all_layers,
         menu="<Image>/File",
         #domain=("gimp20-python", gimp.locale_directory)
        )
main()