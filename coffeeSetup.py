import plotly.express as px 
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df , x = "Coffee in ml" , y = "sleep in hours")
        fig.show()


def getDataSource(data_path):
    iceCreamsSales = []
    Colddrinksales = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            iceCreamsSales.append(float(row["Coffee in ml"]))
            Colddrinksales.append(float(row["sleep in hours"]))
    return {'x': iceCreamsSales , 'y':Colddrinksales}

def findCorrelation(DataSource):
    Correlation = np.corrcoef(DataSource['x'] , DataSource['y'])
    print(Correlation[0,1])

def setup():
    data_path = './cofeeSleep.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()




