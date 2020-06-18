import pandas as pd

# tf = pd.read_csv("testdata.csv")
class RetieveData():
    tf = pd.read_csv("testdata.csv")
    def test(self,data):
        # result = tf["Location"].value_counts()
        if data == "count":
            result = tf["Location"].value_counts()

        elif data == "unique":
            result = tf["Location"].unique()
        else:
            result = "Data not found";
        return result


#test("unique")

#print(result)
