import time, re
import pandas as pd

from services.web_explorer import WebExplorer 
from services.conexion import testear_conexion


df= pd.read_csv('./inputs/datos.csv')

print(df['origen'][0])
# temp = WebExplorer.getBlackListURL(df['origen'][0])


for i in df['origen']:
    # WebExplorer.openURL_VT(i)
    WebExplorer.openURL_TI(i)


# testear_conexion()
