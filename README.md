Implementación de un Pipeline de MLOps con MLflow, MinIO, PostgreSQL y FastAPI

MLOps - Maestría en Inteligencia Artificial

Integrantes: 
* Andres Gomez
* Juan Felipe Forero
* Maria del Mar Montenegro

Introducción

En este proyecto se implementó un pipeline completo de MLOps, desde la ingesta de datos hasta el despliegue de un modelo en producción mediante una API REST. La infraestructura utilizada incluye MLflow para la experimentación, MinIO como almacenamiento de artefactos, PostgreSQL como base de datos y FastAPI para la inferencia del modelo entrenado.

El objetivo del proyecto fue entrenar un modelo de clasificación basado en Logistic Regression para predecir el sexo de los pingüinos a partir de sus características morfológicas, utilizando el dataset penguins_size.

Arquitectura del Proyecto

El proyecto sigue una arquitectura modular con los siguientes componentes:

* Base de datos PostgreSQL: Almacena los datos originales y procesados.
Se accede desde JupyterLab mediante sqlalchemy y pandas.

* MLflow: Gestiona los experimentos.
Registra modelos en el Model Registry.
Se conecta con MinIO para almacenar los artefactos.

* MinIO:
Simula un bucket S3 para almacenar los modelos y otros artefactos.

* JupyterLab en Docker:
Se usa para la experimentación y entrenamiento del modelo.
Se ejecutan al menos 20 experimentos variando hiperparámetros.

* FastAPI:
Expone un endpoint para la inferencia del modelo en producción.
Carga el mejor modelo desde MLflow Model Registry.

* Docker:
Contiene los servicios de JupyterLab y MinIO.


Configuración del Entorno

Para la implementación, se utilizó una máquina virtual con Ubuntu 20.04. Se configuraron los siguientes servicios:

* PostgreSQL

imagen base de datos

CREATE USER mlflow WITH PASSWORD 'mlflow';
CREATE DATABASE mlflow_db OWNER mlflow;
ALTER ROLE mlflow SET client_encoding TO 'utf8';

* MinIO
docker run -p 9000:9000 -p 9001:9001 --name minio \
  -e "MINIO_ROOT_USER=admin" \
  -e "MINIO_ROOT_PASSWORD=supersecret" \
  -v $(pwd)/minio-data:/data \
  quay.io/minio/minio server /data --console-address ":9001"


Proceso

* Carga de datos
* Limpieza y guardado en base de datos
* Entrenamiento del modelo
* Guardado de mejor modelo
* API

Conclusiones

Este proyecto implementó un pipeline completo de MLOps, integrando gestión de datos, entrenamiento de modelos, tracking de experimentos y despliegue de modelos. Se lograron los siguientes objetivos:

✔ Datos cargados y procesados en PostgreSQL.
✔ Experimentación con 20 entrenamientos registrados en MLflow.
✔ Almacenamiento de modelos en MinIO.
✔ Implementación de FastAPI para servir predicciones en tiempo real.
✔ API funcional y accesible.

