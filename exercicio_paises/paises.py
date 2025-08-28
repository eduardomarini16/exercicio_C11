import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

ds_country = ds[1:,0]
#print("Paises: ", ds_country)
ds_region = ds[1:,1]
#print("Region ", ds_region)
ds_population = ds[1:,2]
#print("População: ", ds_population)
ds_area = ds[1:,3]
#print("Área: ", ds_area)

print("Country, Regions, Population, Area: ", ds_country, ds_region, ds_population, ds_area)

ds_literacy = ds[1:,9]
media_literacy = ds_literacy.astype(float)
print("Média Literacy: ", media_literacy.mean())

