def num_square(d):
    return (d**2)

def num_cube(d):
    return (d**3)

def get_digit(calc_func):
    digit=int(input('enter number'))
    print('digit provided is:',digit)
    result=calc_func(digit)
    return result

if __name__=='__main__':
    calc=input('enter func- "square" or "cube"')
    if calc=='square':
        print(get_digit(num_square))
    else:
        print(get_digit(num_cube))
    
