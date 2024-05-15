import pandas as pd

datafile=pd.read_excel('Todays Data.xlsx')

def capacitycheck(dexamenesname, dexamenesvalue, customersdic, mpikan):
    for p,v in customersdic.items():
        i=0
        while v>0 and i <=len(dexamenesvalue)-1:
            if v<=dexamenesvalue[i]:
                mpikan[dexamenesname[i]].append(p)
                mpikan[dexamenesname[i]].append(v)
                dexamenesvalue[i]-=v
                v=0
            elif dexamenesvalue[i]>0:
                mpikan[dexamenesname[i]].append(p)
                mpikan[dexamenesname[i]].append(dexamenesvalue[i])
                v=v-dexamenesvalue[i]
                dexamenesvalue[i]=0
            i+=1
    return mpikan

#Putting excel data in data{}
column_names=datafile.columns
data={}
for column in column_names:
    data[column]=list(datafile[column])


#ABOUT CUSTOMERS
CustomerNames=data['Name']
CustomerAmount=data['Amount/kg']

#Removing NaN Data
    #Names
for nm in range(len(CustomerNames)):
    if type(CustomerNames[nm])!=str:
        CustomerNames[nm]=""
CustomerNames=[n for n in CustomerNames if n!=""]
    #Customer amounts
for ca in range(len(CustomerAmount)):
    check=str(CustomerAmount[ca])
    if check=="nan":
        CustomerAmount[ca]=""
CustomerAmount=[c for c in CustomerAmount if c!=""]


#creating a dictionary for the data that i pulled
CustomerData={}
for cd in range(len(CustomerNames)):
    CustomerData.update({CustomerNames[cd]:float(CustomerAmount[cd])})


#ABOUT TANKS
Tanks=data['Tank']
TanksCapacity=data['Capacity/kg']


#creating empty dictionaries in order to sort the customers
inside={}
for ins in range(len(Tanks)):
    inside.update({Tanks[ins]:[]})

#calling the function and print the results
finaldata=capacitycheck(Tanks,TanksCapacity,CustomerData,inside)
for nm,cpc in finaldata.items():
    print(nm,"",cpc)





