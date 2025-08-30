class Solution:
    def generateTag(self, caption: str) -> str:
        # step 1 split
        words = caption.strip().split()

        if not words:
            return "#"

        camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
        
        result = "#" + "".join(_ for _ in camel if _.isalpha())
        return result[:100]
