from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="Templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faateh123@localhost:5432/antenna_tool'
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

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
    low_band_azimuth_1 = db.Column(db.Float(precision=53))
    low_band_azimuth_2 = db.Column(db.Float(precision=53))
    low_band_azimuth_3 = db.Column(db.Float(precision=53))
    low_band_azimuth_4 = db.Column(db.Float(precision=53))
    low_band_azimuth_5 = db.Column(db.Float(precision=53))
    low_band_azimuth_6 = db.Column(db.Float(precision=53))
    high_band_tilt_range = db.Column(db.String(50))
    low_band_tilt_range = db.Column(db.String(50))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        selected_model = request.form['model_number']
        antenna = AntennaInfo.query.filter(AntennaInfo.model_number == selected_model).first()
        attributes = vars(antenna)
        print(type(attributes))
        # attribute_values = list(attributes.values())
        test = {key: value for key, value in attributes.items() if value != None}
        for key, value in test.items():
            print(key, value)
        high_beam_Count = test['high_beam_count']
        low_beam_Count = test['low_beam_count']
        print(high_beam_Count, low_beam_Count)
        Data = True
        return render_template('home.html', antenna=antenna, Data=Data, test=test, high_beam=int(high_beam_Count), low_beam=int(low_beam_Count))
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)
