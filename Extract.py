import pandas as pd
import io
import numpy as np
# funciones
def verify_date(fn):
    df = pd.read_excel(fn)
    muestra = df.head(40)
    objeto = {muestra.iloc[:,d].dtype == np.dtype(object) for d in range(muestra.shape[1])}
    if len(objeto)==1:    
        # Verificando los temas 
        float_data = [not(isinstance(data, (int, float))) for data in muestra.iloc[3]]
        saltos = 1+sum(float_data)
        print(saltos)
        return saltos
    saltos=0
    return saltos

# Lectura archivos Excel
# Input 
path = 'C:/Users/Jose Ibanez/Datos/Solar/ORI/Obs/'
# filename = 'GIZ METEO PPC F1 & F2 20220928.xls'
filename = 'GIZ METEO PPC F1 & F2 20220924.xls'
# filename = '20221009 - USF - Datos de Estaciones Meteorologicas - PPC.xlsx'
# Process
fn = path+'/'+filename
skip_rows = verify_date(fn)
df = pd.read_excel(fn, skiprows=skip_rows)
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
with open("df_info.txt", "w", encoding="utf-8") as f:
    f.write(s)

# first_row = (df.count(axis = 1)  >= df.shape[1]).idxmax()
# df.columns = df.loc[first_row]
# print(first_row)
# print(df.columns)
# Output
df.to_csv('./temp_E.csv',index=False)