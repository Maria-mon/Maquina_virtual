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
![image](https://github.com/user-attachments/assets/1e7aadae-1f78-4ffd-b236-5826c3de7c7c)

* Limpieza y guardado en base de datos
![image](https://github.com/user-attachments/assets/51d3e4d6-ff09-4328-ae13-f41325b342e6)

* Entrenamiento del modelo
![image](https://github.com/user-attachments/assets/c9f59172-70be-4a16-83b4-323077a1a2b4)
![image](https://github.com/user-attachments/assets/e63b5b7e-091d-45cf-9c0a-48b44fb113ea)
![image](https://github.com/user-attachments/assets/2faff578-bd8e-4545-bddc-3db37af6a75e)

* Guardado de mejor modelo
![image](https://github.com/user-attachments/assets/79183110-e6d8-4c65-b2da-26f876f02e02)
![image](https://github.com/user-attachments/assets/2526a68e-1aad-4254-8b6f-0c23c1a038c3)

* API
![image](https://github.com/user-attachments/assets/d78a817f-b327-4b6b-b9ea-51e63ee1f242)

Conclusiones

Este proyecto implementó un pipeline completo de MLOps, integrando gestión de datos, entrenamiento de modelos, tracking de experimentos y despliegue de modelos. Se lograron los siguientes objetivos:

✔ Datos cargados y procesados en PostgreSQL.
✔ Experimentación con 20 entrenamientos registrados en MLflow.
✔ Almacenamiento de modelos en MinIO.
✔ Implementación de FastAPI para servir predicciones en tiempo real.
✔ API funcional y accesible.

