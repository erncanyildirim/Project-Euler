# ENG : Starting in the top left corner of a 2 × 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. 
# How many such routes are there through a 20 × 20 grid?

# TR : 2x2'lik bir gridin sol üst köşesinden başlayıp sadece sağa ve aşağıya doğru hareket edebilen, sağ alt köşeye giden tam 6 yol var. 
# 20 × 20'lik bir ızgarada bu şekilde kaç tane rota vardır?

def fact(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial

steps = fact(40) / (fact(20) * fact(20))

print(int(steps))
