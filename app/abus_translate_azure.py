import gradio as gr
import pysubs2
import re


import os, requests, uuid, json
from azure.core.exceptions import HttpResponseError
try:
    from azure.ai.translation.text import TextTranslationClient
except ImportError:
    TextTranslationClient = None

try:
    from azure.ai.translation.text import TranslatorCredential
except ImportError:
    try:
        from azure.ai.translation.text._patch import TranslatorCredential
    except ImportError:
        TranslatorCredential = None

from app.abus_genuine import *
from app.abus_path import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_config import (
    get_azure_translator_key,
    get_azure_translator_endpoint,
    get_azure_translator_region
)

import structlog
logger = structlog.get_logger()



class AzureTranslator:
    def __init__(self) -> None:
        self.apikey = get_azure_translator_key()
        self.endpoint = get_azure_translator_endpoint()
        self.region = get_azure_translator_region()
        self.text_translator = None
        self.native_names = []
        self.language_names = []
        self.languages_dict = {}

        if TextTranslationClient is not None and TranslatorCredential is not None:
            try:
                credential = TranslatorCredential(self.apikey, self.region)
                self.text_translator = TextTranslationClient(credential=credential, endpoint=self.endpoint)
            except Exception as exception:
                logger.warning(f"[abus_translate_azure.py] Azure SDK client unavailable, falling back to REST API: {exception}")
        else:
            logger.warning("[abus_translate_azure.py] Azure Translator SDK credential is unavailable, falling back to REST API.")
        
        self._load_languages()

    def _load_languages(self):
        try:
            if self.text_translator is not None:
                response = self.text_translator.get_languages()
                if response.translation is not None:
                    self._set_languages(response.translation)
                    return

            response = requests.get(
                self._rest_url('/languages'),
                params={'api-version': '3.0', 'scope': 'translation'},
                timeout=20,
            )
            response.raise_for_status()
            self._set_languages(response.json().get('translation', {}))
        except HttpResponseError as exception:
            if exception.error is not None:
                logger.error(f"Translation : {exception.error.message} ({exception.error.code})")
        except Exception as exception:
            logger.error(f"[abus_translate_azure.py] _load_languages - error: {exception}")

    def _set_languages(self, languages_dict):
        self.languages_dict = languages_dict
        self.native_names = []
        self.language_names = []
        for value in languages_dict.values():
            native_name = self._language_attr(value, 'native_name')
            name = self._language_attr(value, 'name')
            if native_name:
                self.native_names.append(native_name)
            if name:
                self.language_names.append(name)

    def _language_attr(self, value, attr):
        if isinstance(value, dict):
            return value.get(attr) or value.get('nativeName' if attr == 'native_name' else attr)
        return getattr(value, attr, None)

    def _rest_url(self, path):
        endpoint = self.endpoint.rstrip('/')
        if 'cognitiveservices' in endpoint and '/translator/text/v' not in endpoint:
            endpoint = f'{endpoint}/translator/text/v3.0'
        return f'{endpoint}{path}'
            
    
    def get_languages(self) -> list:
        # return self.native_names
        return self.language_names
    
    def get_language_code(self, language_name) -> str:
        search_name = language_name.lower()
        for key, value in self.languages_dict.items():
            name = self._language_attr(value, 'name')
            native_name = self._language_attr(value, 'native_name')
            if (name and name.lower() == search_name) or (native_name and native_name.lower() == search_name):
                return key
        return "en"
    
    def get_language_value(self, language_name):
        search_name = language_name.lower()
        for key, value in self.languages_dict.items():
            name = self._language_attr(value, 'name')
            native_name = self._language_attr(value, 'native_name')
            if (name and name.lower() == search_name) or (native_name and native_name.lower() == search_name):
                return name
        return None
           

    def request_translate(self, source_lang: str, target_lang: str, text: str) -> str:
        if self.text_translator is None:
            return self.translate_text_webapi(source_lang, target_lang, text)

        try:
            azure_source = self.get_language_code(source_lang)            
            azure_target = self.get_language_code(target_lang)            
            body = [{'text': text}]

            response = self.text_translator.translate(
                content=body, to=[azure_target], from_parameter=azure_source
            )
            translation = response[0] if response else None

            if translation:
                for translated_text in translation.translations:
                    logger.debug(f"[abus_translate_azure.py] request_translate - Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")
                    return translated_text.text
            return "Error"

        except HttpResponseError as exception:
            if exception.error is not None:
                logger.error(f"request_translate : {exception.error.message} ({exception.error.code})")
            return "Error"


    def translate_text(self, source_lang: str, target_lang: str, text: str, progress=gr.Progress()) -> str:
       
        # line 끝 마침표 확인인
        use_punctuation = AbusText.has_ending_marks([text])
                  
        # 텍스트를 문장 단위로 분리
        sentences = AbusText.split_into_sentences(text, use_punctuation)
        sentences = sentences
        
        translated_sentences = []
        
        # 각 문장을 번역
        for sentence in progress.tqdm(sentences, desc="Translating sentences..."):
            try:
                translated = self.request_translate(source_lang, target_lang, sentence)
                translated_sentences.append(translated)
                logger.debug(f"[abus_translate_azure.py] translate_text - {source_lang}: {sentence} -> {target_lang}: {translated}")
            except Exception as e:
                logger.error(f"Translation error: {e}")
                translated_sentences.append(sentence)  # 에러 발생 시 원본 문장 사용
        
        # 번역된 문장들을 다시 하나의 텍스트로 결합
        final_text = ' '.join(translated_sentences)
        return final_text
    

    def translate_file(self, source_lang: str, target_lang: str, subtitle_file_path: str, output_file_path: str, progress=gr.Progress()):
        tts_source_file = path_add_postfix(subtitle_file_path, f"-{source_lang}", ".srt")
        
        # AbusText.process_subtitle_for_tts(subtitle_file_path, tts_source_file)
        AbusSpacy.process_subtitle_for_tts(subtitle_file_path, tts_source_file)
        
        # Load subtitles using pysubs2
        full_subs = pysubs2.load(tts_source_file)
        subs = full_subs
        
        # 구두점이 없는 언어의 경우 각 자막을 개별적으로 번역
        for event in progress.tqdm(subs, desc='Translate...'):
            if not event.text:
                continue
                
            text = event.plaintext
            try:
                translated_text = self.request_translate(source_lang, target_lang, text)
                if translated_text:
                    event.text = translated_text
                    logger.debug(f"[abus_translate_azure.py] translate_file : text       - {text}")
                    logger.debug(f"[abus_translate_azure.py] translate_file : translated - {translated_text}")                        
                else:
                    logger.warning(f"[abus_translate_azure.py] translate_file - Empty translation for: {text}")
            except Exception as e:
                logger.error(f"Translation error for text '{text}': {e}")
                # 에러 발생 시 원본 텍스트 유지

        # Save the translated subtitles
        subs.save(output_file_path)     
        cmd_delete_file(tts_source_file)  

       
    
    def translate_text_webapi(self, source_lang: str, target_lang: str, text: str) -> str:
        azure_source = self.get_language_code(source_lang)
        logger.debug(f'azure_source = {azure_source}')
        
        azure_target = self.get_language_code(target_lang)
        logger.debug(f'azure_target = {azure_target}')
        
        params = {
            'api-version': '3.0',
            'from': azure_source,
            'to': azure_target
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.apikey,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]


        try:
            response = requests.post(self._rest_url('/translate'), params=params, headers=headers, json=body)
            response_data = response.json()
            # logger.debug(f'==> response_data = {response_data}')
            # logger.debug(f'==> response.status_code = {response.status_code}')
            
            if response.status_code == 200:
                translations = response_data[0]['translations']
                first_translation = translations[0]
                translated_text = first_translation['text']
                return translated_text
            else:
                error = response_data['error']
                # error_msg = f'translate_text_webapi : {error["message"]} ({error["code"]})'
                return error["message"]
        except:
            return "Error"
            
        
