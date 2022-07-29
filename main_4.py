# Програма для визначення просте число чи ні
def is_prime(x):
    k = 0
    for i in range(1, x):
        if x%i==0:
            i = i + 1
            k = k + 1
        else:
            i = i + 1
            
    if k  <= 1:
        return True
    else:
        return False


numb = int(input('введіть будь яке число від 1 до 1000: '))
if 1 > numb or 1000 < numb:
    print('не вірно вказане число, повторіть спробу та введіть число від 1 до 1000')
else:
    print(is_prime(numb))
