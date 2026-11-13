class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        shortUrl = "http://tinyurl.com/" + str(self.counter)

        self.url_map[shortUrl] = longUrl
        self.counter += 1

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))