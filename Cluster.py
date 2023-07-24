# Description: This file contains the code for the clustering algorithm
from Helpers import distanceFormula

def clustering(question,ks):
    result={}
    for i,k in enumerate(ks):
        result[k]=[str(i+1)]
    for key in question:    
        if("k"+key in ks):
            continue
        xo=question[key]["xo"]
        yo=question[key]["yo"]
        edks={}
        for i,k in enumerate(ks):
            r=distanceFormula(xo,ks[k]["xo"],yo,ks[k]["yo"])
            edks[str(k)]=(r)
        min_key=min(edks.items(),key=lambda x:x[1])[0]
        ks[min_key]["xo"]=(ks[min_key]["xo"]+xo)/2
        ks[min_key]["yo"]=(ks[min_key]["yo"]+yo)/2
        result[min_key].append(key)
    return result








