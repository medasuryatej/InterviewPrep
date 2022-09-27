class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        while True:
            new_doms = dominoes.replace("R.L", "|").replace(".L", "LL").replace("R.", "RR").replace("|", "R.L")
            if new_doms == dominoes:
                break
            dominoes = new_doms
        return dominoes
            
            
                    
            
        
        
        