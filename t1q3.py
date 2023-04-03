def sinal(entrada):
    saida = ''
    if entrada == 'V':
        saida = 'Siga'
    elif entrada == 'A':
        saida = "Atenção"
    elif entrada == 'E':
        saida = 'Pare'
    
    return saida

def main():
    entrada = input('Digite um sinal (V-verde, A-Amarelo, E-Vermlho)').upper()
    print(f'{sinal(entrada)}')

if __name__ == '__main__':
    main()