# Timesheet

Si otra app para contar la cantidad de horas invertidas en un proyecto.

## Requisitos

- Python 3.6+
- PostgreSQL

## Instalación

Dentro del proyecto hay un archivo `Makefile` si tiene **cmake** ejecute desde la shell

    make iniciar 
    
Requiere tener instalado **pipenv**

    sudo apt install python3-pip
    pip install pipenv
    
## Configuración local

Crear una base de datos en postgres llamada **timesheet** o ejecutar los siguiente comando.

    make reset
    make migrar

   