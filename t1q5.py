def calcula_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3 

def nota_final(nota1, nota2, nota3):
    media = calcula_media(nota1, nota2, nota3)
    if nota3 > 8:
        media += 1
    if media > 10:
        media = 10

    return media

def main():
    nota1 = int(input('Digite nota 1: '))
    nota2 = int(input('Digite nota 2: '))
    nota3 = int(input('Digite nota 3: '))

    print(f'Média: {nota_final(nota1, nota2, nota3)}')

if __name__ == '__main__':
    main()

