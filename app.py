import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    date=request.form['date']
    shift=request.form['shift']
    code=request.form['code']
    if code=='VMCB4101':
        list1=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if code=='VMCB4102':
        list1=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if code=='VMCB4103':
        list1=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
    if code=='VMCB4104':
        list1=[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
    if code=='VTLB4101':
        list1=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if code=='CNTB4101':
        list1=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    if code=='CNTB4102':
        list1=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    if code=='CNTB4103':
        list1=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    if code=='CNTB4104':
        list1=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    if code=='BNDB1101':
        list1=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    if code=='BNDB1102':
        list1=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    if code=='BNDB1103':
        list1=[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    if code=='BNDB1104':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    if code=='BNDB1105':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    if code=='BNDB1106':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    if code=='CVTB4102':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    if code=='DGGB4101':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    if code=='DRLB4105':
        list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        


    LName=request.form['LName']

    if LName=='Work_Center_Cleaning':
        list2 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Tool_Setting':
        list2 = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Other_stop_unknown':
        list2 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='No_plan':
        list2 = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Tea_time':
        list2 = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Lunch_and_Dinner_Time':
        list2 = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
    if LName=='Other_Scheduled_Meeting_by_Management':
        list2 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='No_Man_Power':
        list2 = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='First_off_Insp':
        list2 = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Coolent_Filling':
        list2 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Air_Pressure_Low':
        list2 = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Other_Reasons':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Wrong_tool_Issue_Tool_Change':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='House_Keeping':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Insert_Change':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Material_Movement':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Shift_end_going_early':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Drawing_Clarification':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Mechanical_Breakdown':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Electrical_Breakdown':
        list2 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='No_load':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Material_Shortage':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Scrap_Cleaning':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    if LName=='Scrap_Movement':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    if LName=='Training':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0]
    if LName=='Monthly_Communication_Meeting':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]
    if LName=='QC_Inspection':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]
    if LName=='Want_of_Tool':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
    if LName=='Other_Quality_Error':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]
    if LName=='Power_Fail':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]
    if LName=='Waiting_For_QC':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]
    if LName=='Trail':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]
    if LName=='Attending_nature_calls':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]
    if LName=='Going_early_for_lunch':
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
    
    loss=request.form['loss']

    final_features = np.array([date,shift,loss,list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10],list1[11],list1[12],list1[13],list1[14],list1[15],list1[16],list1[17],list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list1[7],list2[8],list2[9],list2[10],list2[11],list2[12],list2[13],list2[14],list2[15],list2[16],list2[17],list2[18],list2[19],list2[20],list2[21],list2[22],list2[23],list2[24],list2[25],list2[26],list2[27],list2[28],list2[29],list2[30],list2[31],list2[32],list2[33]],dtype=np.int32).reshape(1,-1)

    prediction = model.predict(final_features)

    print(prediction)

    return render_template('index.html', prediction_text='machine end time in sec is {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
