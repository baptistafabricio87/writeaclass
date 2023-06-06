# Write a Class

Passos para rodar o projeto.

Necessário ter python 3.10+ instalado

1. Acesse a pasta do projeto:

```cmd
cd writeaclass
```

2. Crie um ambiente virtual:

```cmd
python -m venv .venv
```

3. Ative o ambiente virtual:

	* Windows:
	```cmd
	.venv\Scripts\activate
	```

	* Linux:
	```cmd
	source .venv\bin\activate
	```

4. Instalar as dependencias do projeto 'requirements.txt':

```cmd
pip install -r requirements.txt
```

4. Subir servidor django

```cmd
python manage.py runserver
```
