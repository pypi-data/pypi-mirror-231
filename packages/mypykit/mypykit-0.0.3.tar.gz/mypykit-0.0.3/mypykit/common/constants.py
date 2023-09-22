import os

TEMP_DIR = os.getenv('tmp')
if TEMP_DIR == None :
    TEMP_DIR = os.getenv('temp')
if TEMP_DIR == None :
    raise('임시 디렉토리를 수동으로 설정하세요.')
    