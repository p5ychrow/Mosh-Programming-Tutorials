#recieve weight input and kg/lbs weight input and then calculate a conversion. Examples inputs below

#weight = float(input('What is your weight? '))
#weight_metric = input('Is your weight in (L)bs or (K)gs? ')
def convert_weight(weight, weight_metric):
    if weight_metric.upper() == 'L':
        result = f"You're converted weight is: {weight * 0.453592} kgs" #converion for lbs to kgs
    elif weight_metric.upper() == 'K':
        result = f"You're converted weight is: {weight * 2.20462} lbs" #conversion for kgs to lbs
    elif weight_metric != 'L' or 'K':
        result = 'ERROR: please provide L for lbs or K for kgs'
    return result