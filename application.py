from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message



application = Flask(__name__, template_folder="Templates")

#AWS DB URI
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Faateh:Faateh123@antenna-tool-db.cwvdgyt4btit.us-east-1.rds.amazonaws.com:5432/antenna_tool_db'

#DEVELOPMENT URI
#application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faateh123@localhost:5432/antenna_tool'
application.config['SECRET_KEY'] = 'secret!'
application.config['SQLALCHEMY_ECHO'] = True
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = 'matsingtools@gmail.com'
application.config['MAIL_PASSWORD'] = 'lvfnjwubxveklhjc'
application.config['MAIL_DEFAULT_SENDER'] = 'matsingtools@gmail.com'
db = SQLAlchemy(application)
mail = Mail(application)


class AntennaInfo(db.Model):
    __tablename__ = 'antenna_info'
    id = db.Column(db.Integer, primary_key=True)
    model_number = db.Column(db.String(255))
    high_beam_count = db.Column(db.String(10))
    low_beam_count = db.Column(db.String(10))
    high_band_azimuth_1 = db.Column(db.Float(precision=53))
    high_band_azimuth_2 = db.Column(db.Float(precision=53))
    high_band_azimuth_3 = db.Column(db.Float(precision=53))
    high_band_azimuth_4 = db.Column(db.Float(precision=53))
    high_band_azimuth_5 = db.Column(db.Float(precision=53))
    high_band_azimuth_6 = db.Column(db.Float(precision=53))
    high_band_azimuth_7 = db.Column(db.Float(precision=53))
    high_band_azimuth_8 = db.Column(db.Float(precision=53))
    high_band_azimuth_9 = db.Column(db.Float(precision=53))
    high_band_azimuth_10 = db.Column(db.Float(precision=53))
    high_band_azimuth_11 = db.Column(db.Float(precision=53))
    high_band_azimuth_12 = db.Column(db.Float(precision=53))
    high_band_azimuth_13 = db.Column(db.Float(precision=53))
    high_band_azimuth_14 = db.Column(db.Float(precision=53))
    high_band_azimuth_15 = db.Column(db.Float(precision=53))
    high_band_azimuth_16 = db.Column(db.Float(precision=53))
    high_band_azimuth_17 = db.Column(db.Float(precision=53))
    high_band_azimuth_18 = db.Column(db.Float(precision=53))
    high_band_azimuth_19 = db.Column(db.Float(precision=53))
    high_band_azimuth_20 = db.Column(db.Float(precision=53))
    low_band_azimuth_1 = db.Column(db.Float(precision=53))
    low_band_azimuth_2 = db.Column(db.Float(precision=53))
    low_band_azimuth_3 = db.Column(db.Float(precision=53))
    low_band_azimuth_4 = db.Column(db.Float(precision=53))
    low_band_azimuth_5 = db.Column(db.Float(precision=53))
    low_band_azimuth_6 = db.Column(db.Float(precision=53))
    low_band_azimuth_7 = db.Column(db.Float(precision=53))
    low_band_azimuth_8 = db.Column(db.Float(precision=53))
    low_band_azimuth_9 = db.Column(db.Float(precision=53))
    low_band_azimuth_10 = db.Column(db.Float(precision=53))
    high_band_tilt_range = db.Column(db.String(50))
    low_band_tilt_range = db.Column(db.String(50))
    hor_beam_3db_high = db.Column(db.String(50))
    ver_beam_3db_high = db.Column(db.String(50))
    hor_beam_3db_low = db.Column(db.String(50))
    ver_beam_3db_low = db.Column(db.String(50))
    high_band_freq = db.Column(db.String(50))
    low_band_freq = db.Column(db.String(50))
    cband_freq = db.Column(db.String(50))
    azimuth_data_tf = db.Column(db.String(10))
    ver_beam_cband = db.Column(db.String(50))
    hor_beam_cband = db.Column(db.String(50))
    cbeam_count = db.Column(db.String(50))
    c_band_tilt_range = db.Column(db.String(50))
    ver_beam_fband = db.Column(db.String(50))
    hor_beam_fband = db.Column(db.String(50))
    fbeam_count = db.Column(db.String(50))
    f_band_tilt_range = db.Column(db.String(50))
    fband_freq = db.Column(db.String(50))
    ver_beam_10db_high = db.Column(db.String(50))
    ver_beam_10db_low = db.Column(db.String(50))
    ver_beam_10db_cband = db.Column(db.String(50))
    ver_beam_10db_fband = db.Column(db.String(50))

def send_error_email(error, is_local=False):
    if is_local:
        recipients = ['faateh.work@gmail.com']
        subject = 'Error in the Antenna Tool local host'
    else:
        recipients = ['faateh.work@gmail.com']
        subject = 'Error in the Antenna Tool'

    msg = Message(subject, recipients=recipients)
    msg.html = render_template('error_email.html', error=error)

    mail.send(msg)

@application.errorhandler(500)
def internal_server_error(error):
    is_local = request.host == '127.0.0.1:5000'
    send_error_email(error, is_local)
    return render_template('500.html'), 500


@application.route('/', methods=['GET', 'POST'])
def hello_world():
    antennas = AntennaInfo.query.all()
    if request.method == "POST":
        from_high_band_range = None
        to_high_band_range = None
        from_low_band_range = None
        to_low_band_range = None
        from_c_band_range = None
        to_c_band_range = None
        from_f_band_range = None
        to_f_band_range = None
        high_beam_Count = None
        low_beam_Count = None
        selected_model = request.form['model_number']
        print(selected_model)
        antenna = AntennaInfo.query.filter(AntennaInfo.model_number == selected_model).first()
        attributes = vars(antenna)
        print(len(attributes))
        print(type(attributes))
        # attribute_values = list(attributes.values())
        test = {key: value for key, value in attributes.items() if value != None}
        for key, value in test.items():
            print(key, value)
        if attributes['high_beam_count']:
            high_beam_Count = int(attributes['high_beam_count'])
        if attributes['low_beam_count']:
            low_beam_Count = int(attributes['low_beam_count'])
        ver_beam_high = attributes['ver_beam_3db_high']
        ver_beam_low = attributes['ver_beam_3db_low']
        hor_beam_high = attributes['hor_beam_3db_high']
        hor_beam_low = attributes['hor_beam_3db_low']
        high_tilt = attributes['high_band_tilt_range']
        low_tilt = attributes['low_band_tilt_range']
        high_band_f = attributes['high_band_freq']
        low_band_f = attributes['low_band_freq']
        c_tilt = attributes['c_band_tilt_range']
        ver_beam_c = attributes['ver_beam_cband']
        ver_beam_f = attributes['ver_beam_fband']
        f_tilt = attributes['f_band_tilt_range']
        c_band_f = attributes['cband_freq']
        f_band_f = attributes['fband_freq']
        ver_beam_10db_f = attributes['ver_beam_10db_fband']
        ver_beam_10db_c = attributes['ver_beam_10db_cband']
        ver_beam_10db_h = attributes['ver_beam_10db_high']
        ver_beam_10db_l = attributes['ver_beam_10db_low']

        if high_tilt:
            elements = high_tilt.split(" to ")
            from_high_band_range = int(elements[0])
            to_high_band_range = int(elements[1])
        if low_tilt:
            elements2 = low_tilt.split(" to ")
            from_low_band_range = int(elements2[0])
            to_low_band_range = int(elements2[1])
        if c_tilt:
            elements3 = c_tilt.split(" to ")
            from_c_band_range = int(elements3[0])
            to_c_band_range = int(elements3[1])
        if f_tilt:
            elements4 = f_tilt.split(" to ")
            from_f_band_range = int(elements4[0])
            to_f_band_range = int(elements4[1])
        # print(high_beam_Count, low_beam_Count)
        # print(from_low_band_range, to_low_band_range)
        Data = True
        return render_template('home.html', antenna=antenna, Data=Data, test=test,
                               ver_beam_high=ver_beam_high, ver_beam_low=ver_beam_low, hor_beam_low=hor_beam_low, hor_beam_high=hor_beam_high,
                               from_high_band=from_high_band_range, to_high_band=to_high_band_range,
                               from_low_band=from_low_band_range, to_low_band=to_low_band_range, antennas=antennas,
                               high_band_freq=high_band_f, low_band_freq=low_band_f, from_c_band=from_c_band_range, to_c_band=to_c_band_range,
                               ver_beam_c=ver_beam_c, from_f_band=from_f_band_range, to_f_band=to_f_band_range, ver_beam_f=ver_beam_f,
                               high_beams=high_beam_Count, low_beams=low_beam_Count, c_band_freq=c_band_f, f_band_freq=f_band_f,
                               ver_beam_10db_f=ver_beam_10db_f, ver_beam_10db_h=ver_beam_10db_h, ver_beam_10db_l=ver_beam_10db_l,
                               ver_beam_10db_c=ver_beam_10db_c)
    return render_template("home.html", antennas=antennas)




if __name__ == '__main__':
    application.run(debug=True)
