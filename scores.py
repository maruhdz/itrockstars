#a, e, i, o, u
#exam scores
from statistics import mean
Arturo=[90,100,50,70]
Artemio=[70,65,100,80]
Juan=[90,90,100,80]
Rene=[50,60,70,80]
Pedro=[100,50,100,90]
Alan=[50,40,70,80]

#excercise 2.1
#print the average score of each student
#score > 95 ==> "excentado"
#score <95 ==> and score > 85: "Aprobado"
#score >70 ==> and score < 85: "Promedio"
#score < 70: "Reprobado"
#output example:
#Name    Score  Message
#arturo  60     Reprobado

names=["Arturo", "Artemio", "Juan", "Rene", "Pedro", "Alan"]
alumnos=[Arturo, Artemio, Juan, Rene, Pedro, Alan]
hlalum=[]
print (" Name      ", " Score        ", " Message        ", " Highest Score  ", " Lowest Score  ")

for i in range(len(alumnos)):
    score=alumnos[i]
    average=(mean(score))

    if average > 95:
        message=("Excentado")
    elif average < 95 and average> 85:
        message=("Aprobado")
    elif average > 70 and average<85:
        message=("Promedio")
    elif average < 70:
        message=("Reprobado")

    hlalum.append(average)

    print(names[i],'      ',average,'          ', message,'          ', (max(score)), '             ', (min(score)))


    maxa= (max(hlalum))
    mina= (min(hlalum))

    nMx=hlalum.index(maxa)
    nMn=hlalum.index(mina)


print ("\n")
print ("Highest Score   ", names[nMx], (max(hlalum)))
print ("Lowest Score   ", names[nMn], (min(hlalum)))
