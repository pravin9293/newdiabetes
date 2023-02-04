import pickle
import json
import config
import numpy as np
import pandas as pd

class DiabetesePrediction():
    
    def  __init__ (self,Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                             DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
    
    
    # loading model
    def __load_model(self):
        # load model file
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
            
            
    def prediction(self):
        self.__load_model()
        array = np.array([self.Glucose,self.BloodPressure,self.SkinThickness,self.Insulin,self.BMI,
                          self.DiabetesPedigreeFunction,self.Age], ndmin=2)
        test_df = pd.DataFrame(array, columns=self.model.feature_names_in_)
        prediction_1 = self.model.predict(test_df)[0]
        return prediction_1
        
        
if __name__ == '__main__':
    pred = DiabetesePrediction(10,20,30,40,50,60,70).prediction()
    print("**********")