#!/usr/bin/env python3

def make_array(word):
    word_lookup = [None] * 26
    
    for char in word:
        index = ord(char) - 97
        word_lookup[index] = True
    
    return word_lookup

def find_chains_for_word(word_array, previous_longest_chain_length):
    chain_length_to_beat = previous_longest_chain_length
    running_total_chain_length = 0
    longest_chains_for_word = None
    working_chain = ""

    for index in range(len(word_array)):
        # build the chain
        if word_array[index] is not None:
            working_chain += chr(index + 97)
            running_total_chain_length += 1

        # stopping condition, check if longest chain and add to solution in word
        if index == len(word_array) - 1 or word_array[index] == None:

            # if longest, record that and remove old entries
            if running_total_chain_length > chain_length_to_beat:
                chain_length_to_beat = running_total_chain_length
                longest_chains_for_word = [working_chain]

            # if equal, add to found chains
            elif running_total_chain_length == chain_length_to_beat:
                if longest_chains_for_word is not None:
                    longest_chains_for_word.append(working_chain)
                else:
                    longest_chains_for_word = [working_chain]

            # if not long enough, ignore

            #reset
            running_total_chain_length = 0
            working_chain = ""
            
    if longest_chains_for_word == None:
        return None, previous_longest_chain_length
    else:
        return longest_chains_for_word, chain_length_to_beat

def longest_chain(words):
    working_longest_chains = {}
    overall_longest_chain_length = 0

    for word in words:
        if word == "":
            continue
    
        word_array = make_array(word)
        longest_chains_from_word, chain_length_to_beat = find_chains_for_word(word_array, overall_longest_chain_length)
        
        # if we have a valid longest chain to add
        if longest_chains_from_word is not None:
        
            # if the new chain length is longer, reset the longest chain lookup
            if chain_length_to_beat > overall_longest_chain_length:
                overall_longest_chain_length = chain_length_to_beat
                working_longest_chains = {}

            #add chains to dictionary
            for chain in longest_chains_from_word:
                if working_longest_chains.get(tuple(chain,)):
                    working_longest_chains[tuple(chain,)].append(word)
                else:
                    working_longest_chains[tuple(chain,)] = [word]
                    
    print("longest chains are:")
    for chain, words in working_longest_chains.items():
        print(chain, words)
        
longest_chain(["abcd", "abcfd", "abrerg"])

longest_chain([""])

longest_chain(["", "a", "", "b"])