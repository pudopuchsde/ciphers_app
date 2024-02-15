from PIL import Image
import requests


class Picture_encrypt:
    

    def __init__(self):
        self.alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            ',', '.', '!', ':', ';', '/', '\\', '?', '-', '_', '~', '@', '#', '№', '%', '^', '*','(', ')', '{', '}',
            '[', ']', '<', '>', ' ', '\t',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '\'', '\"',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def take_image(self, image_way):
        self.image = Image.open(image_way)

    def image_crypt(self, message, action="encrypt"):
        encrypted_message = []
        pixel = (0, 0)
        for i in range(len(message)):
            if message[i] != '\n':
                alph_index = self.alph.index(message[i])
                rgba = self.image.getpixel(pixel)
                if action == 'encrypt':
                    new_index = (alph_index + abs(rgba[0] - rgba[2])) % (len(self.alph))
                else:
                    new_index = (alph_index - abs(rgba[0] - rgba[2])) % (len(self.alph))
                enc_letter = self.alph[new_index]
                encrypted_message.append(enc_letter)
                pixel = (
                    (pixel[0] + rgba[1]) % self.image.size[0],
                    ((pixel[0] + rgba[1]) // self.image.size[0] + pixel[1]) % self.image.size[1]
                )
        return "".join(encrypted_message)
    
