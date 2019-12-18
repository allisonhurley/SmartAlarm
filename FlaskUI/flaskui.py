from flask import Flask, request, send_from_directory, render_template, redirect
import subprocess
import json

app = Flask(__name__)
config_data = { "snooze": 9, "max-active": 120 }
with open('/home/pi/SmartAlarm/config.json') as json_file:
#with open('C:/Users/Shayna/Desktop/Smart_Alarm/SmartAlarm/config.json') as json_file:
    config_data = json.load(json_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    global config_data
    if request.method == 'POST': 
        return redirect("/config")
    return render_template("index.html", config_data=config_data)

@app.route('/on', methods=['GET', 'POST'])
def on():
    subprocess.run(["/home/pi/SmartAlarm/alarm_on"])
    #subprocess.run(["C:/Users/Shayna/Desktop/Smart_Alarm/SmartAlarm/alarm_on"])
    return redirect("/")

@app.route('/off', methods=['GET', 'POST'])
def off():
    subprocess.run(["/home/pi/SmartAlarm/alarm_off"])
    #subprocess.run(["C:/Users/Shayna/Desktop/Smart_Alarm/SmartAlarm/alarm_off"])
    return redirect("/")

@app.route('/config', methods=['GET', 'POST'])
def config():
    global config_data
    if request.method == 'POST': 
        if request.form.get('submit', default=False):
            # save form values
            config_data = request.form
            with open("/home/pi/SmartAlarm/config.json", "w") as out:
            #with open("C:/Users/Shayna/Desktop/Smart_Alarm/SmartAlarm/config.json", "w") as out:
                out.write(json.dumps(request.form))
            subprocess.run(["/home/pi/SmartAlarm/adjust_cron"])
            #subprocess.run(["C:/Users/Shayna/Desktop/Smart_Alarm/SmartAlarm/adjust_cron"])
        return redirect("/")
    return render_template("config.html", config_data=config_data)

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

