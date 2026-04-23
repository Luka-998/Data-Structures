# input is dollar and euro exchange course in RSD
# for dollar-> RSD calculate the euro

print("Please insert course exhange rate for $: ")
dollar = float(input()) #100 rsd
euro = float(input()) #117.4 rsd
value = float(input())

def calculate_euro(dollar_course,euro_course,dollar_value):
    print(f"Please insert course exhange rate for $:{dollar}\n€: {euro}\nValue to change: {value}")
    rsd_from_dollar = dollar_value * dollar_course
    eu_result = rsd_from_dollar/euro_course
    return eu_result

eu = calculate_euro(dollar,euro,value)
print