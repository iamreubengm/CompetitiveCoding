#Encode and Decode TinyURL
'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Solution:
We use two dictionaries to record the longUrl and it's encoding, and the encoding and it's longUrl.
We do this to minimise time taken.
The encoding is using the random.sample function to randomly select 6 letters from the alphabet. If that encoding
already exists, we simply create a new one till a unique one is generated.
The decoding process is just looking up the shortened URL (Code) and finding it's longUrl.
'''
from random import sample
class Codec:
    
    def __init__(self):
        self.url={}
        self.code={}
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"
        

    def encode(self,longUrl):
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url:
            c=''.join(sample(self.alphabet,6))
            if c not in self.code:
                self.code[c]=longUrl
                self.url[longUrl]=c
        return 'http://tinyurl.com/'+self.url[longUrl]

        

    def decode(self,shortUrl):
        """Decodes a shortened URL to its original URL.
        """
        return self.code[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
