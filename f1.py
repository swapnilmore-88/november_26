
def find_prime_nos(num):

    list1 =[]
    for i in range(2,num):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list1.append(i)

    list1.remove(2)
    return list1


print(find_prime_nos(10))
find_prime_nos(10)