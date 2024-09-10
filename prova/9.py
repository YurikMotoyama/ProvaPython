
teste = [1,2,3,4,5,6]

print(len(teste))


def fibonacci_sequence(N):
    xuxa = [0,1]
    
    while (len(xuxa) < N):
        xuxa.append(xuxa[len(xuxa)-2] + xuxa[len(xuxa)-1])
    return (xuxa)
        
print(fibonacci_sequence(5))