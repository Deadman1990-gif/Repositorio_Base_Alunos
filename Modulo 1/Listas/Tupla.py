tupla=("a", "b", "c")
tupla
tupla=100,200,300
tupla
def tabuada():
    l=[2,4,6,8,10,12,14,16,18,20]
    for x, e in enumerate(l):
        print("%d*%d=%d"%(x,e, x*e))
#tabuada()
def tabuada2():
    l=[3,6,9,12,15,18,21,24,27,30]
    for x, e in enumerate(l):
        print("%d+%d=%d"%(x,e, x+e))
# tabuada2()
def tabuada3():
    l=[3,6,9,12,15,18,21,24,27,30]
    for x, e in enumerate(l):
        print("%d+%d=%d"%(x,e, x+e))
#tabuada3()
def tabuada4():
    l=[3,6,9,12,15,18,21,24,27,30]
    for x, e in enumerate(l):
        print("%d/%d=%f"%(x,e, x/e))
tabuada4()