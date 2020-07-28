'''
Copyright (C) 2019 Red Halo Studio(发霉的红地蛋)

Created by Red Halo Studio(发霉的红地蛋)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {  
    "name": "Text Input",  
    "author": "Red Halo Studio",  
    "version": (0, 1),  
    "blender": (2, 80, 0),  
    "location": "Properties > Font > Text Value",  
    "description": "解决Window下无法输入中文的问题",  
    "wiki_url": "",  
    "tracker_url": "",  
    "category": "Properties"
 }

import bpy
from bpy.types import Operator, AddonPreferences
import os

class Tools_OT_insertNewline(Operator):
    bl_idname = "redhalo.insert_newline"
    bl_label = "插入换行符"
    bl_description = "Insert Newline Symbol\n插入换行符"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        bpy.context.active_object.data.body += "\n"
        return {'FINISHED'}

class Tools_OT_setFont(Operator):
    bl_idname = "redhalo.set_font"
    bl_label = "修改字体"
    bl_description = "设置为思源黑体"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        addonPath = os.path.dirname(__file__)
        fontName = "SourceHanSansCN-Normal.otf"
        fontPath = os.path.join(addonPath,fontName)
        font = bpy.data.fonts.load(filepath=fontPath)

        allFonts = bpy.data.fonts

        for f  in range(len(allFonts)):
            if allFonts[f].name == font.name:
                bpy.context.active_object.data.font = allFonts[f]
            else:
                bpy.context.active_object.data.font = font
        return {'FINISHED'}

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Text Value"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        active=bpy.context.active_object
        if active is not None:
            active_type=active.type
        else:
            active_type=""
        return active_type=='FONT'

    def draw(self, context): 
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.prop(obj.data, "body", text="", icon="OUTLINER_OB_FONT")
        row = layout.row()
        row.operator("redhalo.insert_newline", icon = "CHECKMARK")
        row.operator("redhalo.set_font", icon = "FILE_FONT")

def register():
    bpy.utils.register_class(Tools_OT_insertNewline)
    bpy.utils.register_class(Tools_OT_setFont)
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(Tools_OT_setFont)
    bpy.utils.unregister_class(Tools_OT_insertNewline)


if __name__ == "__main__":
    register()