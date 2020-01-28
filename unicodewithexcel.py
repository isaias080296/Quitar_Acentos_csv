import unidecode

#from string import maketrans 

#from seaborn import load_dataset

import pandas as pd

import xlsxwriter

import unicodedata

#hoja = escribir.add_worksheet()

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

datos=pd.read_csv("C:\\Users\\AFIRMA - ISAIAS\\Downloads\\estaciones-metrobus1.csv",header=0)
#print(datos)
escribir=xlsxwriter.Workbook("C:\\Users\\AFIRMA - ISAIAS\\Downloads\\estaciones-metrobus1.csv")
hoja = escribir.add_worksheet('Sheet')
ip2=0

col01=[]
col02=[]

l=datos.iloc[1, 1]





while ip2 < 234:
 # print(datos.iloc[ip2, 1])
  col1=str(strip_accents(datos.iloc[ip2, 1]))

  col2=str(strip_accents(datos.iloc[ip2, 2]))
  col01 +=[str(col1)]
  col02 +=[str(col2)]
  #hoja.write(ip2, 1, diados)
  if (ip2 == 235):
    break
  ip2 +=1
    #print(dia2)




data={'Estaciones':col01,'Linea':col02}

df = pd.DataFrame(data, columns = ['Estaciones','Linea'])
df.to_csv('example.csv')


print(col1,col2)



