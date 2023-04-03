def sr_sra(nome, sexo):
    saida = f''
    if sexo in 'Mm1':
        saida = f'Ilmo Sr. {nome}'
    elif sexo in 'Ff2':
        saida = f'Ilma Sra. {nome}'
    
    return saida

def main():
    nome = input("Digite seu nome: ").strip()
    genero = input('Digite seu genero: ').strip()

    print(sr_sra(nome, genero))

if __name__ == '__main__':
    main()