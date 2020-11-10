import json

datos = {
    'nombre':'jesus',
    'edad':43,
    'pais':'piedras negras'
}

with open('dat.json','w')as file:
    json.dump(datos,file)
    
with open('dat.json','r')as file:
    data=json.load(file)
    print(data)
