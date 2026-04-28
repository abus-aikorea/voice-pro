from concurrent.futures import ProcessPoolExecutor, as_completed
from src.config import UserConfig

from app.abus_path import *
from app.abus_translate_deep import *
from app.abus_translate_azure import *
# from app.abus_live import *
from app.abus_genuine import *

import pysubs2

from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioTranslate:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config

        self.translator = AzureTranslator() if azure_text_api_working() == True else DeepTranslator()

            
    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    

    def gradio_translate_languages(self) -> list:
        return self.translator.get_languages()                        
    
    def gradio_upload_file(self, file_obj):
        if file_obj is not None:
            text = self._read_file(gradio_file_path(file_obj))
            languageName = AbusText.detect_language_name(text[:200])
            return languageName, text
        return "English", "No file uploaded"   
 

    def gradio_save(self, file_obj, source_lang, target_lang, src_text, target_text):
        logger.debug(f'[GradioTranslate] gradio_save')
        message = i18n("Saving files...")
        gr.Info(message)
        
        if file_obj is not None:
            source_file = cmd_copy_file_to(gradio_file_path(file_obj), path_workspace_subfolder(gradio_file_path(file_obj)))
            source_text_file = path_add_postfix(source_file, f'translate-{time.time()}-{source_lang}.txt')   
            target_text_file = path_add_postfix(source_file, f'translate-{time.time()}-{target_lang}.txt')  
        
            self._write_file(source_text_file, src_text)
            self._write_file(target_text_file, target_text)
        else:
            source_text_file = os.path.join(path_translate_folder(), f'translate-{time.time()}-{source_lang}.txt')   
            target_text_file = os.path.join(path_translate_folder(), f'translate-{time.time()}-{target_lang}.txt')  
            
            self._write_file(source_text_file, src_text)
            self._write_file(target_text_file, target_text)
                        

    def gradio_translate(self, text: str, source_lang, target_lang):
        self.user_config.set("translate_source_language", source_lang)
        self.user_config.set("translate_target_language", target_lang)
        
        if not (text and text.strip()):
            message = i18n("Input error")
            gr.Warning(message)
            return None, None
        
        if len(source_lang.strip()) <= 0:
            source_lang = AbusText.detect_language_name(text[:200])          
        
        input_text = text
        logger.debug(f"[gradio_translate.py] gradio_translate - input_text: {input_text}")    
        
        subtitle_file = None
        if self._is_subtitle_format(input_text):
            subs = pysubs2.SSAFile.from_string(input_text)
            subtitle_file = os.path.join(path_translate_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)

        if subtitle_file:    
            translated_file = self._translate_subtitle(subtitle_file, source_lang, target_lang)
            return translated_file, self._read_file(translated_file)
        else:
            translated_text = self._translate_text(input_text, source_lang, target_lang)
            return None, translated_text


    def _is_subtitle_format(self, text):
        try:
            pysubs2.SSAFile.from_string(text)
            return True
        except Exception as e:
            return False   

    def _read_file(self, filepath):    
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except UnicodeDecodeError:
            return "Error: The file is not a valid text file or uses an unsupported encoding."
        except IOError:
            return "Error: Unable to read the file."

    def _write_file(self, filepath, content):
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
        except IOError:
            return "Error: Unable to read the file."        

    def _translate_subtitle(self, subtitle_file, source_lang, target_lang):
        try:
            translated_file = path_add_postfix(subtitle_file, f"_{target_lang}")
            self.translator.translate_file(source_lang, target_lang, subtitle_file, translated_file)
            return translated_file
        except Exception as e:
            logger.error(f"[gradio_translate.py] _translate_subtitle : {e}")
            gr.Warning(f'{e}')
            return None           

    def _translate_text(self, text, source_lang, target_lang):
        try:
            translated = self.translator.translate_text(source_lang, target_lang, text)
            return translated   
        except Exception as e:
            logger.error(f"[gradio_translate.py] _translate_text : {e}")
            gr.Warning(f'{e}')
            return None            
            

