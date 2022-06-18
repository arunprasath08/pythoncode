def func_sq(num):
    return num**2

digit=int(input('You need square for..'))

square=func_sq
if __name__=='__main__':
    val=square(digit)
    print(val)
