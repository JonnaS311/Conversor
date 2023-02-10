import conversor as cv


if __name__ == '__main__':
    conversor = cv.Conversor()
    print('->',conversor.hex_oct('AA12'))
    print('->', conversor.hex_dec('AA12'))
    print('->', conversor.hex_bin('AA12'))
