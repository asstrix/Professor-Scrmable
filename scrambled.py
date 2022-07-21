# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:57:07 2022

@author: Home
"""
import sys

usage = 'Usage:\n'+'/scrmabled-strings --dictionary [PATH TO DICTIONARY FILE] --input [PATH TO INPUT FILE]'

def chk_dict(dictionary):
    shortestWord = {'word':0, 'lenght':0,'line':0}
    longestWord = {'word':0, 'lenght':0,'line':0}
    shortestWord['word']=min(dct, key=len)
    shortestWord['lenght']=len(min(dct, key=len))
    shortestWord['line']=dct.index(shortestWord['word'])
    longestWord['word']=max(dct, key=len)
    longestWord['lenght']=len(max(dct, key=len))
    longestWord['line']=dct.index(longestWord['word'])
    if len(dct) > 105:
        raise ValueError('The sum of lengths of all words in the dictionary exceeds 105')
    if shortestWord['lenght'] < 2:
        raise ValueError(f"The word '{shortestWord['word']}' in line {shortestWord['line']+1} is less than 2 letters")
    if longestWord['lenght'] > 105:
        raise ValueError(f"The word '{longestWord['word']}' in line {longestWord['line']+1} is more than 105 letters")
     
if len(sys.argv) ==1:
    print(usage)
elif sys.argv[1] != '--dictionary' and sys.argv[3] != '--input':
    print(usage)
else:
    try:
        with open(sys.argv[2],'r') as dct, open(sys.argv[4], 'r') as strings:
            strings = [i.strip('\n') for i in strings.readlines()]
            dct = [i.strip('\n') for i in dct.readlines()]
            chk_dict(dct)
            try:   
                result = {}
                for l in range(0, len(strings)):
                    result.update({f'Case #{l+1}':[]})
                    for d in range(0,len(dct)):
                        for i in range(0,len(strings[l])):
                            if len(strings[l][i:i+len(dct[d])]) == len(dct[d]):
                                if dct[d][0] == strings[l][i:i+len(dct[d])][0] and dct[d][-1] == strings[l][i:i+len(dct[d])][-1]:
                                    if sorted(dct[d][1:-1]) == sorted(strings[l][i+1:i+len(dct[d])-1]):
                                        if dct[d] not in result[f'Case #{l+1}']:
                                            result[f'Case #{l+1}'].append(dct[d])
                for i in result: print(f'{i}: {len(result[i])}')
            except Exception as e: print(e)
    except Exception as e: print(e)      
            
    
    
    
    