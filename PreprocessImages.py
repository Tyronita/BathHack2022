from predict import AIModel

m = AIModel()
results = []
for i in range(1, 8):
    results.append(m.predictInstance("static/trains/"+str(i)+".jpg"))