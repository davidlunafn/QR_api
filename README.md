# QR API

## Description

API created with python programming language using the Flask library, for the generation of QR codes for the identification of different establishments, such as office buildings, universities, shopping centers, commercial premises, tourist centers among others. Additionally, the api allows registering all the people who read the generated QR codes through their smartphone. these data are stored in a posgrestql database.

Additionally, this repository has the code of a mobile application developed in android studio that consists of a form that allows to acquire the basic data of the status of the users, after this it allows scanning the QR codes generated through the API and through From app send the information of the form and the reading record of the QR to the database.

These codes were developed to be used in the context of the COVID-19 pandemic with an alternative to the control and registration of occupation in different places in the cities in order to be able to generate useful data for the data analysis and capture processes. of decisions.

![Explanations Image](https://github.com/davidluna-fn/QR_api/blob/master/esquema%20de%20funcionamiento.png)

## Installation and configuration

### API configuration

The first step for the installation is to clone this repository or download it from the web interface
```
git clone https://github.com/davidluna-fn/QR_api
```

The second step requires the installation of pgAdmin and posgrestql for the management and handling of the databases to be used to save the information. To download it, go to the following link https://www.postgresql.org/download/ and select the necessary option for our team. After this, run the installer, accept the required permissions and continue with the installation. When running for the first time the program requires a user password.
Despues de esto se debe crear una base de datos con el nombre de ubicaciones. Posteriormente se configurar la variable SQLALCHEMY_DATABASE_URI del archivo config.py en la carpeta /ubicaciones-restapi, dicha variable debe quedar con una configuracion del siguiente estilo 'postgresql://usuario:constraseña@direccion_de_la_db'

To run the API you must install the requirements with the following command:
```
pip install -r requirements.txt
```

Finally, the next step is to run the server with the following command:

```
python app.py 
```

### Mobile app configuration

The mobile app project requires the use of android studio, which can be downloaded from the following link https://developer.android.com/studio?hl=es-419 and the default installer configuration is carried out.
When executing the program, you must load the project by selecting the LectorQR folder and then you must configure the path of the server where the API is running and finally compile the project and install it on the cell phone.

## API paths

- '/api/v1/ubicaciones/', methods=['POST'] registers the position of a user at a specific point where the QR code is read.

required parameters:
  - id_place : It is automatically acquired from the QR code read by the application.
  - id_device : It is acquired automatically by the app as an identifier of the mobile device used.
  - phone: It is acquired from the form that is filled out when using the app to scan a code.
  - form1: Answer to question 1 of the form that is filled when using the app to scan a code.
  - form2: Answer to question 2 of the form that is filled when using the app to scan a code.
  - form3: Answer to question 3 of the form that is filled when using the app to scan a code.

- '/api/v1/ubicaciones', methods=['GET'] : It returns all the user records that through the application have read the QR code in a certain location, in json format.

- '/api/v1/qrcode/<filename>', methods=['GET'] : Returns a specific QR code corresponding to the id supplied with the information supplied for the registration of premises in the city.
  
- '/api/v1/qrcode/', methods=['POST']: Returns the QR code generated with the information provided for the registration of premises in the city.


required parameters:
  - name: Name of the place to register to generate the QR code.
  - address: address of the place to register to generate the QR code.
  - coordinate_N: North coordinate of the place to be registered to generate the QR code.
  - coordinate_W: East coordinate of the place to be registered to generate the QR code.
  - tipo: type of place to register to generate the QR code.


