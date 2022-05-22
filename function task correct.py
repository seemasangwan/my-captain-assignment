import operator
def most_frequent(string):
    d={}
    for i in string:
        keys=d.keys()
        if i not in keys:
            d[i]=1
        else:
            d[i]+=1
    dsc=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    print("decreasing order ",dsc)
string=str(input("enter your string "))
most_frequent(string)