#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *
import os

filetypes = [".jpg",".png",".bmp"]

#export parameter
#JPEG parameter
quality = 0.92
smoothing = 0.0
optimize = 1
progressive = 1
comment = ""
subsmp = 1
baseline = 1
restart = 1
dct = 1

#PNG parameter
interlace = 1
compression = 9
bkgd = 1
gama = 1
offs = 0
phys = 1
time = 1



# unique_filename from http://stackoverflow.com/questions/183480/is-this-the-best-way-to-get-unique-version-of-filename-w-python
def unique_filename(file_name):
    counter = 1
    file_name_parts = os.path.splitext(file_name) # returns ('/path/file', '.ext')
    while os.path.isfile(file_name):
        file_name = file_name_parts[0] + '_' + str(counter) + file_name_parts[1]
        counter += 1
    return file_name

# MAIN PART
def python_export_all_layers(image, path, filetype):
    print "============== python_save_all_layers START: ==============\n"
    #first choose the path to safe the images:
    #(path is input parameter "path" given from gui function PF_DIRNAME)
    print "save layers in \n %s \n" %path
    
    #...and convert "filetype" from index int to its string representation
    filetype = filetypes[filetype]
    
    # 2.: Choose File-Format preferences (currently preset on top of this skript)
    if filetype == ".jpg":
      # TODO
      pass
    elif filetype == ".png":
      # TODO
      pass
    elif filetype == ".bmp":
      # TODO
      pass
    
    
    # 3.: get layers
    print "image has following layers:\n", image.layers, "\n"
    
    # 4.: loop through layers
    # we don't want the image to be called "image.jpg.png", so...
    file_extensions = [".jpg", ".JPG", ".jpeg", "JPEG", ".png", ".PNG", ".bmp", ".BMP", ".gif", ".GIF", ".tif", ".TIF", ".tiff", ".TIFF", ".psd", ".PSD"]
    
    for layer in image.layers:
        print "current layer: %s \n" %layer.name
        
        # 5.: ...check for file extension pattern in name (assume, that there is no "image.png-weird.name"
        if not filetype in layer.name:
            #if file does not contain selected filetype, check for false extension...
            print "add "+filetype+" file extension to layer %s...\n" %layer.name
            for e in file_extensions:
                if e in layer.name:
                    print "replace", e
                    #...and cut the string plus concatenate chosen filetype
                    layer.name = layer.name[:layer.name.find(e)]
                    print "new name:", layer.name
                    break
            layer.name = layer.name + filetype
        
        # 6.: build the full path and ensure that it is unique
        file_path = unique_filename(path + "/" + layer.name)
        print "file path/name for that layer:\n %s \n" %file_path
        
        # 7.: and FINALLY save that layer!
        if filetype == ".jpg":
	  pdb.file_jpeg_save(image,	#image: IMAGE
			  layer, 	#drawable: DRAWABLE
			  file_path,	#filename: STRING
			  file_path,	#raw-filename: STRING
			  quality,	#quality: FLOAT
			  smoothing,	#smoothing: FLOAT
			  optimize,	#optimize: INT32
			  progressive,	#progressive: INT32
			  comment,	#comment: STRING
			  subsmp,	#subsmp: INT32
			  baseline,	#baseline: INT32
			  restart,	#restart: INT32
			  dct)		#dct: INT32
	  
	elif filetype == ".png":
	  pdb.file_png_save(image,	#image: IMAGE
			  layer, 	#drawable: DRAWABLE
			  file_path,	#filename: STRING
			  file_path,	#raw-filename: STRING
			  interlace,	#interlace: INT32
			  compression,	#compression: INT32
			  bkgd,		#bkgd: INT32
			  gama,		#gama: INT32
			  offs,		#offs: INT32
			  phys,		#phys: INT32
			  time)		#time: INT32
	  
	elif filetype == ".bmp":
	  pdb.file_bmp_save(image,	#image: IMAGE
			  layer, 	#drawable: DRAWABLE
			  file_path,	#filename: STRING
			  file_path)	#raw-filename: STRING
	
    
        
    print "all layers saved \n ------END------ \n"
    return


register(
        "python-fu-export-all-layers-rl",
         "Export all layers based on their names",
         """-Filenames are based on each layers names \n
         -if there are file-extensions (.jpg, .jpeg, .png, .bmp, .gif, .psd, .tif, .tiff), they will be replaced with specified type
         -available filetypes are: JPEG, PNG and BMP
         -currently the quality preferences are preset in the plug-in""",
         "Ruben La Biunda <ruben.labiunda@openmailbox.org>",
         "GNU",
         "2015",
         "export all layers",
         "*",
         [
            (PF_IMAGE, "image", "takes current image", None),
            (PF_DIRNAME, "directory", "the desired directory where to save", os.getcwd()),
            (PF_OPTION,"filetype",   "filetype:", 0, [".jpg",".png",".bmp"]), # initially 0th is choice
         ],
         [],
         python_export_all_layers,
         menu="<Image>/File",
         #domain=("gimp20-python", gimp.locale_directory)
        )
main()