from Criptografia_Hill import *

t = 'S'
descrip = descriptografia()
crip = criptografia()

while t != 'N':
    print('\n'*49)
    print(' ' * 10 + '\033[0;30m 1 - criptografar\n' +
          ' ' * 10 + ' 2 - descriptografar\n')
    print(' ' * 6 + 'Digite a opcao que deseja: ', end='')
    opcao = int(input())
    print('\n'*49)

    if opcao == 1:

        matriz = list()
        print("\033[0;30m=>Digite sua Matriz<=")
        matrizz = list(map(int, input().split()))
        matriz.append(matrizz)
        for x in range(len(matrizz) - 1):
            matriz1 = list(map(int, input().split()))
            matriz.append(matriz1)
        print("=>Digite sua frase<=\033[0m")
        frase = input()

        det_inverso = descrip.mod_26_inverso(descrip.calc_det_cofat(matriz))

        if type(det_inverso) == str:
            print(f'\n\033[0;31mSua frase não irá poder ser descriptografada, pois seu determinante({descrip.calc_det_cofat(matriz)}) não pode ser invertido em mod26!!\033[0m\n ')

        frase = crip.format_frase(frase, len(matriz))

        silabas = crip.separa_silabas(frase, len(matriz))
        silabas_ASCII = crip.array_ASCII(silabas)
        crip_num = crip.criptografar(silabas_ASCII, matriz)
        mod26 = crip.mod_26(crip_num)
        criptografia = crip.frase_criptografada(mod26)

        print(f'\033[0;30mFrase criptografada:\033[1m {criptografia}\033[0m')

    elif opcao == 2:

        matriz = list()
        print("\033[0;30m=>Digite sua Matriz que usou para criptografar<=".title())
        matrizz = list(map(int, input().split()))
        matriz.append(matrizz)
        for x in range(len(matrizz) - 1):
            matriz1 = list(map(int, input().split()))
            matriz.append(matriz1)
        print("=>Digite sua frase criptografada<=\033[0m")
        frase = input()

        frase = crip.format_frase(frase, len(matriz))

        matriz_inversa = descrip.matriz_inversa(matriz)
        if descrip.calc_det_cofat(matriz)>0:
            det_inverso = descrip.mod_26_inverso(descrip.calc_det_cofat(matriz))

            if type(det_inverso) == str:
                print(f'\n\033[0;31mError, determinante({descrip.calc_det_cofat(matriz)}) não pode ser invertido mod26!!\033[0m')
            else:
                matriz_mod26_inv = descrip.matriz_inv_mod26(matriz_inversa, det_inverso)
                silabas = crip.separa_silabas(frase, len(matriz))
                silabas_ASCII = crip.array_ASCII(silabas)
                crip_num = crip.criptografar(silabas_ASCII, matriz_mod26_inv)
                mod26 = crip.mod_26(crip_num)
                des = descrip.frase_descriptografada(mod26)

                print(f'\033[0;30mFrase criptografada:\033[1m {des}\033[0m')
        else:
            print(f'\n\033[0;31mError Determinante({descrip.calc_det_cofat(matriz)}) menor que zero!!\033[0m')
    else:
        print('\033[0;31mOpção não existe!!\033[0m')

    t = input('\n\n\n\033[0;30mDeseja Continuar?[S/N]\033[0m').upper()[0]