# Blender

* [Blender Hotkey](http://wiki.blender.org/index.php/Doc:2.4/Reference/Hotkeys/All)
* [Blender manual Sphinx](https://www.blender.org/manual/contents.html)

### List of content:

* [Reference](#reference)
* [Cheatsheet image](#cheatsheet)

## <a name="reference"></a> Reference (free models)

* [tf3dm.com](http://tf3dm.com/)
* [cgtrader](http://www.cgtrader.com/)

## Desperate times calls for help

| hotkey | function | alternate | source |
|:------:|:--------:|:---------:|:------:|
|``H``        | Delete face connected to specific vertices    | alternate | source |
|``Ctrl + J`` | Make multiple Blender objects into one        | alternate | source |
| hotkey | Add background reference image                | Small PLUS sign at top right corner of the 3d view workspace | source |
| hotkey | Change camera lens                            | Select 1st the camera, then at the editor menu, there is an filming device icon called Object Data. | [link](http://wiki.blender.org/index.php/Doc:2.4/Manual/Render/Camera/Depth_Of_Field)|
| hotkey | Switch to **edit mode** after .obj import | | [link](http://blenderartists.org/forum/showthread.php?127550-newbie-can-t-switch-to-edit-mode-after-obj-import)
|``Shift + Ctrl + Alt + C``| Recenter point of an abject | and select **Origin to Geometry**. | [link](http://blender.stackexchange.com/questions/14294/how-to-recenter-an-objects-origin) |
| ``Q`` | Delete multiple material | alternate | [click me](#deletemat) |
| hotkey | PNG background transparency | alternate | [click me](#pngalpha) |
| hotkey | function | alternate | source |

## <a name="deletemat"></a> Can I delete all materials of all objects in a scene quickly?

Enable it in the ``User Preferences > Addons``, select all objects ``A``, hit ``Q`` over 3D View and chose **Remove Material Slots**:

![image](http://i.stack.imgur.com/MgkJ2.png)

Then use script:

    import bpy
    
    for ob in bpy.context.selected_editable_objects:
        ob.active_material_index = 0
        for i in range(len(ob.material_slots)):
            bpy.ops.object.material_slot_remove({'object': ob})
            
## <a name="pngalpha"></a> Can Blender render pngs with the background transparent? [(source)](http://blender.stackexchange.com/questions/1303/can-blender-render-pngs-with-the-background-transparent)

At **CYCLES**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Film Panel``, check ``Transparent``.

![cycles](http://i.stack.imgur.com/pi6Kw.png)

At **Blender Render**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Shading Panel/OpenGL Render``, choose ``Alpha Transparent type``.

![cycles](http://i.stack.imgur.com/4LRZk.png)

## <a name="cheatsheet"></a>Cheatsheet

![cheatsheet](http://www.giudansky.com/images/downloads/blender/blender3d-shortcuts-infographic.png)

[source link](http://blenderartists.org/forum/showthread.php?353472-Blender-key-map-infographic-poster)
