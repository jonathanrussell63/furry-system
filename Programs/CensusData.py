#64.7
import pandas as pd
data = pd.read_csv('census.csv')
def check_in_rule(X,Y):


    total = 0
    works = 0
    for i in range(len(data)):
        the_xs = []
        for p in range(12):
            the_xs.append(data.iloc[i][p])

        for item in X:
            init = False

            if item in the_xs:
                init=True
            else:
                init=False
        total+=init
        if init ==True:
            if Y[0] in the_xs :
                works +=1 
    if total==0:
    	return 0              
    return works/total


def arrangingRules(rules):

    ratios = []
    for rule in rules:
        loc = rule.find('>')-1
        X = rule[:loc]
        Y = rule[loc+2:]
        Y = Y.strip('{}')
        Y = Y.split()
        X = X.strip('{}')
        X=X.split(',')
        ratios.append(check_in_rule(X,Y))
       
    ratios_tmp = ratios.copy()
    ratios_sorted = ratios.copy()
    ratios_sorted.sort()

    indicies = []
    for x in ratios_sorted:
        indicies.insert(0,ratios_tmp.index(x))
        ratios_tmp[ratios_tmp.index(x)] =-1
    
    a = []
    for i in indicies:
        a.append(rules[i])
    return a


rule = ['{workclass=Private,capital-gain=None,income=Small}=>{capital-loss=None}',
'{capital-gain=None,native-country=United-States,income=Small}=>{capital-loss=None}',
'{workclass=Private,native-country=United-States,income=Small}=>{capital-loss=None}']
print(arrangingRules(rule))