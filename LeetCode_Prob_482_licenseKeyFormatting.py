class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key = "".join([val.upper() for val in list(s) if val.isalnum()])
        if len(key) % k == 0:
            return "-".join([key[i:i+k] for i in range(0, len(key)-k+1, k)])
        else:
            starting = len(key) % k
            output = key[:starting] + "-" + "-".join([key[i:i+k] for i in range(starting, len(key)-k+1, k)])
            return output.rstrip("-")