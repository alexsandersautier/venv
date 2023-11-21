import sys
import os
from cx_Freeze import setup, Executable

arquivos = ['settings.json','mensagem1.txt']
configuracao = Executable(
    script='main.py',
    icon='logo.ico'
)

setup(
    name='Automatizador de programar postagem',
    version='1.0',
    description='Este programa automatizar o processo de agendamento de postagens',
    author='Alexsander Sauter',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)