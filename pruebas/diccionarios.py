midiccionario ={"Alemania":"Berlin","España":"Madrid","Francia":"Paris"}
midiccionario["Italia"]="Lisboa"

print(midiccionario["España"])
print(midiccionario)

midiccionario["Italia"]="Roma"
print(midiccionario)

del midiccionario["Italia"]
print(midiccionario)