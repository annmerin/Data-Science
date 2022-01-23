import pandas as pd

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