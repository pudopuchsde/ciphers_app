class Ciphers:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.len_alphabet = len(self.alphabet)
        self.alphabet_polybium = "abcdefghijklmnopqrstuvwxyz0123456789"  
        self.len_alphabet_digits = len(self.alphabet_polybium)
        self.alphabet_os = "abcdefghijklmnopqrstuvwxyz"

    def generate_Polybium_square(self, alpabet, y_scale, direction=True):
        if direction:
            sl, c1, c2 = {}, 1, 1
            for i in alpabet:
                sl[i] = (c1, c2)
                c2 += 1
                if c2 == y_scale + 1:
                    c1, c2 = c1 + 1, 1
        else:
            sl, c1, c2 = {}, 1, 1
            for i in alpabet:
                sl[(c1, c2)] = i
                c2 += 1
                if c2 == y_scale + 1:
                    c1, c2 = c1 + 1, 1
        return sl

    def Cezarus_cipher(self, source_string, shift):
        self.source_string, self.shift = source_string, shift
        result = []
        for i in self.source_string:
            result.append(self.alphabet[(self.alphabet.find(i) + shift) % self.len_alphabet])

        return ''.join(result)

    def Polybium_cipher_encrypt(self, source_string, y_scale):
        self.data = self.generate_Polybium_square(self.alphabet_polybium, y_scale, True)
        result = []
        for i in source_string:
            result.append(f"{self.data[i][0]}{self.data[i][1]}")

        return ' '.join(result)
    
    def Polybium_cipher_decrypt(self, cipher, y_scale):
        cipher = [(int(i[0]), int(i[1])) for i in cipher.split()]
        self.data = self.generate_Polybium_square(self.alphabet_polybium, y_scale, False)
        result = []
        for i in cipher:
            result.append(self.data[i])

        return ''.join(result)

    def Vigenere_cipher_encrypt(self, source_string, encryption_word):
        source_string = source_string.replace(" ", "")
        len_source_string, len_encryption_word = len(source_string), len(encryption_word)
        len_difference = len_source_string - (len_source_string // len_encryption_word * len_encryption_word)
        encryption_key = f"{(len_source_string // len_encryption_word) * encryption_word}{encryption_word[:len_difference]}"
        result = []
        for i in range(len(source_string)):
            result.append(f"{self.alphabet[int(self.alphabet.find(source_string[i]) + self.alphabet.find(encryption_key[i])) % self.len_alphabet]}")
        
        return ''.join(result)

    def Vigenere_cipher_decrypt(self, cipher, encryption_word):
        cipher = cipher.replace(" ", "")
        len_cipher, len_encryption_word = len(cipher), len(encryption_word)
        len_difference = len_cipher - (len_cipher // len_encryption_word * len_encryption_word)
        encryption_key = f"{(len_cipher // len_encryption_word) * encryption_word}{encryption_word[:len_difference]}"
        result = []
        for i in range(len(cipher)):
            result.append(f"{self.alphabet[int(self.alphabet.find(cipher[i]) - self.alphabet.find(encryption_key[i])) % self.len_alphabet]}")
        
        return ''.join(result)
    
    def private_cipher_encrypt(self, source_string, encryption_word):
        source_string = source_string.replace(" ", "")
        len_source_string, len_encryption_word = len(source_string), len(encryption_word)
        len_difference = len_source_string - (len_source_string // len_encryption_word * len_encryption_word)
        encryption_key = f"{(len_source_string // len_encryption_word) * encryption_word}{encryption_word[:len_difference]}"
        bin_encryption_key = []
        bin_result = []
        bin_cithers = []
        for i in source_string:
            i = ord(i)
            bin_result.append(str(bin(i))[2:])

        for i in encryption_key:
            i = ord(i)
            bin_encryption_key.append(str(bin(i))[2:])
        
        for i in range(len(bin_result)):
            s = ""
            for j in range(len(bin_result[i])):
                s += str(int(bin_result[i][j]) ^ int(bin_encryption_key[i][j]))
            bin_cithers.append(s)

        return (" ".join(bin_cithers), " ".join(bin_encryption_key))
    
    def private_cipher_decrypt(self, bin_cither, bin_encryption):
        bin_cither_list = bin_cither.split()
        bin_encryption_list = bin_encryption.split()
        result = []
        for i in range(len(bin_cither_list)):
            s = ""
            for j in range(len(bin_cither_list[i])):
                if int(bin_cither_list[i][j]) == 1 and int(bin_encryption_list[i][j]) == 1:
                    s += "0"
                if int(bin_cither_list[i][j]) == 0 and int(bin_encryption_list[i][j]) == 0:
                    s += "0"
                if int(bin_cither_list[i][j]) == 1 and int(bin_encryption_list[i][j]) == 0:
                    s += "1"
                if int(bin_cither_list[i][j]) == 0 and int(bin_encryption_list[i][j]) == 1:
                    s += "1"

            result.append(s)
            s = ""

        for i in result:
            s += chr(int(i, 2))
        return s
    
    def os_encode(self, text, clue):
        my_alp = []
        clue_num = 0

        # Постройка своего алфавита
        for i in self.alphabet_os:
            if clue_num == 0:
                my_alp.append([i, (self.alphabet_os.index(i) + clue) * clue + (clue * 2 - 7)])
                clue_num = 1
            else:
                my_alp.append([i, (self.alphabet_os.index(i) + clue) * clue - (clue * 3 + 9)])
                clue_num = 0
        answer = ''

        #Чтобы не втыкал
        for i in text:
            i = self.alphabet_os.index(i.lower())
            answer += str(my_alp[i][1]) + ' '
            my_alp[i][1] += int(clue / 2 * 9)

        return answer

    def os_decode(self, text, clue):
        my_alp = []
        clue_num = 0
        for i in self.alphabet_os:
            if clue_num == 0:
                my_alp.append([i, (self.alphabet_os.index(i) + clue) * clue + (clue * 2 - 7)])
                clue_num = 1
            else:
                my_alp.append([i, (self.alphabet_os.index(i) + clue) * clue - (clue * 3 + 9)])
                clue_num = 0
        answer = ''

        for i in str(text).split():
            for i_1 in my_alp:
                if i_1[1] == int(i):
                    answer += i_1[0]
                    my_alp[my_alp.index(i_1)][1] += int(clue / 2 * 9)
        return answer

# c = Ciphers()
# r1 = c.private_cipher_encrypt("xyzz", "a")
# print(c.private_cipher_decrypt(r1[0], r1[1]))
#print(r2)
# r2 = c.private_cipher_decrypt(r1[0], r1[0])
# print(r1[1])
# print(r2)
#o = c.private_cipher_encrypt("abcd", "a")
# out = c.private_cipher_decrypt('0000000 0000011 0000010 0000101', '1100001 1100001 1100001 1100001')
# print(out)
# i1, i2, i3 = "abcdz", "hello", "hello world"
# c1, c2, c3 = c.Cezarus_cipher(i1, 1), c.Polybium_cipher_encrypt(i2, 7), c.Vigenere_cipher_encrypt(i3, "python")
# d1 = c.Cezarus_cipher(c1, -1)
# d2 = c.Polybium_cipher_decrypt(c2, c.generate_Polybium_square("abcdefghijklmnopqrstuvwxyz", 7, False))
# d3 = c.Vigenere_cipher_decrypt(c3, "python")

# print(i1, i2, i3)
# print(c1, c2, c3)
# print(d1, d2, d3)