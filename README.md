# TTM Mexico Website

### Requerimientos 📋
- Python 3
- Node.js
- Red Funcional

## Objetivo 🎯
Desarrollar una plataforma integral de gestión de infraestructuras de redes que aproveche las capacidades de Django, React, Python y bases de datos, integrando la librería Netmiko para facilitar la gestión y configuración de dispositivos de red, proporcionando a los usuarios una experiencia completa y eficiente en la administración y monitoreo de redes.

## Build 🛠️
Antes que nada, debemos de asegurarnos de estar conectados a una red LAN con dispositivos configurados con acceso SSH, ips por puertos y algunas configuraciones basicas.
Debemos tener conexion y acceso a todos los dispositivos para que la pagina web pueda funcionar de manera adecuada.

## Set up de Python 🐍
Para poder correr el proyecto de manera local, debemos de comprobar la version de Python de nuestro sistema. Regularmente los sistemas operativos MACOS y Linux ya cuentan con una version de Python instalada.

Vamos a comprobar que la version de Python sea la 3.9.0 o mayor a esta:

`python3`

En dado caso de que no este instalado, tendremos que instalar la version adecuada.

## Clonar repositorio 📂

La forma mas sencilla de clonar el repositorio es accediendo a la ventana de comandos, colocarnos en cualquier lugar donde queramos almacenar el repositorio.
Clonar el repositorio:

`git clone https://github.com/fabrizzioRios/TTM-Mexico-R4`

Con esto ya tendrias el repositorio descargado directamente a tu computadora.

## Set up del backend

Dentro del directorio deberemos de entrar al proyecto de Django. Ahi esta almacenada toda la logica de programacion y la parte del backend.

`cd icart_backend`

Necesitaremos descargar las librerias necesarias para el funcionamiento del proyecto. Con el archivo requirements.txt podemos instalar de manera rapida las librerias y dependencias utilizadas.

El siguiente comando ayuda a instalar todo directamente en el lugar donde este almacenado el repositorio ya clonado.

`pip install -r requirements.txt`

Despues se debera de correr el servidor de django mediante el siguiente comando.

`python manage.py runserver`

Este comando iniciará el servidor de desarrollo de Django en tu máquina local. Se podra acceder a la aplicación a través de la dirección proporcionada en la consola (Tiene que ser http://127.0.0.1:8000/).


## Set up del frontend

Dentro del directorio deberemos de entrar al proyecto de ReactJX. Ahi esta almacenada toda la logica de programacion y la parte del frontend.

`cd icart_backend`

Ejecutamos este comando para descargar todas las dependencias de Javascript que se utilizaron en el proyecto.

`npm install`

Dentro se debera de correr el servidor de ReactJX mediante el siguiente comando.

`npm start`

Este comando iniciará el servidor de desarrollo de ReactJX en tu máquina local. Se podra acceder a la aplicación a través de la dirección proporcionada en la consola (Tiene que ser http://localhost:3000/).


## Uso del sitio

Ambos procesos deberan de estar corriendo de forma adecuada.

Se debera acceder a la siguiente url http://localhost:3000/Admin

Ahi se debera usar el usuario administrador para iniciar sesion y acceder a la pagina:

Email: `network_admin@ttm.mexico.com`
Contraseña: `TTMM3x1c0@.`

Y listo, el proyecto debera de ser funcional y podra ser editado y configurado de manera que se adapte a la red donde se necesite ser usado.
