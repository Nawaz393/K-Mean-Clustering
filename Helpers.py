
import math 
def Question():
    question = {}
    try:
        rows=int(input("Enter the number of rows: "))
    except ValueError:
        print("Enter a valid number")
        exit()
    for i in range(rows):
        try:
            xo=float(input("Enter xo for row"+ str(i+1)+ ": "))
            yo=float(input("Enter yo for row"+ str(i+1)+ ": "))
        except ValueError:
            print("Enter a valid number")
            exit()
        question[str(i+1)]={"xo":xo,"yo":yo}
    given_ks={}
    num_of_k=int(input("Enter the number of k: "))

    if(num_of_k>2):
        for i in range(num_of_k):
            given_ks["k"+str(i+1)]=question[str(i+1)]
    else:
        given_ks["k1"]=question["1"]
        given_ks["k2"]=question["2"]
    return (question,given_ks)

def distanceFormula(xo,xc,yo,yc):
    return math.sqrt((xo-xc)**2+(yo-yc)**2)




