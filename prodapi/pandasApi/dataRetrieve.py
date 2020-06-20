import pandas as pd

# tf = pd.read_csv("testdata.csv")
class RetieveData():

    def test(self,data):
        # result = tf["Location"].value_counts()
        tf = pd.read_csv("testdata.csv")
        if data == "count":
            result = tf["Location"].value_counts()

        elif data == "unique":
            result = tf["Location"].unique()
        else:
            result = "Data not found";
        return result


x = RetieveData()

y=x.test('unique')

print(type(y))

z= pd.Series(y).to_json(orient='values')

print(type(z))

