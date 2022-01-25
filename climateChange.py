import pandas as pd
import matplotlib.pyplot as plt


def climateChangefn():
    glbtemp = pd.read_csv("/Users/annmerinpeter/Downloads/GlobalTemperatures.csv",index_col=0)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.max_rows',None)
    print(glbtemp.columns)
    #print(glbtemp.head())
    #print(glbtemp)

    glblandtempstate = pd.read_csv("/users/annmerinpeter/Downloads/GlobalLandTemperaturesByState.csv",index_col=0)
    print(glblandtempstate.columns)

    glblandtempMcity = pd.read_csv("/Users/annmerinpeter/Downloads/GlobalLandTemperaturesByMajorCity.csv",index_col=0)
    print(glblandtempMcity.columns)

    glblandtemcountry = pd.read_csv("/Users/annmerinpeter/Downloads/GlobalLandTemperaturesByCountry.csv",index_col=0)
    print(glblandtemcountry.columns)

    state = glblandtempstate["State"]
    temp = glblandtempstate["AverageTemperature"]

    plt.bar(state, temp)
    plt.title('title name')
    plt.xlabel('xAxis name')
    plt.ylabel('yAxis name')
    plt.show()
