# Scripted by Oscar Nebe Abad 05-2019 v1
import os
import bpy

# bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
# bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)


# THIS IS THE PANEL IN RENDER PROPS
class CommandlineLauncherPanel(bpy.types.Panel):
	"""Creates a Panel in the Render properties window"""
	bl_label = "CommandLine Render Launcher"
	bl_idname = "RENDER_PT_CommandlineLauncher"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"


    # PANEL - THIS DRAW THE BUTTONS INSIDE PANEL FOR OPTIONS
	def draw(self, context):
		layout = self.layout

        # PANEL - THIS IS THE OVERALL MESSAGE TEXT
		row = layout.row()
		row.label(text="ATENTION! This close Blender GUI.", icon='WORLD_DATA'),
		row = layout.row()
		row.label(text="Blender will auto-reopen.")

        # PANEL - BASIC OPTIONS BUTTONS FOR RENDER
        row = layout.row()
        row.operator("render.render", text="Render Still (Shift+F12)")
        row = layout.row()
        row.operator("render.render", text="Render Animation (Shift+Ctrl+F12)")


    # THIS DRAW THE LIST CAMERAS FOR ALLCAMERAS & EXTRA OPTIONS

        # THIS DRAW THE CAMERA LIST FOR ALLCAMERAS AND BUTTONS
		row = layout.row()
		row.label(text="By Cameras")
		row = layout.row()
		row.operator("render.render", text="Render Cameras Stills")
		row = layout.row()
		row.operator("render.render", text="Render Cameras Animation")
		row = layout.row()
		row.operator("render.render", text="Render Playblast Animation")

        # THIS DRAW THE EXTRA OPTIONS
		row = layout.row()
		row.label(text="Other Options")
		row = layout.row()
		row.operator("render.render", text="All VSE Timeline Playblast")
		row = layout.row()
		row.operator("render.render", text="All Selected Bakes")
		

def register():
	bpy.utils.register_class(CommandlineLauncherPanel)

def unregister():
	bpy.utils.unregister_class(CommandlineLauncherPanel)

if __name__ == "__main__":
	register()

#       ESTRUCTURA
#       
#       PANEL (RENDER context)
#           Label Mensaje
#           Boolean Checkbox Commandline Yes/No
#           Boolean Checkbox AllCameras Yes/No
#           Boton Function Still (Shift + F12)
#           Boton Function Animation (Shift + Ctrl + F12)
#           Boton Function AllBakes (Alt + Shift + Ctrl + F12)
#       BOTON Still (Shift F12)
#           If CommandLine yes
#               if AllCameras yes
#                   queue render scene.AllCameras.cameras
#                   then for Each cameras...
#                       
#               if AllCameras not
#                   grab the LastSelectedCamera...
#
#               ...Save BlendFile, BatchFile in SavedPath
#                       if not, write files in TempPath
#               
#                   write BlendFile.path into BatchFile.RenderPath
#                   write Launch/ReUseLast commandline
#                   write closes LastUsedBlenderPID
#                   write execute render with ActualFrame
#                   SCRIPT for Updating stats info in commandline each 3 seconds
#                   When finish Render saves in BlendFile.path with BlendFileName+DateName
#                   
#                   Open Blender with LastSessionFile
#                   Close process on commandline print RenderStats
#                   
#
#
#   x8 faster command - https://developer.blender.org/T63249
#   https://github.com/RayMairlot/Batch-Render-Tools/blob/master/batchRenderTools.py
#   https://github.com/VertStretch/RenderBurst
#   https://docs.blender.org/api/master/