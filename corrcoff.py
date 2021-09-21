import numpy as np 
import csv
import plotly.express as px

def getDataSource(data_path):
    ice_Cream_sales=[]
    temperature=[]
    with open("data.csv") as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Marks In Percentage"]))
            ice_Cream_sales.append(float(row["Days Present"]))
            
    return{"x": temperature,"y": ice_Cream_sales}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between temp and icecream sale is - \n -->",correlation[0,1])


def plotFigure(data_path):
    with open(data_path)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()


def setup():
    data_path="data.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

    plotFigure(data_path)
    

setup()                   