class Codec:
    
    def __init__(self):
        
        self.hash_to_url = {} 

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.hash_to_url[hash(longUrl)] = longUrl
        return "http://tinyurl.com/" + str(hash(longUrl))
                

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = shortUrl.find("m")
        
        hashcode = int(shortUrl[index + 2:])
        
        return self.hash_to_url[hashcode]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))