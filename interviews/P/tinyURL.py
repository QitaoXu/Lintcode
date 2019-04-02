class Codec:
    
    def __init__(self):
        
        self.count = 0
        self.count_to_url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count_to_url[self.count] = longUrl
        return "http://tinyurl.com/" + str(self.count)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        for i in range(len(shortUrl)):
            
            if shortUrl[i].isdigit():
                
                break
                
        key_count = int(shortUrl[i:])
        return self.count_to_url[key_count]
        
   
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))