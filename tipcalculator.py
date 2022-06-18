def main():
    bill=input('How much was your bill?')
    tip=input('How much do you want to tip?')
    print('bill amount is:',bill)
    print('tip % is:',tip)
    percent_final=tip_percent(tip)
    print('Final percentage is:',percent_final)
    bill_final=bill_calculator(bill)
    print('Final bill after strip:',bill_final)
    return percent_final,bill_final

def tip_percent(per_val):
    print('before strip and divide by 100',per_val)
    per=per_val.strip('%')
    print('After stripping %:',per)
    percent=float(per)/100
    print('after strip and divide by 100',percent)
    return percent

def bill_calculator(bill_val):
    print('bill value before strip:',bill_val)
    bill_strip=bill_val.strip('$')
    print('bill value after strip:',bill_strip)
    return bill_strip

percent_end,bill_end=main()
##bill_end=bill_final
##percent_end=percent_final

tip_final=percent_end*float(bill_end)
print(f'Leave ${tip_final:.2f}')
