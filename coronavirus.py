def infect(a, w, h):

    i, j = 0, 0

    for i in range(w):
        for j in range(h):
            
            if i == 0 and a[i][j] == 1:
                a[i+1][j] = 1
                a[i][j+1] = 1
                a[i][j-1] = 1

            elif j == 0 and a[i][j] == 1 and i != w:
                a[i+1][j] = 1
                a[i][j+1] = 1
                

            elif i == w and a[i][j] == 1:
                a[i-1][j] = 1
                a[i][j+1] = 1

            elif j == h and a[i][j] == 1:
                a[i+1][j] = 1
                a[i][j-1] = 1
            
            elif (a[i][j] == 1):
                a[i+1][j] = 1
                a[i][j+1] = 1
                a[i-1][j] = 1
                a[i][j-1] = 1

            j+=1
        i+=1

    return a



w, h = 5, 4
inputinf = [[0 for x in range(w)] for y in range(h)] 

inputinf[0][0] = 0
inputinf[0][1] = 1
inputinf[0][2] = 1
inputinf[0][3] = 0
inputinf[0][4] = 1

inputinf[1][0] = 0
inputinf[1][1] = 1
inputinf[1][2] = 0
inputinf[1][3] = 1
inputinf[1][4] = 0

inputinf[2][0] = 0
inputinf[2][1] = 0
inputinf[2][2] = 0
inputinf[2][3] = 0
inputinf[2][4] = 1

inputinf[3][0] = 0
inputinf[3][1] = 1
inputinf[3][2] = 0
inputinf[3][3] = 0
inputinf[3][4] = 0


print("Input", inputinf)
inputinf = infect(inputinf, 3, 4) 
print("After first hour : ", inputinf)
inputinf = infect(inputinf, 3, 4) 
print("After 2nd hour", inputinf)




