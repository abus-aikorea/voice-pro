import os
from pathlib import Path
from huggingface_hub import hf_hub_download
import zipfile
import shutil

import structlog
logger = structlog.get_logger()


# Environment
script_dir = os.getcwd()
conda_env_path = os.path.join(script_dir, "installer_files", "env")
app_model_path = os.path.join(script_dir, "model")

class HF_Model():
    def __init__(self, repo_id, file_type, file_name, file_size, level, display_name: str = ""):
        self.repo_id = repo_id
        self.file_type = file_type        
        self.file_name = file_name
        self.file_size = file_size
        self.level = level
        self.display_name = display_name if display_name != "" else os.path.splitext(file_name)[0]

    def __str__(self):
        return f'HFModel(repo_id={self.repo_id}, file_name={self.file_name}, file_size={self.file_size}, file_type={self.file_type}, level={self.level})'
    
    def download_info(self):
        mega_bytes = self.file_size / 1024**2
        return f'{self.file_name} : {mega_bytes: .2f} MB'
    
    def has_local_file(self):
        file_path = os.path.join(app_model_path, self.file_type, self.file_name)
        if os.path.exists(file_path):
            if os.path.getsize(file_path) == self.file_size:
                logger.debug(f'has_local_file - OK : {file_path}')    
                return True
        return False
    
    def download(self):
        try:
            logger.warning(f'start download : {self.file_name}')            
            cache_dir = os.path.join(Path.home(), ".cache", "huggingface", "hub")
            hf_download_path = hf_hub_download(repo_id=self.repo_id, filename=self.file_name, cache_dir=cache_dir)
            
            download_folder = os.path.join(app_model_path, self.file_type)
            if not os.path.exists(download_folder):
                os.mkdir(download_folder)

            download_file_path = os.path.join(download_folder, self.file_name)
            shutil.copy(hf_download_path, download_file_path)
            logger.warning(f'download complete : {download_file_path}')    
            
            _, extension = os.path.splitext(download_file_path)
            if extension.lower() == '.zip':
                self.unzip(make_folder=(self.file_type=='rvc-voice'))
            return True
        except:
            return False   
        
    def unzip(self, make_folder: bool = False):
        zip_path = os.path.join(app_model_path, self.file_type, self.file_name)
        extract_to = os.path.dirname(zip_path)
        logger.debug(f'unzip: {zip_path}')        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_contents = zip_ref.namelist()
                logger.debug(f'zip_contents: {zip_contents}')
                
                if not os.path.exists(extract_to):
                    os.makedirs(extract_to)
                
                if '/' in zip_contents[0]:
                    zip_ref.extractall(extract_to)
                else:
                    if make_folder:
                        folder_name = os.path.splitext(os.path.basename(zip_path))[0]
                        extract_to = os.path.join(extract_to, folder_name)
                        if not os.path.exists(extract_to):
                            os.makedirs(extract_to)
                    zip_ref.extractall(extract_to)
            return True
        except:
            return False  
    
    
HF_MODELS = [
    HF_Model('ABUS-AI/AICover-v0.1', 'rvc-model', 'rmvpe.pt', 181184272, 0),           # level 0
    HF_Model('ABUS-AI/AICover-v0.1', 'rvc-model', 'hubert_base.pt', 189507909, 0),     # level 0
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_a_bass.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_a_drums.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_a_vocals.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_a_other.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_b_bass.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_b_drums.onnx', 21930313, 1),    
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_b_vocals.onnx', 29703204, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'kuielab_b_other.onnx', 29703204 , 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_1_9703.onnx', 29704436, 1, 'UVR-MDX-NET 1'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_2_9682.onnx', 29704436, 1, 'UVR-MDX-NET 2'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_3_9662.onnx', 29704436, 1, 'UVR-MDX-NET 3'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_9482.onnx', 29704436, 1),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_KARA.onnx', 29704436, 1, 'UVR-MDX-NET Karaoke'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_KARA_2.onnx', 52786726, 0, 'UVR-MDX-NET Karaoke 2'),  # level 0
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_Main.onnx', 52786726, 1, 'UVR-MDX-NET Inst Main'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET_Crowd_HQ_1.onnx', 59074342, 1, 'UVR-MDX-NET Crowd HQ 1'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'Kim_Inst.onnx', 66759214, 1, 'Kim Inst'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'Kim_Vocal_1.onnx', 66759214, 1, 'Kim Vocal 1'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'Kim_Vocal_2.onnx', 66759214, 1, 'Kim Vocal 2'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR_MDXNET_Main.onnx', 66759214, 1, 'UVR-MDX-NET Main'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_1.onnx', 66759214, 1, 'UVR-MDX-NET Inst 1'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_2.onnx', 66759214, 1, 'UVR-MDX-NET Inst 2'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_3.onnx', 66759214, 1, 'UVR-MDX-NET Inst 3'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_HQ_1.onnx', 66759214, 1, 'UVR-MDX-NET Inst HQ 1'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_HQ_2.onnx', 66759214, 1, 'UVR-MDX-NET Inst HQ 2'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_HQ_3.onnx', 66759214, 1, 'UVR-MDX-NET Inst HQ 3'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Inst_HQ_4.onnx', 59074342, 1, 'UVR-MDX-NET Inst HQ 4'),
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'UVR-MDX-NET-Voc_FT.onnx', 66762490, 0),      # level 0
    HF_Model('ABUS-AI/AICover-v0.1', 'mdxnet-model', 'Reverb_HQ_By_FoxJoy.onnx', 66780123, 0, 'Reverb HQ (FoxJoy)'),   # level 0    
    HF_Model('ABUS-AI/AICover-v0.1', 'demucs', '955717e8-8726e21a.th', 84141911, 0, 'htdemucs'),        # level 0
    HF_Model('ABUS-AI/AICover-v0.1', 'demucs', '5c90dfd2-34c22ccb.th', 54996327, 1, 'htdemucs_6s'),
    HF_Model('ABUS-AI/AICover-v0.1', 'demucs', 'htdemucs_ft.zip', 311843957, 1, 'htdemucs_ft'),
    HF_Model('ABUS-AI/AICover-v0.1', 'demucs', 'mdx_extra.zip', 579915263, 1, 'mdx_extra'),        
    HF_Model('phant0m4r/LiSA', 'rvc-voice', 'LiSA.zip', 263711433, 0),        # level 0
    HF_Model('pjesek/AdoRVCv2', 'rvc-voice', 'AdoRVCv2.zip', 330871899, 0),   # level 0
]


def hf_all_display_names():
    """Return a list of hf model names."""
    return [hf_model.display_name for hf_model in HF_MODELS]


def hf_download_all_models():
    os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = 'True'
    for hf_model in HF_MODELS:
        if hf_model.has_local_file():
            continue
        hf_model.download()
        
def hf_download_models(file_type: str, level : int):
    os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = 'True'
    for hf_model in HF_MODELS:
        if hf_model.level > level:
            continue
        if hf_model.file_type != file_type:
            continue
        
        if hf_model.has_local_file():
            continue
        hf_model.download()    
        

def hf_get_from_name(display_name: str) -> HF_Model:
    hf_model = next((model for model in HF_MODELS if model.display_name == display_name), None)
    return hf_model

def hf_display_names(file_types, max_level):
    results = []
    
    for hf_model in HF_MODELS:
        if hf_model.file_type in file_types:
            if hf_model.level <= max_level:
                results.append(hf_model)
    return results

def hf_demixing_names(has_local_file: bool):
    results = []
    for model in HF_MODELS:
        logger.debug(f'hf_demixing_names: model = {model}')
        if model.file_type == 'mdxnet-model' or model.file_type == 'demucs':
            if has_local_file == model.has_local_file():
                results.append(model.display_name)
    return results
   