import base64

class Codec:
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded_string = base64.b64encode(longUrl.encode("ascii"))
        return encoded_string


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded_string = base64.b64decode(shortUrl)
        return decoded_string.decode("ascii")