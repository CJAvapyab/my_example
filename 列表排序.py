numberlist = [78,68,46,0,8,5,89,70]
for num in numberlist:
    if num <= 40:
        numberlist.remove(num) 
        numberlist.insert(0,0)
        
numlist = len(numberlist)
for i in range(0,numlist):
    try:
        numberlist.remove(0)
    except ValueError:
        pass
numberlist.sort(reverse=False)
print(numberlist)
