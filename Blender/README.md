blackjuice's Blender experience

version: **Blender 2.77**

# Notes

This Markdown page is available at:

* [blackjuice's GitHub](https://github.com/blackjuice/sectionAlpha/tree/master/Blender)
* [saguahollic's wordpress blog](https://saguahollic.wordpress.com/)

<!-- ================================================================================== -->
# Contents

* [Documentation](#documentation)
* [Free library](#freelibrary)
* [Hotkey table](#hotkeytable)
* [Tips](#tips)
* [Cheatsheet image](#cheatsheet)

<!-- ================================================================================== -->
## Documentation

Official doc for Blender:

* [Blender Hotkey](http://wiki.blender.org/index.php/Doc:2.4/Reference/Hotkeys/All)
* [Blender manual Sphinx](https://www.blender.org/manual/contents.html)

[> back to main Contents](#contents)

<!-- ================================================================================== -->
## FreeLibrary

List of websites containing free models for reference:

* [tf3dm.com](http://tf3dm.com/)
* [cgtrader](http://www.cgtrader.com/)
* [BenSimonds basemesh body](http://bensimonds.com/2011/07/31/basemeshes/)

[> back to main Contents](#contents)

<!-- ================================================================================== -->
## HotkeyTable

Desperate times calls for desperate measures.

List:

* [common](#common)
* [hints](#hints)
* [camera](#camera)
* [wheel design](#wheel_design)
* [background](#background)

[> back to main Contents](#contents)

Category:

#### * *common*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|`H`            | Hide              | | |
|`Alt + H`      | Unhide            | | |
|`Ctrl + J`     | Make multiple Blender objects into one        | | |
|`P`            | Opposite of `Ctrl + J`                        | | |
|`Shift + Ctrl + Alt + C`| Recenter pivot point of an object  | and select **Origin to Geometry**. | [link](http://blender.stackexchange.com/questions/14294/how-to-recenter-an-objects-origin) |

[> back to Hotkey_table](#hotkeytable)

<!-- ---------------------------------------------------------------------------------- -->
#### * *hints*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|  |  | Switch to **edit mode** after .obj import | [link](http://blenderartists.org/forum/showthread.php?127550-newbie-can-t-switch-to-edit-mode-after-obj-import)

[> back to Hotkey_table](#hotkeytable)


<!-- ---------------------------------------------------------------------------------- -->
#### * *wheel_design*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
|`Alt + D`      | Duplicated Link   | wheel design | |
|`Ctrl + M`     | Mirroring         | wheel design | |

[> back to Hotkey_table](#hotkeytable)


<!-- ---------------------------------------------------------------------------------- -->
#### * *camera*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
| | Change camera lens | Select 1st the camera, then at the editor menu, there is an filming device icon called Object Data. | [link](http://wiki.blender.org/index.php/Doc:2.4/Manual/Render/Camera/Depth_Of_Field)|

[> back to Hotkey_table](#hotkeytable)


<!-- ---------------------------------------------------------------------------------- -->
#### * *background*

| hotkey | function | comment | source |
|:------:|:--------:|:-------:|:------:|
| `T` | Add background reference image | Activate `Properties Shelf` with the `T` key. At `Background Images`, click `Add Image` | |

[> back to Hotkey_table](#hotkeytable)

<!-- ================================================================================== -->
## Tips

* [Delete multiple material](#tip001);
* [PNG background transparency](#tip002);
* [Set-up perspective view based on ref img](#tip003);
* [11 tips for speeding up rendering cycles](#tip004);

[> back to main Contents](#contents)


<!-- ---------------------------------------------------------------------------------- -->
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


<!-- ---------------------------------------------------------------------------------- -->
### Tip002
#### Can Blender render pngs with the background transparent?

[Click here](http://blender.stackexchange.com/questions/1303/can-blender-render-pngs-with-the-background-transparent) for the source content.

At **CYCLES**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Film Panel``, check ``Transparent``.

![cycles](http://i.stack.imgur.com/pi6Kw.png)

At **Blender Render**:

* At ``Properties Editor > Render Context > Output Panel``, choose ``RGBA``;
* At ``Properties Editor > Render Context > Shading Panel/OpenGL Render``, choose ``Alpha Transparent type``.

![cycles](http://i.stack.imgur.com/4LRZk.png)

[> back to list of Tips](#tips)


<!-- ---------------------------------------------------------------------------------- -->
### Tip003
#### How to set-up the perspective view based on a reference image?

[Click here](http://blender.stackexchange.com/questions/9328/how-to-set-up-the-perspective-view-based-on-a-reference-image) for the source content.

[> back to list of Tips](#tips)

<!-- ---------------------------------------------------------------------------------- -->
### Tip004
#### At boundlessblending: “11 crazy tweaks to speed up cycles”

11 useful tips on speeding up your rendering on cycles!

What I always thought about doing it but never really did it was to use render layers to distribute calculations. Is really logical to think that rendering all layers together is more expensive than rendering each one separately. But for some time, I thought it wasn’t.

[Click here](https://boundlessblending.blogspot.com.br/2016/04/blender-fast-rendering.html) for the source content.

[> back to list of Tips](#tips)

<!-- ================================================================================== -->
## Cheatsheet

From http://www.giudansky.com/

![cheatsheet](http://www.giudansky.com/images/downloads/blender/blender3d-shortcuts-infographic.png)

[> back to main Contents](#contents)
