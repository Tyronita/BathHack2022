from flask import Flask, render_template, request
from DatabaseModel import DatabaseConnection
from NetworkModel import NetworkModel
import os
from predict import AIModel
# from datetime import datetime

app = Flask(__name__)
db = DatabaseConnection()
network: NetworkModel = db.get_network()
TRAIN_FOLDER = os.path.join("\\static", "trains")
app.config["TRAIN_FOLDER"] = TRAIN_FOLDER
mdl: AIModel = AIModel()
mdl_results = []
for i in range(1, 8):
    mdl_results.append(mdl.predictInstance("static/trains/"+str(i)+".jpg"))
# lines = network.getLines()

@app.route('/')
def home():
    title = "Project Halo"
    location = "United Kingdom"
    return render_template(
        'main.html', 
        enumerate=enumerate, 
        title = title, 
        location = location, 
        lineId = None, 
        network = network
    )

@app.route('/line/<int:line_id>', methods=['GET', 'POST'])
def line(line_id):
    title = "Project Halo"
    location = "United Kingdom"
    train_location = 1
    station_set = [2,3]
    predictResult = None
    full_filename = os.path.join(app.config["TRAIN_FOLDER"], str(station_set[0])+".jpg")
    if request.method == "POST":
        train_location = int(request.form.get("move_train"))+1
        station_set = []
        station_set.append(train_location+1)
        station_set.append(train_location+2)
        if station_set[0] < 8:
            full_filename = os.path.join(app.config["TRAIN_FOLDER"], str(station_set[0])+".jpg")


    # Evan/sort of Nathan AI Here
    predictResult = mdl_results[station_set[0]-1]

    return render_template(
        'main.html', 
        enumerate=enumerate,
        title = title, 
        location = location, 
        network = network, 
        lineId = line_id, 
        train_loc = train_location,
        station_set = station_set,
        station_img = full_filename,
        prediction = predictResult
    )


if __name__ == "__main__":
    app.run(debug=True)