from flask import Flask, render_template, request
import pickle
app=Flask(__name__ ,template_folder='/Users/ray/Desktop/IBM_Project/ProjectDevelopmentPhase/Sprint - IV')

@app.route('/')
def home():
    return render_template('Prediction/Prediction.html')


@app.route('/data_predict',methods=['POST'])
def data_predict():
    age=request.form['Age']
    gender=request.form['Gender']
    tb=request.form['Total_Bilirubin']
    db=request.form['Direct_Bilirubin']
    ap=request.form['Alkaline_Phosphotase']
    aa1=request.form['Alamine_Aminotransferase']
    aa2=request.form['Aspartate_Aminotransferase']
    tp=request.form['Total_Protiens']
    a=request.form['Albumin']
    agr=request.form['Albumin_and_Globulin_Ratio']

    data=[[float(age),float(gender),float(tb),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]

    model=pickle.load(open('LiverAnalysis.pkl','rb'))
    prediction=model.predict(data)[0]

    if prediction==1:
        return render_template("Prediction/Chance.html")
    else:
        return render_template("Prediction/noChance.html")
    



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8080)