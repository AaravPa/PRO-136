import pandas as pd

df=pd.read_csv("/Users/kartik/Downloads/star_with_gravity.csv")

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

data=[]
temp_dict={}

for i in range(0, len(name)):
    temp_dict["name"]=name[i]
    temp_dict["mass"]=mass[i]
    temp_dict["radius"]=radius[i]
    temp_dict["distance"]=dist[i]
    temp_dict["gravity"]= gravity[i]
    data.append(temp_dict)

print(data)
