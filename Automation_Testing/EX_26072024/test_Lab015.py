import csv
import pandas as pd


class Test_crud(object):

    def test_update(self):
        # read the file
        with open("Automation_Testing/EX_26072024/usedadata.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])


    def test_read_csv(self):
        df = pd.read.csv("Automation_Testing/EX_26072024/usedadata.csv")
        print(df)


