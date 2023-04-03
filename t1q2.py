def eh_impar(numero):
    if numero % 2 != 0 :
        return True
    return False

def main():
    numero = int(input('Digite um número: '))
    print(f'O número é impar? {eh_impar(numero)}')

if __name__ == '__main__':
    main()