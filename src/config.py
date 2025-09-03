import json
import os
import shutil as sh

import gradio as gr
import torch
import torchvision

SCRIPT_PATH = os.path.abspath(__file__)
SRC_DIR = os.path.dirname(SCRIPT_PATH)
ROOT_DIR = os.path.dirname(SRC_DIR)
SETTINGS_DIR = os.path.join(ROOT_DIR, "settings")

def save_config_gr(settings_debug_mode, settings_start_in_browser, settings_share_gradio, settings_clear_on_start, settings_use_proxy):
    settings = {
        "debug_mode": str(settings_debug_mode),
        "start_in_browser": str(settings_start_in_browser),
        "share_gradio": str(settings_share_gradio),
        "clear_on_start": str(settings_clear_on_start),
        "use_proxy": str(settings_use_proxy)
    }
    
    json_file = ""
    if "dev_config.json" in os.listdir(SETTINGS_DIR):
        json_file = "dev_config.json"
    elif "config.json" in os.listdir(SETTINGS_DIR):
        json_file = "config.json"
        
    json_file_path = os.path.join(SETTINGS_DIR, json_file)

    with open(json_file_path, 'w') as file:
        json.dump(settings, file, indent=4)
        
    settings_save_progress_toast = f"Settings saved to [{json_file_path}]. Restart GXAI!"
    settings_save_progress = "Done!"
    
    gr.Info(settings_save_progress_toast)
    
    return settings_save_progress

if "dev_config.json" in os.listdir(SETTINGS_DIR):
    with open(os.path.join(SETTINGS_DIR, "dev_config.json")) as json_file:
        data = json.load(json_file)
        print("dev_config.json loaded")
elif "config.json" in os.listdir(SETTINGS_DIR):
    with open(os.path.join(SETTINGS_DIR, "config.json")) as json_file:
        data = json.load(json_file)
        print("config.json loaded")

debug = data.get('debug_mode', 'False').lower() == 'true'
inbrowser = data.get('start_in_browser', 'False').lower() == 'true'
share_gradio = data.get('share_gradio', 'False').lower() == 'true'
clear_on_start = data.get('clear_on_start', 'False').lower() == 'true'
use_proxy = data.get('use_proxy', 'False').lower() == 'true'

if not (debug or inbrowser or share_gradio or clear_on_start or use_proxy):
    print("Something wrong in config.json. Check them out!")
    
cuda_version = torch.version.cuda
cudnn_version = torch.backends.cudnn.version()
torch_version = torch.__version__
torchvision_version = torchvision.__version__

def delete_tmp_pngs():
    output_dir = "tmp"
    try:
        rm_tmp = os.path.join(ROOT_DIR, output_dir)
        sh.rmtree(rm_tmp)
    except (PermissionError, FileNotFoundError, FileExistsError, Exception):
        pass
    
    tmp_file = "tmp.png"
    
    try:
        os.remove(os.path.join(ROOT_DIR, tmp_file))
    except FileNotFoundError as e:
        gr.Error(f"Error: {e}")
        pass

def clear_all():
    import gx
    gx.Upscaler_batch_Clear()
    gx.BgRemoverLite_Clear()
    gx.NSFWDetector_Clear()
    gx.VideoAnalyzerBatch_Clear()
    gx.AID_Clear()
    gx.tts_clear()
    gr.Info("All outputs cleared!")

def check_gpu():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
    try:
        if debug:
            gr.Info(f"Device: {device}")
            print(f"Allocated memory: {torch.cuda.memory_allocated()} bytes")
            print(f"Reserved memory: {torch.cuda.memory_reserved()} bytes")
            print("")
        if torch.cuda.is_available():
            gr.Info("CUDA available! Working on")
        elif not torch.cuda.is_available():
            gr.Warning("CUDA is not available, using CPU. Warning: this will be very slow!")
    except Exception as e:
        print(f"ERROR IN CHECK GPU: {e}")
    return device