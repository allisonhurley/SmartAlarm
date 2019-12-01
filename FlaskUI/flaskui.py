from flask import Flask, request, send_from_directory, render_template, redirect
import json

app = Flask(__name__)
config_data = { "snooze": 9, "max-active": 120 }

@app.route('/', methods=['GET', 'POST'])
def index():
    global config_data
    if request.method == 'POST': 
        return redirect("/config")
    return render_template("index.html", config_data=config_data)

@app.route('/config', methods=['GET', 'POST'])
def config():
    global config_data
    if request.method == 'POST': 
        if request.form.get('submit', default=False):
            # save form values
            config_data = request.form
            with open("config.json", "w") as out:
                out.write(json.dumps(request.form))
        return redirect("/")
    return render_template("config.html", config_data=config_data)

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

