# input number
# if divisible by 3 we get fizz
# if divisible by 5 we get buzz
# if divisible by 3 and 5 we get fizz buzz
# else number

def fizz_buzz(number):
    number = int(number)
    if number % 3 == 0 and number % 5 ==0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 ==0:
        return 'buzz'
    return number


print(fizz_buzz(6))