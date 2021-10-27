import csv
rows=[]
with open("final.csv","r") as f:
  csvreader=csv.reader(f)
  for i in csvreader:
    rows.append(i)
headers=rows[0]
planet_data=rows[1:]
headers[0]="row_num"
print(headers)
print(planet_data[0])


ss={}
for i in planet_data:
  if(ss.get(i[11])):
    ss[i[11]]+=1
  else:
    ss[i[11]]=1

print(ss["KOI-351"])

temp=list(planet_data)
for i in temp:
  planet_mass=i[3]
  if(planet_mass.lower()=="unknown"):
    planet_data.remove(i)
    continue
  else:
    planet_mass_value=planet_mass.split(" ")[0]
    planet_mass_ref=planet_mass.split(" ")[1]  
    if(planet_mass_ref=="Jupiters"):
      planet_mass_value=float(planet_mass_value)*317.8
    i[3]=planet_mass_value


  planet_radius=i[7]
  if(planet_radius.lower()=="unknown"):
    planet_data.remove(i)
    continue
  else:
    planet_radius_value=planet_radius.split(" ")[0]
    planet_radius_ref=planet_radius.split(" ")[2]  
    if(planet_radius_ref=="Jupiter"):
      planet_radius_value=float(planet_radius_value)*11.2
    i[7]=planet_radius_value  

print(len(planet_data))    

planets=[]
max_ss=max(ss,key=ss.get)
for i in planet_data:
   if(max_ss==i[11]):
     planets.append(i)

print(planets)
