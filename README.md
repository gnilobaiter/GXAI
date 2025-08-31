## AIs
**1. BgRemoverLite**

**2. Image upscaler**

**3. Image Analyzer**

**4. Video Analyzer**

**5. Prompt Generator**

**6. AI Detector**

**7. TTS**

## System requirements
**1. Windows 10-11**

**2. NVIDIA GPU with CUDA 12.1 support**

**3. 16gb RAM**

**4. 8gb+ free SSD (NOT HDD) space**

**5. Python 3.10.0 or 3.10.11, other version will crash programm**

## Installation for Windows (recommended)
**1. Install [Winget](https://learn.microsoft.com/windows/package-manager/winget/#install-winget)**

**2. Install Python (3.10-3.11)**
```py
winget install -e --id Python.Python.3.10
```
**3. Install Git**
```py
winget install -e --id Git.Git
```

**4. Clone repository**
```git
git clone https://github.com/gnilobaiter/GXAI.git
```
**5. Run *install.bat* for first time. Next time run *run.bat***

## Installation for Windows (legacy)
**1. Install [Python (3.10-3.11)](https://www.python.org/downloads/)**

**2. Install [Git](https://git-scm.com/downloads)**

**3. Download using "Code --> Download ZIP"** ([or click here](https://github.com/gnilobaiter/GXAI/archive/refs/heads/main.zip))

**4. Unarchive ZIP**

**5. Run *install.bat* for first time. Next time run *run.bat***

## Settings tab (recommended)
**You don't have to go into config.json and change something with your hands. This tab will do everything for you!**
1. Choose necessary checkboxes
2. Press *Save settings*
3. Restart **GXAI**

## Settings (legacy, ../settings/config.json)
```js
    {
        "debug_mode": "True", 
        // Boolean ("True" or "False")
        // Enable debug mode (write debug info)
        // Enable logging
        
        "start_in_browser": "True",
        // Boolean ("True" or "False")
        // Enable GXAI starting in browser

        "share_gradio": "False",
        // Boolean ("True" or "False")
        // Enable GXAI starting with share link

        "clear_on_start": "False",
        // Boolean ("True" or "False")
        // Clear all outputs on start

        "use_proxy": "False"
        // Boolean ("True" or "False")
        // Using system proxy to use WebUI
    }
```

## Support
1. If you see errors like this: ```ModuleNotFoundError: No module named "certifi"```, run install.bat for fix them. If that didn't help, open a new issue
2. If you encounter errors during the execution of the program, open a new issue
3. If your console window freezes during the install process.bat, restart it with administrator rights. It is also highly recommended to run run.bat from the administrator.

## Credits
- Built with **Gradio** - https://www.gradio.app/
- Using **u2net model** for *BgRemoverLite* - https://github.com/xuebinqin/U-2-Net
- **RemBG** library for *BgRemoverLite* - https://github.com/danielgatis/rembg
- **NSFW Detection** - https://github.com/GantMan/nsfw_model
- **NSFW Detection 2.0** - https://huggingface.co/Falconsai/nsfw_image_detection 
- **Upscaling** - https://github.com/kmewhort/upscalers
- **Clip-interrogator** for *Image Analyzer* - https://github.com/pharmapsychotic/clip-interrogator
- **Fast Prompt Generator** - https://huggingface.co/FredZhang7/anime-anything-promptgen-v2
- **H5 Keras Model** - trained by me
- **Silero TTS** - https://github.com/snakers4/silero-models
## License
MIT license | Copyright (c) 2025 gnilobaiter
