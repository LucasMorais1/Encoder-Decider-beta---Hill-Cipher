import copy
import math


class criptografia:

    def separa_silabas(self, frase, tam):
        letras = 0
        silabas = ''
        cont = 0
        while letras < len(frase):
            if cont <= tam - 1:
                silabas += frase[letras]
                cont += 1
                letras += 1
            else:
                silabas += '_'
                cont = 0
        silabas = silabas.split('_')
        return silabas

    def array_ASCII(self, silabas):
        silabasD = []
        s = []
        for x in silabas:
            for y in x:
                if y != 'Z':
                    s.append(ord(y) - 64)
                else:
                    s.append(0)
            silabasD.append(s)
            s = []
        return silabasD

    def format_frase(self, frase, tam):
        frase = frase.replace(' ', '').upper()
        if len(frase) % tam > 0:
            frase += str(frase[-1]) * (tam - int(len(frase) % tam))
        return frase

    def criptografar(self, silabas_ASCII, matriz):
        crip = []
        crip_num = []
        multiplicacao = 0
        tam = len(matriz)
        # print(silabas_ASCII)
        # print(matriz)
        for s in silabas_ASCII:
            for m in matriz:
                for x in range(tam):
                    multiplicacao += (s[x] * m[x])
                crip.append(multiplicacao)
                multiplicacao = 0
            crip_copy = []
            for z in crip:
                crip_copy.append(int(z))
            crip = crip_copy
            crip_num.append(crip)
            crip = []

        return crip_num

    def mod_26(self, crip_num):
        mod26 = []
        line = []
        for x in crip_num:
            for y in x:
                num = y - ((y // 26) * 26)
                line.append(num)
            mod26.append(line)
            line = []
        return mod26

    def frase_criptografada(self, mod26):
        frase = ''
        for x in mod26:
            for y in x:
                if y != 0:
                    frase += chr(y + 64)
                else:
                    frase += 'Z'
        return frase


class descriptografia:
    def calc_det_cofat(self, matriz):
        mat = copy.deepcopy(matriz)
        if len(mat) == 1:
            return mat[0][0]
        else:
            val_det = 0
            tam = len(mat)
            for x in list(range(tam)):
                val_det += mat[0][x] * (-1) ** (2 + x) * self.calc_det_cofat(self.menor(mat, x))
            return val_det

    def menor(self, mat, i):

        mat_menor = copy.deepcopy(mat)

        del mat_menor[0]
        for k in list(range(len(mat_menor))):
            del mat_menor[k][i]
        return mat_menor

    def matriz_2x2(self, matriz):
        det = self.calc_det_cofat(matriz)
        novaMatriz = [[], []]
        novaMatriz[0].append(matriz[1][1])
        novaMatriz[0].append(matriz[0][1] * (-1))
        novaMatriz[1].append(matriz[1][0] * (-1))
        novaMatriz[1].append(matriz[0][0])
        return novaMatriz

    def matriz_3x3(self, m):
        pares = []
        cont = 0
        det = self.calc_det_cofat(m)
        if det != 0:
            for x in range(3):
                for y in range(3):
                    cont += 1
                    matriz = []
                    # ---------------------
                    for wxz in m:
                        s = ''
                        for vxy in wxz:
                            s += str(vxy) + '_'
                        matriz.append(list(map(int, s.strip('_').split('_'))))
                    # ---------------------
                    copy_matriz = [matriz[0], matriz[1], matriz[2]]

                    copy_matriz.remove(copy_matriz[x])
                    for z in range(2):
                        copy_matriz[z].remove(copy_matriz[z][y])

                    pares.append([copy_matriz, x + 1, y + 1])

            mi = []
            for x in pares:
                v = math.pow(-1, x[1] + x[2]) * ((x[0][0][0] * x[0][1][1]) - (x[0][0][1] * x[0][1][0]))
                if v - int(v) == 0:
                    mi.append(int(v))
                else:
                    mi.append(v)

            m = [[mi[0], mi[3], mi[6]], [mi[1], mi[4], mi[7]], [mi[2], mi[5], mi[8]]]
            return m
        else:
            return 'ERROR, sua matriz possui determinante igual a zero!!'

    def matriz_inversa(self, matriz):
        if len(matriz) == 2:
            return self.matriz_2x2(matriz)

        elif len(matriz) == 3:
            return self.matriz_3x3(matriz)

    def mod_26_inverso(self, det):
        tabela = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}
        if det < 0:
            det *= -1
        if det > 26:
            det -= ((det//26)*26)
        for x, k in tabela.items():
            if x == det:
                return int(k)
        return 'NÃO EXISTE'

    def matriz_inv_mod26(self, matriz, det_inverso):

        t = len(matriz)
        nova_matriz = []
        for x in range(t):
            linha = []
            for y in range(t):
                v = matriz[x][y] * det_inverso
                if v < -26:
                    v *= -1
                if v > 26:
                    v = v-((v//26)*26)
                v = round(v, 4)
                linha.append(v)
            nova_matriz.append(linha)
        return nova_matriz

    def frase_descriptografada(self, mod26):
        frase = ''
        for x in mod26:
            for y in x:
                if y != 0:
                    frase += chr(y + 64)
                else:
                    frase += 'Z'
        return frase
