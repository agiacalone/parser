#!/usr/bin/python3

class parser_tokens:
        token_lookup = [0,"library","program","id",";","var",":",",","int","real","sci","currency",
                        "string","begin","return",":=","device_open","file","for","to","do","repeat",
                        "until","(",")","while","if","then","else","device_close","read_from_device",
                        "write_to_device","writeln","readln","<",">","<=",">=","==","!=","+","-","*",
                        "/","abs","fabs","stop","$"]

        
        parse_val_dict = { 1:[4,2,3],
                           2:[4],
                           3:[2,3],
                           5:[-1],
                           6:[5],
                           8:[23,12,6,-4,-3,-2],
                           9:[7,-4,11,-6,8,-5],
                          10:[7,-4,11,-6,8],
                          12:[9,10],
                          13:[9,10,-7],
                          15:[-3],
                          16:[-8],
                          17:[-9],
                          18:[-10],
                          19:[-11],
                          20:[-12],
                          21:[-4,-8,-14,13,-13],
                          22:[14,15],
                          23:[14,15],
                          25:[-4,18,-15,-3],
                          26:[-4,-17,-16],
                          27:[-4,-20,23,13,-20,-3,-19,-3,-15,-3,-18],
                          28:[-4,-20,23,-24,16,-23,-22,13,-20,-21],
                          29:[-4,-20,23,13,-20,-24,16,-23,-25],
                          30:[-4,23,13,-13,-28,-4,23,13,-13,-27,-24,16,-23,-26],
                          31:[-4,-17,-29],
                          32:[-4,-17,-30],
                          33:[-4,-17,-31],
                          34:[-4,-24,18,-23,-32],
                          35:[-4,-24,8,-23,-33],
                          36:[18,17,18],
                          37:[-34],
                          38:[-35],
                          39:[-36],
                          40:[-37],
                          41:[-38],
                          42:[-39],
                          43:[19,20],
                          44:[-12],
                          45:[19,20,-40],
                          46:[19,20,-41],
                          48:[21,22],
                          49:[21,22,-42],
                          50:[21,22,-43],
                          52:[-24,18,-23],
                          53:[-3],
                          54:[-8],
                          55:[-9],
                          56:[-10],
                          57:[-11],
                          58:[-24,18,-23,-44],
                          59:[-24,18,-23,-45],
                          60:[-46]
                          }
        
        
        def get_token(token):       
            try:
                tval = parser_tokens.token_lookup.index(token)
            except:
                return 0
            
            # return the negative index value of the item
            return tval * -1
        
        def get_val(token):
            if token == 0:
                print("Read error")
                exit(1)
                
            elif token == 61:
                print("Scan error")
                exit(1)
            
            elif token == 62:
                print("Pop error")
                exit(1)
                
            try:
                pval = parser_tokens.parse_val_dict[token]
            except:
                return []       # this is the LAMBDA case
                
            return pval
