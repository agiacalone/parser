#!/usr/bin/python3

# import the tables
from statetable import *
from actiontable import *
from lookuptable import *
from rwords import *
from codes import *
from tokens import *

class scanner:
    def scan_tokens(scanned_file):

        state = 0
        token_status = ""
        counter = 0
        buffered = 0
        id_dict = {}
        final_print = ""
        current_read = 0
        scanned_tokens = []

        while counter < len(scanned_file):
            token = scanned_file[counter]           # token variable is the actual char input
            
            # compare the various tokens and determine state table value
            old_read = current_read
            current_read = tokens.gettoken(token)
            
            if (statetable.gettable(state, current_read) != -1) and (actiontable.gettable(state, current_read) == 1):     
                token_status = token_status + token         # token_status is the accumulated chars
                state = statetable.gettable(state, current_read)
                buffered = 0
            
            elif (statetable.gettable(state, current_read) == -1) and (actiontable.gettable(state, current_read) == 2):
                # Halting condition
                buffered = 1
                result = codes.getcode(lookuptable.gettable(state, current_read))
                if result == "id":
                    if rwords.check_rword(token_status) == True:
                        result = token_status        
                    else:
                        if token_status in id_dict:
                            id_dict[token_status] += 1
                        else:
                            id_dict[token_status] = 1

                if result != "space":
                    scanned_tokens.append(result)
                state = 0
                token_status = ""    # clear the token buffer

            if buffered != 1:
                counter += 1
                
            else: buffered = 0
            # end while loop

        return scanned_tokens
    # end of program
