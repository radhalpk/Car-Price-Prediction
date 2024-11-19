from django.shortcuts import render
# from AppOne import LinearRegressionModel
import pickle
import pandas as pd
import os
from AppOne.forms import *
from django.http import HttpResponse
import numpy as np

def index(request):
    ##import model pkl
    model_name='LinearRegressionModel.pkl'

    model_path=os.path.join(os.path.dirname(__file__),model_name)

    with open(model_path,'rb') as file:
        Model=pickle.load(file)
    #########################
        #import csv pkl
    csv_name='cars_pkl.pkl'

    csv_path=os.path.join(os.path.dirname(__file__),csv_name)

    with open(csv_path,'rb') as file:
        data=pickle.load(file)
    ##############################
    form=InputForm()

    if request.method=="POST":
        form = InputForm(request.POST)
        if form.is_valid():
            # Access form data using cleaned_data
            year = form.cleaned_data['Year']
            name = form.cleaned_data['Name']
            company = form.cleaned_data['Company']
            fuel = form.cleaned_data['FuelType']
            kms = form.cleaned_data['Traveled']
            val=round(Model.predict(pd.DataFrame(columns=data.columns.drop('Price'),data=np.array([name,company,year,kms,fuel]).reshape(1,5)))[0],2)
            return HttpResponse(val)
    return render(request,'AppOne/index.html',context={'form':form})

def base(request):
    pkl_name='cars_pkl.pkl'

    pkl_path=os.path.join(os.path.dirname(__file__),pkl_name)

    with open(pkl_path,'rb') as file:
        data=pickle.load(file)

    return render(request,'Appone/base.html',context={'data':data})

