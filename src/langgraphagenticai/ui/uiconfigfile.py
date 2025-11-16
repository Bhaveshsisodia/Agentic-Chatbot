from configparser import ConfigParser
import os
from src.langgraphagenticai.constant import UICONFIGFILENAME



class Config:
    def __init__(self):
        self.config = ConfigParser()
        path_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(path_dir,UICONFIGFILENAME)
        self.config_file = fr"{config_file_path}"
        self.config.read(self.config_file)

    def get_llm_options(self):
        return self.config['DEFAULT'].get('LLM_OPTIONS').split(', ')

    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS').split(', ')

    def get_groq_model_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS').split(', ')

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')



