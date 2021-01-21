from flask import Flask
from flask import redirect, send_from_directory
from flask import url_for
from flask import jsonify
from flask import request
from config import config
import os
import qrcode
from werkzeug.utils import secure_filename


from models import Ubicaciones
from models import QrPlace


from models import db
import urllib.parse as urlparse



def generateQR(data):
    data = "http://192.168.43.71:5000/api/v1/ubicaciones/?id_place={}".format(data)
    img = qrcode.make(data)
    return img



def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    app.config['UPLOAD_FOLDER'] = './codigos_qr'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)




@app.route('/api/v1/ubicaciones/', methods=['POST'])
def create_user():
    url = request.url
    parsed = urlparse.urlparse(url)
    parsed = urlparse.parse_qs(parsed.query)
    print('#'*200)
    data = {
        "id_place" :  int(parsed['id_place'][0]),
        "id_device" :  parsed['id_device'][0],
        "status" :  parsed['status'][0],
        }
    #data = request.get_json(force=True)
    print(type(data))

    if data.get('id_place') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('id_device') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('status') is None:
        return jsonify({'message': 'Bad request'}), 400


    ubicacion = Ubicaciones.create(data)

    return jsonify({'ubicacion': data })





@app.route('/api/v1/ubicaciones', methods=['GET'])
def get_users():
    ubicaciones = [ ubicacion.json() for ubicacion in Ubicaciones.query.all() ] 
    return jsonify({'Ubicaciones': ubicaciones })

@app.route('/api/v1/ubicaciones/<id>', methods=['GET'])
def get_user(id):
    ubicacion = Ubicaciones.query.filter_by(id=id).first()
    if ubicacion is None:
        return jsonify({'message': 'Ubicacion does not exists'}), 404

    return jsonify({'ubicacion': ubicacion.json() })


@app.route('/api/v1/qrcode/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/api/v1/qrcode/', methods=['POST'])
def regiter_place():
    url = request.url
    parsed = urlparse.urlparse(url)
    parsed = urlparse.parse_qs(parsed.query)
    data = {
        "name" :  parsed['name'][0],
        "address" :  parsed['address'][0],
        "coordinate_N" :  parsed['coordinate_N'][0],
        "coordinate_W" :  parsed['coordinate_W'][0],
        "tipo" :  parsed['tipo'][0],
        }



    if data.get('name') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('address') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('coordinate_N') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('coordinate_W') is None:
        return jsonify({'message': 'Bad request'}), 400
    if data.get('tipo') is None:
        return jsonify({'message': 'Bad request'}), 400

    qrplace = QrPlace.create(data)

    img = generateQR(str(qrplace.id_place))
    filename = secure_filename(str(qrplace.id_place)+ '.png')
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for("get_file",filename=filename))



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)    