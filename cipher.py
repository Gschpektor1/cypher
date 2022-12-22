map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
    
    def encode(self, s):
        result = ''
        for i in s:
            result += self.map2[self.map1.find(i)]
        return result
    
    def decode(self, s):
        result = ''
        for i in s:
            result += self.map1[self.map2.find(i)]
        return result