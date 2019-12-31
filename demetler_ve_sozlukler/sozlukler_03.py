yemekler = {"çorbalar": {"etli" :  ["işkembe","kelle paça","tavuk suyu"],
                         "etsiz":  ["mercimek","ezo gelin"],
                         "sebze":  ["domates","brokoli"]},
            "Kebaplar": {"acılı" : ["adana","beyti"],
                         "acısız": ["urfa","mardin"],
                         "dürümler":["ciger","adana"]}  }


#print(yemekler)
#print(yemekler["Kebaplar"])
#print(yemekler["Kebaplar"]["dürümler"][0])

yemekler["çorbalar"]["etli"].append("kavurma")

print(yemekler)