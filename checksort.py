def checksort(array):
    i = 1
    for i in range (len(array)):
        if (array[i] < array[i-1]):
            print("sorted")
            return True
        else:
            print("sorted")
            return False
        i+=1


a = [1,2,3,4,5,6]

print(checksort(a))
