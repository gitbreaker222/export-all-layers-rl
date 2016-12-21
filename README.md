# export-all-layers-rl
## python plug-in for GIMP: Export all layers based on their names
- choose between JPG and PNG (compression predefined at ~90%).
- choose directory
- Save export: Does not override files with same name, but adds an postfix counter.

## INSTALLATION:
- To use the plug-in, move it to the gimp-plug-in folder.
- To find out that folder, look into gimps properties (folders --> Plugins)
- Usually there are two paths by default:
    - /home/MY-USERNAME/.gimp-2.8/plug-ins
    - /usr/lib/gimp/2.0/plug-ins
- First path, in the home-directory, is for this specific user only (I chose that, for it is easier to handle file-permissions on ubuntu).
- Second path is for global usage

### NOTE:
- New plug-ins do not load while gimp is running --> restart gimp
- Before gimp can load python-plug-ins, the permission has to be set to "executable"
	- For the KDE-desktop simply right-click the file --> permissions --> check "executable"
	- For gnome-desktop and windows it should be similar.
	- With terminal:
```sh
chmod 755 /path/to/file/export-all-layers-rl.py
```
>```
Info:
 7       5     5
user   group  world
r+w+x  r+x    r+x
4+2+1  4+0+1  4+0+1  = 755```		
 
- further information to chmod here: http://codex.wordpress.org/Changing_File_Permissions

## USAGE:
- In the gimp menu should appear an entry at the bottom of "file / export all layers"
- Give your layers the names, that should be the filename.

    > If a layer name ends with either ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".tiff", ".psd", the file extension for the target file will be replaced with chosen filetype. 

    > (For example: You load a bunch of .jpg-files into gimp and the file extension is within the layer name - that would not result in naming the file "picture.jpg.png")
- select the new function --> a plug-in window pops up --> choose directory and filetype


### SAY HELLO:
Don't be afraid to ask a question, if something is not working. 

If you like it, you might just tell me. This will sure motivate me in my future work :)

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
