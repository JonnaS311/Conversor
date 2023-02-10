class Conversor:
    def __init__(self):
        self.dicBinToOct = {
            '000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'
        }
        self.dicBinToHex = {
            '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8','1001': '9','1010': 'A','1011': 'B','1100': 'C','1101': 'D','1110': 'E','1111': 'F'
        }
        self.dicOctToBin = {
            '0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'
        }

    def dec_bin(self, decimal:int)->str:
        binario = ''
        while decimal !=0:
            binario += str(decimal%2)
            decimal = decimal//2
        if binario == '':
            binario = '0'
        return binario[::-1]

    def dec_oct(self,decimal:int)->str:
        octal = ''
        while decimal != 0:
            octal += str(decimal%8)
            decimal = decimal // 8
        if octal == '':
            octal = '0'
        return octal[::-1]

    def dec_hex(self,decimal:int)->str:
        hex = ''
        while decimal != 0:
            if decimal%16 > 9:
                if decimal%16 == 10:
                    hex += 'A'
                elif decimal%16 == 11:
                    hex += 'B'
                elif decimal%16 == 12:
                    hex += 'C'
                elif decimal%16 == 13:
                    hex += 'D'
                elif decimal%16 == 14:
                    hex += 'E'
                elif decimal%16 == 15:
                    hex += 'F'
            else:
                hex += str(decimal % 8)
            decimal = decimal // 16
        if hex == '':
            hex = '0'
        return hex[::-1]

    def bin_oct(self, binario:str):
        list = []
        oct = ''
        for i in range(len(binario)//3):
            list.append(binario[-3*(i+1):len(binario)-(i*3)])
        binario = binario[0:len(binario)-3*(len(binario)//3)]
        if binario != '':
            if len(binario)%3 == 1:
               list.append(f'00{binario}')
            elif len(binario)%3 == 2:
                list.append(f'0{binario}')
        for i in range(len(list)):
            oct += self.dicBinToOct[list[i]]
        return oct[::-1]

    def bin_dec(self,binario:str)->int:
        binario = binario[::-1]
        dec = 0
        for i in range(len(binario)):
            if binario[i] == '1':
                dec += pow(2,i)
        return dec

    def bin_hex(self,binario:str):
        list = []
        hex = ''
        for i in range(len(binario) // 4):
            list.append(binario[-4 * (i + 1):len(binario) - (i * 4)])
        binario = binario[0:len(binario) - 4 * (len(binario) // 4)]
        if binario != '':
            if len(binario) % 4 == 1:
                list.append(f'000{binario}')
            elif len(binario) % 4 == 2:
                list.append(f'00{binario}')
            elif len(binario) % 4 == 3:
                list.append(f'0{binario}')
        for i in range(len(list)):
            hex += self.dicBinToHex[list[i]]
        return hex[::-1]
        pass

    def oct_bin(self,octal:str)->str:
        bin = ''
        for i in range(len(octal)):
            bin += self.dicOctToBin.get(octal[i])
            pass
        return bin

    def oct_dec(self,octal:str)->int:
        octal = octal[::-1]
        dec = 0
        for i in range(len(octal)):
                dec += int(octal[i])*pow(8, i)
        return dec

    def oct_hex(self,octal:str)->str:
        tmp = self.oct_bin(octal)
        print(tmp)
        return self.bin_hex(tmp)

    def hex_bin(self, hexa:str)->str:
        tmp = self.hex_dec(hexa)
        return self.dec_bin(tmp)

    def hex_oct(self, hexa:str)->str:
        tmp = self.hex_dec(hexa)
        return self.dec_oct(tmp)

    def hex_dec(self, hexa:str)->int:
        hexa = hexa[::-1]
        dec = 0
        for i in range(len(hexa)):
            if hexa[i].isdigit():
                dec += int(hexa[i])*pow(16,i)
            else:
                if hexa[i] == 'A':
                    dec += 10*pow(16,i)
                elif hexa[i] == 'B':
                    dec += 11*pow(16,i)
                elif hexa[i] == 'C':
                    dec += 12*pow(16,i)
                elif hexa[i] == 'D':
                    dec += 13*pow(16,i)
                elif hexa[i] == 'E':
                    dec += 14*pow(16,i)
                elif hexa[i] == 'F':
                    dec += 15*pow(16,i)
        return dec
