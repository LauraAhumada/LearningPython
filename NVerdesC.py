
## Negocios Verdes Colombia

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import unicodedata
import seaborn as sns

os.chdir('/home/laura/Documents/codebar/Projects/Negocios Verdes Colombia')
data= pd.read_csv("Listado_De_Negocios_Verdes_Verificados_-_Listado_MADS.csv")
data.columns = data.columns.str.replace(' ', '_')
data.columns = data.columns.str.lower()
data.columns = [unicodedata.normalize('NFKD', n).encode('ASCII', 'ignore').decode('utf-8') for n in data.columns]

print(data.dtypes)
print(data.isnull().sum()) # Looking for missing data


# Looking the data

print(data.region.unique()) # as it is a small dataframe we can examine all the variables reapiting this code and just changing the column name. 

# Data Visualization
 # Business per region

region_freq = data.groupby('region').count()
region_per = round(region_freq.codigo_completo*100/len(data)) #percentages
labels = ('Amazonia','Caribe','Central','Orinoquia','Pacifico')

fig1, ax1 = plt.subplots()
ax1.pie(region_per,labels=labels,autopct='%1.0f%%')
plt.title('Negocios por Regiones')
ax1.axis('equal')
plt.show()

 # Sectors
 
sectors_freq = data.groupby('sector_').count()
sectors_per = (sectors_freq.codigo_completo*100/len(data)) #percentages
labels2 = ('Agro Sostenible','Apro/Val de Residuos','Biocomerio','Fuentes N/Conv de Eng Renv','Otros')

fig2, ax2 = plt.subplots()
ax2.pie(sectors_per,labels=labels2,autopct='%1.1f%%')
plt.title('Sectores')
ax2.axis('equal')
plt.show()

 # Productive chain  (THIS GRAPHIC IS USELESS)

 value = []
 
 for n in data.cadena_productiva:
         if n== 'Ingredientes naturales' or n== 'Acaí' or n== 'Asai, piña, mora, breva' or n== 'Arazá y Borojó' or n== 'Chontaduro y Tomate' or n== 'Vinagreta, Frutas, Especias' or n== 'Frutos amazónicos' or n== 'Sábila ' or n== 'vegetales y frutales amazónicas' or n== 'Pulpa de frutas' or n== 'Chontaduro' or n== 'Hortalizas' or n== 'Mora' or n== 'Papa Criolla' or n== 'Limón ' or n== 'Maracuya' or n== 'Citricos' or n== 'Piña' or n== 'Pitahaya' or n== 'Alimentos' or n== 'Frutas' or n== 'Coco' or n== 'Frutas y Hortalizas' or n== 'Mango' or n== 'Frijol ' or n== 'Col Achiote' or n == 'Achiote' or n== 'Arroz':
                 x='Frutas y verduras'       
         elif n== 'Cacao' or n == 'Cafe' or n== 'café' or n== 'Café' or n== 'Café ' or n== 'Café, Cacao y Frutas' or n== 'Café, Cacao, Frutas Hortalizas' or n== 'Café, cacao y Camarón' or n== 'Chocolates':
                 x='Cafe y/o cacao'
         elif n== 'Abejas y Apicultura ' or n== 'Miel' or n== 'Miel y Cacao':
                 x='Apicultura'
         elif n== 'Fique ':
                 x='Fique'
         elif n== 'Panela ' or n== 'Panela':
                 x='Caña de azúcar'
         elif n== 'Productos medicinales' or n== 'Salud':
                 x='Medicinal'
         elif n== 'Productos reciclados' or n== 'Reciclaje ' or n== 'Reciclaje' or n== 'Recolección' or n== 'Residuos Orgánicos' or n== 'Papel Reciclado' or n== 'Jabones a base de aceite de cocina':
                 x='Reciclaje, reutilizacion y recoleccion'
         elif n== 'Pesca Artesanal' or n== 'Piscicultura' or n== 'Cangrejo':
                 x='Pesca'
         elif n== 'Lácteos' or n== 'Carne' or n== 'Embutidos' or n== 'Ganadería': 
                 x='Ganadería y lacteos'
         elif n== 'Harinas, Jarabes y Suplementos ':
                 x='Harinas'
         elif n== 'Hilo Artesanal':
                 x='Artesanías'
         else:
                 x= n
         value.append(x)
                
data['cadena_productiva_2'] = value
cadena_productiva_freq = data.groupby('cadena_productiva_2').count()
cadena_productiva_freq['negocios']=cadena_productiva_freq.index

fig3, ax3 = plt.subplots(figsize=(6,20))
ax3.barh(cadena_productiva_freq.negocios, cadena_productiva_freq.codigo_completo, height=0.5)
plt.title('Cadena Productiva')
plt.show()

 # Business per Region and Sector
 

region_x_sector = data.pivot_table('codigo_completo', index='region', columns='sector_', aggfunc='count')
region_x_sector.columns.str.lower()
region_x_sector[np.isnan(region_x_sector)] = 0
G = 5
ind = np.arange(G)

sett1 = np.array(region_x_sector.iloc[:,0])
sett2 = np.array(region_x_sector.iloc[:,1])
sett3 = np.array(region_x_sector.iloc[:,2])
sett4 = np.array(region_x_sector.iloc[:,3])
sett5 = np.array(region_x_sector.iloc[:,4])

fig4, ax4 = plt.subplots(figsize=(10,5))
p1 = ax4.bar(ind, sett1)
p2 = ax4.bar(ind, sett2, bottom=sett1)
p3 = ax4.bar(ind, sett3, bottom=sett1+sett2)
p4 = ax4.bar(ind, sett4, bottom=sett1+sett2+sett3)
p5 = ax4.bar(ind, sett5, bottom=sett1+sett2+sett3+sett4)

plt.xticks(ind, labels)
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0]), (labels2), ncol=3, loc='lower left', bbox_to_anchor=(0, 1), fontsize='small')
plt.ylabel('Negocios Verdes')
plt.xlabel('Region')
plt.show()

 # Most frequent sectors, >10 business per sector
 
most_freq_sectors = cadena_productiva_freq[cadena_productiva_freq.codigo_completo >10]
mfsectors_list = list(most_freq_sectors.negocios)
data2 = data[data.cadena_productiva_2.str.contains('|'.join(mfsectors_list ))] #REMEMBER THIS LINE (select values from columns or subset)
  # df[(df.name.str.contains('string1')) & (df.name.str.contains('string2'))] #another option
  # df.loc[df.columnname.isin(['string1','string2','string3'])] 
  
region_x_mfsectors = data2.pivot_table('codigo_completo', index='region', columns='cadena_productiva_2', aggfunc='count')  
region_x_mfsectors[np.isnan(region_x_mfsectors)] = 0

set1 = np.array(region_x_mfsectors.iloc[:,0])
set2 = np.array(region_x_mfsectors.iloc[:,1])
set3 = np.array(region_x_mfsectors.iloc[:,2])
set4 = np.array(region_x_mfsectors.iloc[:,3])
set5 = np.array(region_x_mfsectors.iloc[:,4])
set6 = np.array(region_x_mfsectors.iloc[:,5])
set7 = np.array(region_x_mfsectors.iloc[:,6])
set8 = np.array(region_x_mfsectors.iloc[:,7])


fig5, ax5 = plt.subplots(figsize=(10,5))
pp1 = ax5.bar(ind, set1)
pp2 = ax5.bar(ind, set2, bottom=set1)
pp3 = ax5.bar(ind, set3, bottom=set1+set2)
pp4 = ax5.bar(ind, set4, bottom=set1+set2+set3)
pp5 = ax5.bar(ind, set5, bottom=set1+set2+set3+set4)
pp6 = ax5.bar(ind, set6, bottom=set1+set2+set3+set4+set5)
pp7 = ax5.bar(ind, set7, bottom=set1+set2+set3+set4+set5+set6)
pp8 = ax5.bar(ind, set8, bottom=set1+set2+set3+set4+set5+set6+set7)

plt.xticks(ind, labels)
plt.legend((pp1[0],pp2[0],pp3[0],pp4[0],pp5[0],pp6[0],pp7[0],pp8[0]), (mfsectors_list), ncol=4, loc='lower left', bbox_to_anchor=(0, 1), fontsize='small')
plt.ylabel('Negocios Verdes')
plt.xlabel('Region')
plt.show()

 # Business stage

value2 = []

for m in data.etapa_empresarial_:
        if m == 'No Reporta ':
                x1 = 'No Reporta'
        elif m == 'Inversión Inicial ':
                x1 = 'Inversión Inicial'
        else:
                x1 = m
                
        value2.append(x1)

data['etapa_empresarial_2'] = value2
business_stage = data.groupby('etapa_empresarial_2').count()
business_stage_per = business_stage.codigo_completo*100/len(data)
labels3 = 'Consolidacion', 'Despegue', 'Expansion', 'Inversion Inicial', 'No Reporta', 'Pendiente'

fig6, ax6 = plt.subplots(figsize=(10,5))
ax6.pie(business_stage_per,labels=labels3,autopct='%1.1f%%')
ax6.axis('equal')
plt.show()
## falta visualizar los sectores por departamento y la variable etapa empresarial

