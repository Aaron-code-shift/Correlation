import plotly.express as px 
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df , x = "Temperature" , y = "Ice-cream")
        fig.show()


def getDataSource(data_path):
    iceCreamsSales = []
    Colddrinksales = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            iceCreamsSales.append(float(row["Temperature"]))
            Colddrinksales.append(float(row["Ice-cream"]))
    return {'x': iceCreamsSales , 'y':Colddrinksales}

def findCorrelation(DataSource):
    Correlation = np.corrcoef(DataSource['x'] , DataSource['y'])
    print(Correlation[0,1])

def setup():
    data_path = './ice-cream.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()




