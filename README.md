export-all-layers-rl
lexon222@gmx.de (2014)
====================

python plug-in for GIMP: Export all layers based on their names

INSTALLATION:
-To use the plug-in, move it to the gimp-plug-in folder.
-To find out that folder, look into gimps properties (folders --> Plugins)
-Usually there are two paths by default:
	 /home/MY-USERNAME/.gimp-2.8/plug-ins
	 /usr/lib/gimp/2.0/plug-ins
	 
	-First path, in the home-directory, is for this specific user only (I chose that, for it is easier to handle file-permissions on ubuntu).
	-Second path is for global usage

NOTE:
-Before gimp can load python-plug-ins, the permission has to be set to "executable"
	-For the KDE-desktop simply right-click the file --> permissions --> check "executable"
	-For gnome-desktop and windows it should be similar.
	-With terminal: chmod 755 /path/to/file/export-all-layers-rl.py
		Info:
		  7       5     5
		 user   group  world
		 r+w+x  r+x    r+x
		 4+2+1  4+0+1  4+0+1  = 755
	further information to chmod here: http://codex.wordpress.org/Changing_File_Permissions
-New plug-ins do not load while gimp is running --> restart gimp


USAGE:
-In the gimp menu should appear an entry at the bottom: file --> export all layers as .png
-Give your layers the names, that should be the filename
	If a layer name ends with either ".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".psd",
	the file extension for the target file will be replaced with ".png"
	(For example: You load a bunch of .jpg-files into gimp and the file extension
	is within the layer name - that would not result in naming the file "picture.jpg.png")
-select the new function --> a plug-in window pops up --> choose directory


SAY HELLO:
-don't be afraid to ask a question, if something is not working
-if you like it, you might just tell me. This will sure motivate me in my future work :)
