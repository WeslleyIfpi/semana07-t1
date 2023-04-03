def identifica_Carac(caractere):
    saida = ''
    if caractere in "0123456789":
        saida = 'número'
    elif caractere in 'AEIOU':
        saida = 'vogal'
    elif caractere in 'BCDFGHJKLMNPQRSTVXWYZ':
        saida = 'consoante'
    else:
        saida = 'símbolo'
    
    return saida

def main():
    entrada = input('Digite um caractere: ').upper()
    print(f'O caractere digitado é um(a): {identifica_Carac(entrada)}')

if __name__ == '__main__':
    main()