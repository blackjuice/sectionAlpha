# Windows 8.1

## USB ports keep disconnecting and reconnecting [(source)](http://www.tomshardware.com/answers/id-1783536/usb-ports-disconnecting-reconnecting.html)

1. Scroll to the right and type 'Power Options' in the search field and click on it.
2. Click 'Change plan setting' on your chosen plan.
3. Click 'Change advanced power setting' on your chosen plan.
4. Find 'USB settings' and open.
5. Find 'USB selective suspend setting' and change it to disabled.

## explorer.exe. application Error

### Message:

The instruction at 0x1b7f3e01 referenced memory at 0x00000000. The memory could not be read. Click on OK to terminate the program.

### solving 0x00000000 memory unreadable

To change the DEP settings, choose Start > Control Panel > System > Advance > Performance Settings > Data Execution Prevention.

http://www.tomshardware.com/forum/263457-45-instruction-0x7c910b2c-referenced-memory-0x00000000-memory

https://social.technet.microsoft.com/Forums/en-US/c7b7e17f-a54a-4532-a57f-d1c569f15d9d/explorer-exe-application-error-it-says-the-instruction-at-0xf6628a87-referenced-memory-at?forum=winservermanager

Run Dell Diagnostics PSA/ePSA outside of Windows. Run long memory test: http://en.community.dell.com/owners-club/alienware/f/3746/t/19609415

## Scree Tearing

Card: AMD Radeon HD 7800 Series (Club 3D HD 7870 XT jokerCard)

https://us.battle.net/forums/en/overwatch/topic/20755046243

* Fast sync: OFF
* FreeSync: OFF

Settings_v0.ini

        [Render.13]
        AADetail = "0"
        CpuForceSyncEnabled = "1"
        DirectionalShadowDetail = "1"
        DynamicAmbient = "0"
        EffectsQuality = "1"
        FrameRateCap = "300"
        FullScreenHeight = "800"
        FullScreenRefresh = "120"
        FullScreenWidth = "1280"
        FullscreenWindow = "1"
        FullscreenWindowEnabled = "1"
        GFXPresetLevel = "1"
        LimitAspectRatio = "0"
        LimitTo30 = "0"
        LimitToRefresh = "0"
        LocalFogDetail = "1"
        LocalReflections = "0"
        MaxAnisotropy = "1"
        MaxEffectsAnisotropy = "1"
        MaxExtraQualityAnisotropy = "1"
        MaximizedWindow = "0"
        RefractionDetail = "0"
        RenderBrightness = "0.000000"
        RenderContrast = "1.000000"
        RenderScale = "-5"
        ShowFPSCounter = "1"
        ShowGPUTemp = "1"

Copy, replace [Render.13] in Settings_v0.ini. Then set up resolution, aspect ratio, render etc as u wish.