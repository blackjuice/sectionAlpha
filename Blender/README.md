blackjuice's Blender experience

# Contents:

* [Documentation](#documentation)
* [Free library](#free_library)
* [Hotkey table](#hotkey_table)
* [Tips](#tips)
* [Cheatsheet image](#cheatsheet)

## Documentation

Official doc for Blender:

* [Blender Hotkey](http://wiki.blender.org/index.php/Doc:2.4/Reference/Hotkeys/All)
* [Blender manual Sphinx](https://www.blender.org/manual/contents.html)

[> back to main Contents](#contents)

## Free_library

List of websites containing free models for reference:

* [tf3dm.com](http://tf3dm.com/)
* [cgtrader](http://www.cgtrader.com/)
* [BenSimonds basemesh body](http://bensimonds.com/2011/07/31/basemeshes/)

[> back to main Contents](#contents)

## Hotkey_table

Desperate times calls for desperate measures.

List:

* [common](#common)
* [hints](#hints)
* [camera](#camera)
* [wheel design](#wheel_design)
* [background](#background)

[> back to main Contents](#contents)

Category:

* #### *common*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|`H`            | Hide              | | |
|`Alt + H`      | Unhide            | | |
|`Ctrl + J`     | Make multiple Blender objects into one        | | |
|`P`            | Opposite of `Ctrl + J`                        | | |
|`Shift + Ctrl + Alt + C`| Recenter pivot point of an object  | and select **Origin to Geometry**. | [link](http://blender.stackexchange.com/questions/14294/how-to-recenter-an-objects-origin) |

[> back to Hotkey_table](#hotkey_table)

* #### *hints*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|  |  | Switch to **edit mode** after .obj import | [link](http://blenderartists.org/forum/showthread.php?127550-newbie-can-t-switch-to-edit-mode-after-obj-import)

[> back to Hotkey_table](#hotkey_table)

* #### *wheel_design*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|`Alt + D`      | Duplicated Link   | wheel design | |
|`Ctrl + M`     | Mirroring         | wheel design | |

[> back to Hotkey_table](#hotkey_table)

* #### *camera*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
| --- | Change camera lens | Select 1st the camera, then at the editor menu, there is an filming device icon called Object Data. | [link](http://wiki.blender.org/index.php/Doc:2.4/Manual/Render/Camera/Depth_Of_Field)|
| `Q`           | Delete multiple material              | alternate | [click me](#deletemat) |
| hotkey        | PNG background transparency           | alternate | [click me](#pngalpha) |

[> back to Hotkey_table](#hotkey_table)

* #### *background*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
| --- | Add background reference image | Small PLUS sign at top right corner of the 3d view workspace | --- |

[> back to Hotkey_table](#hotkey_table)

## Tips

* [Delete multiple material](#tip001);
* [PNG background transparency](#tip002);
* [Set-up perspective view based on ref img](#tip003);

[> back to main Contents](#contents)

### Tip001
#### Can I delete all materials of all objects in a scene quickly?

Enable it in the `User Preferences > Addons`, select all objects `A`, hit `Q` over 3D View and chose **Remove Material Slots**:

![image](http://i.stack.imgur.com/MgkJ2.png)

Then use script:

```
python
    import bpy

    for ob in bpy.context.selected_editable_objects:
        ob.active_material_index = 0
        for i in range(len(ob.material_slots)):
            bpy.ops.object.material_slot_remove({'object': ob})
```

[> back to list of Tips](#tips)

### Tip002
#### Can Blender render pngs with the background transparent? [(source)](http://blender.stackexchange.com/questions/1303/can-blender-render-pngs-with-the-background-transparent)

At **CYCLES**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Film Panel``, check ``Transparent``.

![cycles](http://i.stack.imgur.com/pi6Kw.png)

At **Blender Render**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Shading Panel/OpenGL Render``, choose ``Alpha Transparent type``.

![cycles](http://i.stack.imgur.com/4LRZk.png)

[> back to list of Tips](#tips)

### Tip003
#### How to set-up the perspective view based on a reference image? [(source)](http://blender.stackexchange.com/questions/9328/how-to-set-up-the-perspective-view-based-on-a-reference-image)

[> back to list of Tips](#tips)

## Cheatsheet

From http://www.giudansky.com/

![cheatsheet](http://www.giudansky.com/images/downloads/blender/blender3d-shortcuts-infographic.png)

[> back to main Contents](#contents)
