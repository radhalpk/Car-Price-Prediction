from django import forms
import pickle
import os
import pandas as pd

# class InputForm(forms.Form):
#     pkl_name='cars_pkl.pkl'

#     pkl_path=os.path.join(os.path.dirname(__file__),pkl_name)

#     with open(pkl_path,'rb') as file:
#         data=pickle.load(file)


#     company_list=data     
#     Company=forms.ChoiceField(company_list)
#     Name=forms.CharField(max_length=128)
#     EnterYear=forms.CharField(max_length=128)
#     FuelType=forms.CharField(max_length=128)

class InputForm(forms.Form):
    pkl_name = 'cars_pkl.pkl'
    pkl_path = os.path.join(os.path.dirname(__file__), pkl_name)

    # Define the ChoiceField in the __init__ method
    Company = forms.ChoiceField(choices=[], required=True)
    Name = forms.ChoiceField(choices=[], required=True)
    Year = forms.CharField(max_length=4)
    FuelType = forms.ChoiceField(choices=[], required=True)
    Traveled = forms.CharField(max_length=7)


    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)

        # Load data from pickle file
        with open(self.pkl_path, 'rb') as file:
            data = pickle.load(file)

        # Assume 'company' is a column in the loaded data
        company_choices = [(x, x) for x in data['company'].unique()]
        name_choices = [(x, x) for x in data['name'].unique()]
        #year_choices = [(x, x) for x in data['year'].unique()]
        fuel_choices = [(x, x) for x in data['fuel_type'].unique()]
        #kms_choices = [(x, x) for x in data['kms_driven'].unique()]


        # Update the choices for the Company field
        self.fields['Company'].choices = sorted(company_choices)
        self.fields['Name'].choices = sorted(name_choices)
        #self.fields['Year'].choices = year_choices
        self.fields['FuelType'].choices = sorted(fuel_choices)
        #self.fields['Traveled'].choices = kms_choices