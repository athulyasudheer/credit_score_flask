from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        Age = float(request.form['Age'])
        Occupation = float(request.form['Occupation'])
        Annual_Income = float(request.form['Annual_Income'])
        Monthly_Inhand_Salary = float(request.form['Monthly_Inhand_Salary'])
        Outstanding_Debt = float(request.form['Outstanding_Debt'])
        Payment_of_Min_Amount = float(request.form['Payment_of_Min_Amount'])
        Total_EMI_per_month = float(request.form['Total_EMI_per_month'])
        Amount_invested_monthly = float(request.form['Amount_invested_monthly'])
        Payment_Behaviour = float(request.form['Payment_Behaviour'])
        Monthly_Balance = float(request.form['Monthly_Balance'])
        
        
        
        features = [[Age, Occupation, Annual_Income, Monthly_Inhand_Salary, Outstanding_Debt, Payment_of_Min_Amount, Total_EMI_per_month, Amount_invested_monthly, Payment_Behaviour, Monthly_Balance]]
        
        model = pickle.load(open('model.pkl', 'rb'))
        
        prediction = model.predict(features)
        


        defaulter_mapping = {0: 'Good', 1: 'Poor', 2: 'Standard'}
        predicted_result = defaulter_mapping[prediction[0]]
        

    return render_template('prediction.html', result=predicted_result)



if __name__ == '__main__':
    app.run()