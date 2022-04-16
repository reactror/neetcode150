class Solution:
    def encode(self, strs):
        encoded = ''

        for s in strs:
            encoded += '{}{}{}'.format(len(s), "#", s)

        return encoded

    def decode(self, s):
        decoded = []

        i = 0

        while i < len(s):
            num = int(s[i])
            decoded.append(s[i+2:i+num+2])
            
            i += num + 2

        return decoded