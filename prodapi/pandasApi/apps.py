from django.apps import AppConfig
from django.conf import settings
import os

class PandasapiConfig(AppConfig):
    name = 'pandasApi'


import pandas as pd

# tf = pd.read_csv("testdata.csv")
class RetieveData():


    # CV = os.path.join(settings.CV, 'testdata.csv')
    # tf = pd.read_csv(CV)
    def test(data):
        # result = tf["Location"].value_counts()
        CV = os.path.join(settings.CV, 'testdata.csv')
        tf = pd.read_csv(CV)
        if data == "count":
            result = tf["Location"].value_counts()

        elif data == "unique":
            result = tf["Location"].unique()
            # result.to_frame()
        else:
            result = "Data not found";
        return result
