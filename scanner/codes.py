class codes:
    lookup_codes = ["!accept", "`", "<", ">", "[", "]", "{", "}", "@", "&", "#", "!", "~", "'", "$", 
                    ":", ";", ".", ",", "+", "-", "/", "\\", "*", "=", "^", "(", ")", "id", "int", " ", 
                    "<<", "<>", "<=", ">>", ">=", "!!", "!=", ":=", "++", "+-", "-+", "--", "/=", "==", 
                    "real", "string", "comment", "currency", "file", "library", "sci"]
    
    def getcode(code):
        return codes.lookup_codes[code]
