def pow(N,p):
    if p == 1:
        return N
    temp = pow(N,p//2)
    if p%2 != 0:
        return N*temp*temp
    else:
        return temp*temp
    
print(pow(2,9))

