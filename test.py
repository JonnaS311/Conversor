import conversor as cv


if __name__ == '__main__':
    conversor = cv.Conversor()
    verificador = cv.verificador()

    print(verificador.isHexadecimal('ABCDEFC'))
    #print('->', conversor.dec_oct(100))
    #print('->', conversor.dec_bin(100))
    #print('->', conversor.dec_hex(100))

    #print('->',conversor.hex_oct('AA12'))
    #print('->', conversor.hex_dec('AA12'))
    #print('->', conversor.hex_bin('AA12'))
