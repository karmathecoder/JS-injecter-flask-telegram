from flask import Flask,render_template ,request
from methods import send_msg
import json
from datetime import datetime

app = Flask(__name__)

now = datetime.now()

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/ThankYou',methods=['GET','POST'])
def thankyou():
    if request.method == "POST":
        email = request.form.get("sender_email")
        send_msg(str(email))
        print(email)
        return render_template('thanks.html',flashmsg = "Thank You, You Will get Nortified Soon")
    return render_template('main.html')

@app.route('/test/', methods=['GET','POST'])
def test():
     if request.method == "POST":
        ipdata=request.json['data']
        head = request.headers
        send_data = (ipdata,now.strftime("%d/%m/%Y %H:%M:%S"),head)
        send_msg(str(send_data))
     return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)