
#intala o ambiente
python -m venv minhavenv

minhavenv\Scripts\activate

Se tiver problemas de acesso não autorizado, execute: Set-ExecutionPolicy Unrestricted -Scope Process 

#ativaçao do ambiente
.\activate.ps1

#instalar dentro do virtual machine
pip install flask
pip install Flask-Restful

#instalar tudo
pip install -r requirement.txt


