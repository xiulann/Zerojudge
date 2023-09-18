x1,y1,r1,x2,y2,r2 = map(int,input().split())
try:
    if x1!=x2:
        x1r=x1*x2
        y1r=y1*x2
        r1r=r1*x2
        x2r=x2*x1
        y2r=y2*x1
        r2r=r2*x1
    if y1r>y2r:
        y = (r1r-r2r)/(y1r-y2r)
        x=(r2r-(y2r*y))/x1r
        
    else:
        y = (r2r-r1r)/(y2r-y1r)
        x=(r1r-(y1r*y))/x2r
        
    print("x="+"{:.2f}".format(x))
    print("y="+"{:.2f}".format(y))
except Exception as e:
    print(e)

