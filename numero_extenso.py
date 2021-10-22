TRANSCRICAO = [
    [
        'zero',
        'um',
        'dois',
        'três',
        'quatro',
        'cinco',
        'seis',
        'sete',
        'oito',
        'nove'
    ],
    [
        'dez',
        'onze',
        'doze',
        'treze',
        'quartoze',
        'quinze',
        'dezesseis',
        'dezessete',
        'dezoito',
        'dezenove'
    ],
    [
        'vinte',
        'trinta',
        'quarenta',
        'cinquenta',
        'sessenta',
        'setenta',
        'oitenta',
        'noventa'
    ],
    [
        '',
        'cento',
        'duzentos',
        'trezentos',
        'quatrocentos',
        'quinhentos',
        'seiscentos',
        'setecentos',
        'oitocentos',
        'novecentos'
    ]
]


class Numero:
    @staticmethod
    def __centenas(digito):
        return TRANSCRICAO[3][int(digito)]

    @staticmethod
    def __dezenas(dezena, unidade):
        if dezena == '1':
            return TRANSCRICAO[1][int(unidade)]
        else:
            return TRANSCRICAO[2][int(dezena) - 2]

    @staticmethod
    def __unidade(unidade):
        return TRANSCRICAO[0][int(unidade)]

    @staticmethod
    def por_extenso(number):
        number = str(number)
        if not number.isdigit() or len(number) > 3:
            raise ValueError
        cent, deze, uni = number.rjust(3, "0")
        res = ""
        if not (deze == '0' and uni == '0') or \
                (cent == '0' and deze == '0' and uni == '0'):
            if deze not in "1":
                if deze != "0":
                    res = Numero.__dezenas(deze, uni)
                    if uni != "0":
                        res += " e " + Numero.__unidade(uni)
                else:
                    res = Numero.__unidade(uni)
            else:
                res = Numero.__dezenas(deze, uni)
            if Numero.__centenas(cent):
                res = Numero.__centenas(cent) + " e " + res
        elif cent == '1':
            res = "cem"
        else:
            res = Numero.__centenas(cent)
        return res


if __name__ == "__main__":
    for i in range(1000):
        print(f"'{i}': {Numero.por_extenso(i)}")
