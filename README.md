# QR API

## Descripción

API creada con lenguaje de porgramacion python usando la libreria Flask, para la generacionde codigos QR para la identificación de diferentes establecimientos, como lo pueden ser edificios de oficinas, universidades, centros comerciales, locales comerciales, centros turisticos entre otros. Adicionalmente la api permite registrar todas las personas que leen por medio de sus smartphone los codigos QR generados. estos datos son guardados en una base de datos posgrestql.

Adicionalmente el presente repositorio cuenta con el codigo de una aplicacion movil desarrollada en android studio que consta de un formulario que permite adquirir los datos basicos del estado de los usuarios, posterior a esto permite escanear los codigos QR generados a travez de la API y por medio  de app enviarla informacion del formulario y el registro de lectura del QR a la base de datos.

Estos codigos se desarrollaron para ser utlizados en el contexto de la pandemia COVID-19 con una alternativa al control y registro de ocupacion en los diferentes lugares de la ciudades con el fin de poder generar datos de utidad para los procesos de analisis de datos y toma de desiciones.

![Explanations Image](https://github.com/davidluna-fn/QR_api/blob/master/esquema%20de%20funcionamiento.png)

## Instalacion y configuracion

### Configuracion de la API

El primero paso para la instalacion es clonar este repositorio o descargarlo desde la interfaz web

```
git clone https://github.com/davidluna-fn/QR_api
```

el segundo paso requiere la instalacion de pgAdmin y posgrestql para la gestion y manejo de las base de datos a utilizar en para guardar la informacio. Para descargarlo entrar al siguiente enlace https://www.postgresql.org/download/ y seleccionar la opcion necesaria para nuestro equipo. Posterior a esto ejecutar el instalador, aceptar los permisos requeridos y continuar con la instalacion. Al ejecutar por primera vez el programa requiere una contraseña de usuario.

Despues de esto se debe crear una base de datos con el nombre de ubicaciones. Posteriormente se configurar la variable SQLALCHEMY_DATABASE_URI del archivo config.py en la carpeta /ubicaciones-restapi, dicha variable debe quedar con una configuracion del siguiente estilo 'postgresql://usuario:constraseña@direccion_de_la_db'

para ejecutar la API se debe instalar los requerimientos con el siguiente comando:

```
pip install -r requirements.txt
```

por ultimo esl siguiente paso es ejecutar el servidor con el siguiente comando:
```
python app.py 
```

### Configuracion app movil 

El proyecto de la app movil requiere el uso de android studio es cual se puede descargar desde el siguiente enlace https://developer.android.com/studio?hl=es-419 y se realiza la configuracion por defecto del instalador.
Al ejecutar el programa se debe cargar el proyecto seleccionando la carpeta LectorQR y despues se debe configurar la ruta del servidor donde esta corriendo la API y por ultimo compilar el proyecto e instalarlo en el celular.

## Rutas de la API

- '/api/v1/ubicaciones/', methods=['POST'] registra la posicion de un usuario en un punto especifico donde realiza la lectura del codigo QR. 
parametros requeridos:
  - id_place : se adquiere automaticamente del codigo QR leido por la aplicación.
  - id_device : se adquiere automaticamente por la app como identificador del dispositivo movil utilizado.
  - phone: se adquiere del formulario que se llena al usar la app para escanear un codigo.
  - form1: respuesta a la pregunta 1 del formulario que se llena al usar la app para escanear un codigo.
  - form2: respuesta a la pregunta 2 del formulario que se llena al usar la app para escanear un codigo.
  - form3: respuesta a la pregunta 3 del formulario que se llena al usar la app para escanear un codigo.

- '/api/v1/ubicaciones', methods=['GET'] : devuelve todos los registros de usuarios que por medio de la aplicacion han leido el codigo QR en determinada ubicacion, en formato json.

- '/api/v1/qrcode/<filename>', methods=['GET'] : devuelve un codigo codigo QR especifico correspondiente al id suministrado  con la informacion suministrada para el registro de locales en la ciudad.
  
- '/api/v1/qrcode/', methods=['POST']: devuelve el codigo QR generado con la informacion suministrada para el registro de locales en la ciudad.
parametros requeridos:
  - name: Nombre del lugar a registrar para generar el codigo QR.
  - address: direccion del lugar a registrar para generar el codigo QR.
  - coordinate_N: coordenada norte del lugar a registrar para generar el codigo QR.
  - coordinate_W: coordenada este del lugar a registrar para generar el codigo QR.
  - tipo: tipo de lugar a registrar para generar el codigo QR.


