import requests 
api_address='https://rest.soilgrids.org/query?lon=76.959319&lat=11.013929'
latitude=11
longitude=79
url=api_address+str(longitude)+'&'+str(latitude)

json_data = requests.get(url).json()
alum = json_data['properties']['ALUM3S']['M'].values()[0]
sand = json_data['properties']['SNDPPT']['M'].values()[0]

print("Alum is ",alum,"\n")
print("Sand is ",sand,"\n")