# 14.12.2020
# Susi foi dormir no hospital

def saudacao(msg, nome):
    print(f'{msg}, {nome}')


saudacao('ola', 'jovane')

print('*****')


def soma3(a, b, c):
    print(a + b + c)


soma3(5, 6, 7)

print('*****')


def dois_n(a, b):
    return a + (b * a / 100)


print(dois_n(100, 10))

print('*****')


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n


print(fizz_buzz(30))
