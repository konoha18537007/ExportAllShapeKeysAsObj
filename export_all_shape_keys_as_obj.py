#-*- coding: utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info={
    "name" : "Export All Shape Keys As OBJ",
    "author" : "konoha18537007",
    "version" : (1, 0),
    "blender": (2, 80, 0),
    "category": "Import-Export",
    "location": "File > Export",
}


import bpy

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, FloatProperty

import os


class ExportAllShapeKeysAsObj(bpy.types.Operator, ExportHelper):
    '''This script exports all of the shape keys of the active object as OBJ with the vertex order kept.
    As an optional behavior, if there exists any shape keys with non zero value, this script can skip those keys and export the rest of the shape keys with leaving non zero valued keys as they are, which means exported OBJs will have mixed shapes with non zero valued shape keys.'''
    bl_idname = "object.export_all_shape_keys_as_obj"
    bl_label = "Select Dir"
    bl_options = {'REGISTER'}

    DEBUG = False
    
    filename_ext = ".obj"

    filepath: StringProperty(
        name="Export Dir",
        subtype= 'DIR_PATH',
        default= '',
    )

    filter_glob: StringProperty(
        default="*.obj",
        options={'HIDDEN'},
        maxlen=255,
    )

    is_mix: BoolProperty(
        name="Mix Non Zero Shape Key",
        description="If checked, any shape keys with non zero value will be skipped and left as they are while exporting.",
        default=False,
    )

    scale: FloatProperty(
        name="Scale",
        min=0.00000001,
        soft_min=0.01,
        step=1,
        default=1.0,
    )

    is_mod: BoolProperty(
        name="Apply Modifiers",
        default=True,
    )

    is_mtl: BoolProperty(
        name="Write Materials",
        default=False,
    )


    @classmethod
    def poll(cls, context):
        o = context.active_object
        return o is not None and o.data.shape_keys is not None


    def execute(self, context):
        ret = self.__write_data(context)
        return {'FINISHED'}


    def invoke(self, context, event):
        o = bpy.context.active_object
        if o is None or o.data.shape_keys is None :
            self.report({"ERROR"}, "Object not selected, or Object has no shape key")
            return { 'RUNNING_MODAL' }

        self.filepath = os.path.join(os.path.dirname(bpy.data.filepath) ,"")
        wm = context.window_manager.fileselect_add(self)
        return { 'RUNNING_MODAL' }


    def __write_data(self,context):
        o = bpy.context.active_object

        # mixture non zero shape keys
        if self.is_mix:
            for kb in o.data.shape_keys.key_blocks[1:]:
                if kb.value != 0:
                    continue # skip to next shape key
                    
                kb.value = 1

                obj_path = os.path.join(self.filepath, kb.name) + ".obj"
                bpy.ops.export_scene.obj(
                    filepath = obj_path,
                    check_existing = False,
                    use_selection = True,
                    use_mesh_modifiers = self.is_mod,
                    use_normals = True,
                    use_materials = self.is_mtl,
                    use_uvs = True,
                    keep_vertex_order = True,
                    global_scale = self.scale,
                    )

                kb.value = 0
                    
        # export every shape key regardless of zero or non zero
        else:
            # memorize all shape keys' values and set them to 0
            sk_vals = []
            for kb in o.data.shape_keys.key_blocks:
                sk_vals.append(kb.value)
                kb.value = 0

            for kb in o.data.shape_keys.key_blocks[1:]:
                kb.value = 1

                obj_path = os.path.join(self.filepath, kb.name) + ".obj"
                bpy.ops.export_scene.obj(
                    filepath = obj_path,
                    check_existing = False,
                    use_selection = True,
                    use_mesh_modifiers = self.is_mod,
                    use_normals = True,
                    use_materials = self.is_mtl,
                    use_uvs = True,
                    keep_vertex_order = True,
                    global_scale = self.scale,
                    )

                kb.value = 0

        return True
                

    def __debug(self,msg):
        if self.DEBUG:
            self.report({"INFO"},msg)
        return


def menu_func_export(self, context):
    self.layout.operator(ExportAllShapeKeysAsObj.bl_idname, text="Export All Shape Keys As OBJ")

classes = [
    ExportAllShapeKeysAsObj,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

