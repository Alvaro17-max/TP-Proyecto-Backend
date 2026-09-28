#  Sistema de Gestión - Club Deportivo Backend

Este es el repositorio de backend para la gestión de un **Club Deportivo**, desarrollado en **Python** utilizando el framework **Flask** y una base de datos **MySQL 8** contenerizada.

## Integrantes del Grupo
* Alvaro Ricardo Avalos Aguilar - 114565 
Juan Pablo Tacunan Navarro - 112500 
Kayl Omar Ponce Enciso. - 116317 
Smith Junior Montes Solorzano - 114434
Julian Joel Cansino -116419

---

## Requisitos Previos

Para ejecutar este proyecto localmente de forma correcta, se requiere contar con las siguientes herramientas instaladas en el sistema operativo (**Entorno Linux/WSL recomendado**):

* **Python 3.10+** y `pip`
* **Docker** y **Docker Compose**
* Un cliente API como **Postman** o un navegador web para pruebas.

---

## Pasos para Ejecutar el Proyecto Localmente

Siga estas instrucciones en orden desde su terminal de Linux para poner en marcha el servidor y la base de datos:

### 1. Inicializar la Base de Datos con Docker
El proyecto incluye un archivo `docker-compose.yml` que levanta de forma automatizada un contenedor con MySQL 8 e importa la estructura inicial del archivo `init_db.sql`.

En la raíz del proyecto, ejecute:
```bash
sudo docker-compose up -d
```
*Nota: Si el puerto `3306` se encuentra ocupado por un servicio MySQL local nativo, se recomienda apagarlo temporalmente ejecutando `sudo systemctl stop mysql` antes de levantar el contenedor.*

### 2. Configurar el Entorno Virtual de Python
Aísle las dependencias del proyecto creando y activando un entorno virtual (`venv`):

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 3. Instalar Dependencias del Servidor
Con el entorno virtual activo (verá el prefijo `(venv)` en su terminal), instale los paquetes requeridos por la API:
```bash
pip install -r requirements.txt
pip install python-dotenv
```

### 4. Configurar Variables de Entorno (`.env`)
Asegúrese de que el proyecto cuente con un archivo `.env` en la raíz con las credenciales exactas del contenedor de datos:
```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root_password
DB_NAME=club_deportivo
```

### 5. Iniciar el Servidor Backend (Flask)
Finalmente, ponga en marcha la aplicación ejecutando el script principal:
```bash
python3 app.py
```
El servidor quedará activo y escuchando peticiones en **`http://127.0.0.1:5000`**.

---

## 🧪 Pruebas de Endpoints Disponibles (API REST)

Una vez encendido el sistema, puede consumir los servicios directamente utilizando herramientas como **Postman** o desde el propio navegador web apuntando a las siguientes rutas:

* **Módulo de Socios:** `GET http://127.0.0`
* **Módulo de Canchas:** `GET http://127.0.0`
* **Módulo de Reservas:** `GET http://127.0.0`
