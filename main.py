#program to print 3 vcalues in decreasing order

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

largest = max(a,b,c)
least = min(a,b,c)
mid = a+b+c-(largest+least)


print(largest,mid,least,sep=">")