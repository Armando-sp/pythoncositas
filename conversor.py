def run():
    bolivares= float(input('Cuantos bolivares tienes?: '))
    precio_dolar= float(4.44)
    dolares= str(round(bolivares/ precio_dolar, 2))
    print('posees '+ dolares + ' $')


if __name__ == '__main__':
    run()