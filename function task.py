import operator
def most_frequent(string):
  d={}
  for key in string :
     if key not in d:
        d[key]=1
     else:
       d[key]=d[key]+1
  des=dict(sorted(d.items(),key=operator.itemgetter(1)))
  print("decreasing order",des)
  

string=str(input("please enter a string"))
print(most_frequent(string))