Iniciar o projeto com Django

python -m venv venv
. venv\Scripts\activate
pip install django
django-admin startproject project .
criando app: python manage.py startapp 'nome do app'


COnifgurar o git 

'''

git config --global user.name 'NOME'
git config --global user.email 'EMAIL'
git config --global init.defaultBranch main 
CONFIGURE O .gitignore
git init
git add .
git commit -m 'Mensagem do ajuste'

Migrando a base de dados do Django

''' 
python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha de um super usuário Django

'''
python manage.py createsuperuser
python manage.py changepassword USERNAME


