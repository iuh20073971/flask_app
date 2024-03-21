from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://www.kindpng.com/picc/m/343-3437091_iron-man-helmet-logo-hd-png-download.png",
    "https://i.ebayimg.com/images/g/aTwAAOxyVaBS3dUJ/s-l400.jpg",
    "https://i.pinimg.com/474x/c1/f7/2f/c1f72f23c2b299fd556bf35c0f991bbe.jpg",
    "https://i.pinimg.com/474x/4c/1d/be/4c1dbed508d2e85c1488b576939cf0e6.jpg",
    "https://i.pinimg.com/originals/c4/8e/c8/c48ec805ab6adb7738c5551bea137939.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Captain_America%27s_shield.svg/640px-Captain_America%27s_shield.svg.png",
    "https://www.nicepng.com/png/detail/120-1208220_black-widow-symbol-fill-black-widow-logo-marvel.png"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "DaiPhuc":
    app.run(host="0.0.0.0")
from flask import Flask, render_template

app = Flask(DaiPhuc)

@app.route('/')
def index():
    school = "Trường DHCNTPHCM"
    class_name = "Lớp DHHTTT16B"
    student_id = "20073971"
    student_name = "Đại Phúc"
    return render_template('index.html', school=DHCNTPHCM, class=DHHTTT16B, student_id=20073971, student_name="Đại Phúc")

if __name__ == '__main__':
    app.run(debug=True)
