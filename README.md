# ExportAllShapeKeysAsObj
Blender Script.

## Description
This script exports all of the shape keys of the active object as OBJ with the vertex order kept. Each exported OBJ file's name is the same as the shape key's.

![screen1](screen1.png 'screen1')

As an optional behavior, if you check _Mix Non Zero Shape Keys_, 
this script will skip the shape keys with non zenro value and export the rest of the shape keys with leaving non zero valued keys as it is, which means exported OBJs will have mixed shapes with non zero valued shape keys.

If you uncheck _Mix Non Zero Shape Keys_, regardless of the values of shape keys, this script will eport every single shape key as it is.

![screen2](screen2.png 'screen2') ![screen3](screen3.png 'screen3')

I tested this only on blender 2.92. Use this script at your own risk.

## Usage
1. Select the target object.

2. Run this script by "File" > "Export" > "Export All Shape Keys As Obj".

3. Choose destination directory, and set options below :
 - Mix Non Zero Shape Keys
  + If checked, this script will skip the shape keys with non zenro value and export the rest of the shape keys with leaving non zero valued keys as it is, which means exported OBJs will have mixed shapes with non zero valued shape keys.
  + If unchecked, this script will just export every single shape keys.

 - Scale
  + The same as blender OBJ export option.

 - Apply Modifiers
  + The same as blender OBJ export option.

 - Write Materials
  + The same as blender OBJ export option.

## Installation
Edit > Preferences > Add-ons > Install... and select export_all_shape_keys_as_obj.py

## Notice
* This script **will overwrite** the existing obj files with the same names.
