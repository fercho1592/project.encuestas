# Encuestas
Sistema de encuestas para escuelas en SLP

## Justificacion
Uno de los grandes problemas en las escuelas hoy en día es la falta de tecnología. Gran parte de los procesos son hechos a lápiz y papel para luego leer uno por uno todos los documentos y poder obtener la información que necesitan.  Esto pasa muy seguido con las encuestas que se hacen, cada profesor crea su conjunto de preguntas y respuestas, imprimen con dinero de su bolsa cientos de hojas, para después pasarse una tarde tratando de entender que fue lo que pusieron los niños. La verdad es un trabajo largo, tedioso e innecesario.
Es por eso que se propuso crear un sistema para crear, aplicar cuestionarios y que permita obtener los datos para analizarlos posteriormente.

## Historias de usuario
Como...|Quiero...|Para...
-------|--------|--------
Profesor|Crear un nuevo cuestionario|...
Profesor|Modificar un cuestionario|Agregar o corregir elementos
Profesor|En cuanto escriba una pregunta se genere el espacio para escribir las respuestas|facilitar mi uso de la aplicacion
Profesor|En cuanto escriba una pregunta se genere un espacio para otra pregunta|no tener que picar un boton cada vez que quiera una nueva
Profesor|En cuanto termine de modificar un campo se guarde automaticamente en la base de datos|Hacer los cambios mas agilmente

## Virtual env
Action |CMD
-------|--------
Create env| `python3 -m venv .venv`
Activate|`source ./.venv/bin/activate`
Deactivate|`deactivate`

## Installation
```
pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r Requirements.txt
```
or
```
pip install -r Requirements.txt
```

## Run project
1. Start migration to create SQLite tables
    ```
    python ./src/manage.py migrate
    ```
2. Create a superuser
   ```
   python ./src/manage.py createsuperuser
   ```
3. Run server
    ```
    python ./src/manage.py runserver
    ```
4. Go to `http://127.0.0.1:8000/admin` and login with user created on first step



**Fernando Alvarez Flores** :
[@silver1592](https://github.com/silver1592) |
feral1592@gmail.com
