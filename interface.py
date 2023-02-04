from flask import Flask,render_template, jsonify, request
import config
from utils import DiabetesePrediction
import traceback

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_diabetes', methods = ['POST','GET'])

def predict_diabetes():
    try:
        if request.method == 'POST':
            data = request.form.get
            
            print("user data is :", data)
            Glucose = eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThickness = eval(data('SkinThickness'))
            Insulin = eval(data('Insulin'))
            BMI = eval(data('BMI'))
            DiabetesPedigreeFunction = eval(data('DiabetesPedigreeFunction'))
            Age = eval(data('Age'))
            
         
            obj = DiabetesePrediction(Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                                          DiabetesPedigreeFunction,Age)
            
            pred_class = obj.prediction()
            
            # return jsonify({"result": f"diabetes class is :{pred_class}"})
            return render_template('index.html', prediction = pred_class)
        
        else:
            data = request.args.get
            
            #print("user data is :", data)
            Glucose = eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThickness = eval(data('SkinThickness'))
            Insulin = eval(data('Insulin'))
            BMI = eval(data('BMI'))
            DiabetesPedigreeFunction = eval(data('DiabetesPedigreeFunction'))
            Age = eval(data('Age'))
            
            obj = DiabetesePrediction(Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                                          DiabetesPedigreeFunction,Age)
            
            pred_class = obj.prediction()
            
            return render_template('index.html', prediction = pred_class)
        
    except:
        print(traceback.print_exc())
        return jsonify({"message" : "unsuccessful"})
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port  = config.PORT_NUMBER, debug=False)
