class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # return filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n'))
        one_liner_source_code = "\n".join(source)
        expression = re.sub("//.*|/\*(.|\n)*?\*/", "", one_liner_source_code)
        return filter(None, expression.split("\n"))
    
    
    