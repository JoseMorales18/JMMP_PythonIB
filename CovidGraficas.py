from matplotlib.pyplot import *

estados=["Coahuila","Nuevo Leon","Ciudad de Mexico","Total"]
valores=[2143,3583,14480,20206]
colores=["blue","red","green","purple"]

title("Fallecidos por Covid")
bar(estados, height=valores, color=colores, width=0.5)
ylabel("Fallecidos")
xlabel("Estados")
show()
