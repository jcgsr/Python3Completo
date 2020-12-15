# 15.12.2020
# Susi no hospital ainda

def ola_mundo():
    return 'olá mundo!'

def retorno(fun):
    return fun()

exe = retorno(ola_mundo)
print(exe)


def f1(fun, *args, **kwargs):
    return fun(*args, **kwargs)


def fala_oi(nome):
    return f'oi, {nome}'


def saud(nome, saud):
    return f'{saud} {nome}'

e = f1(fala_oi, 'Jó')
e2 = f1(saud, 'Jó', saud='DIZ!')
print(e)
print(e2)

