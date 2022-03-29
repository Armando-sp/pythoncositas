def conversor():
    

def run():
    bolivares= float(input('Cuantos pesos tienes?: '))
    precio_dolar= float(4.5)
    dolares= str(round(bolivares/ precio_dolar, 2))
    print('tienes '+ dolares + ' $')


if __name__ == '__main__':
    run()
