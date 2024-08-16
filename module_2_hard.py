def findpairs(num):
    result=[]
    for i in range(1, num):
        for k in range(1, num):
            if num % (i + k) == 0 and i != k:
                if i in result and k in result:
                    continue
                result.append(i)
                result.append(k)

    return result
for k in range(3, 21):
    print(findpairs(k))