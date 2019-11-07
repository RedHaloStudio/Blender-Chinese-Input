'''
Copyright (C) 2019 Red Halo Studio(发霉的红地蛋)
samytichadou@gmail.com

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
 "category": "Properties"}


import bpy

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
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
        row.label(text="Input Text Value")
        row = layout.row()
        row.prop(obj.data, "body", text="", icon="TEXT")
        row = layout.row()
        row.label(text='只支持单行文字', icon="QUESTION")
        row = layout.row()
        row.label(text='如需多行', icon="QUESTION")
        row = layout.row()
        row.label(text='输入后进入编辑模式自己换行', icon="QUESTION")


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()