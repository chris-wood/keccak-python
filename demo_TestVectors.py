#! /usr/bin/pythonw
# The Keccak sponge function, designed by Guido Bertoni, Joan Daemen,
# Michaël Peeters and Gilles Van Assche. For more information, feedback or
# questions, please refer to our website: http://keccak.noekeon.org/
# 
# Implementation by Renaud Bauvin,
# hereby denoted as "the implementer".
# 
# To the extent possible under law, the implementer has waived all copyright
# and related or neighboring rights to the source code in this file.
# http://creativecommons.org/publicdomain/zero/1.0/

import Keccak
import os

## Iterate through the files 'Short... and LongMsgKAT_XXX.txt' containing the
## test vectors and compare the computed values to the provided ones
## In case of difference, it stops the processing and print a message

dirTestVector=os.path.abspath(os.path.join('.'))
verbose=False
instances=[
#    ['r40c160', 40, 160, 0],
#    ['r144c256', 144, 256, 0],
#    ['r544c256', 544, 256, 0],
#    ['r1344c256', 1344, 256, 0],
    ['0', 1024, 576, 0],
    ['224', 1152, 448, 224],
    ['256', 1088, 512, 256],
    ['384', 832, 768, 384],
    ['512', 576, 1024, 512]
]
fileTypes=['Short']
#fileTypes=['Short', 'Long']


#String comparison function (useful later to compare test vector and computation
def sameString(string1, string2):
    """Compare 2 strings"""

    if len(string1)!=len(string2):
        return False
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            return False
    return True

#Create an instance
myKeccak=Keccak.Keccak()

for instance in instances:
    [suffix, r, c, n] = instance
    for fileType in fileTypes:
        print('Processing file: %sMsgKAT_%s.txt...' % (fileType, suffix))

        #Open the corresponding file
        try:
            reference=open(os.path.join(dirTestVector,fileType+('MsgKAT_%s.txt' % suffix)), 'r')
        except IOError:
            print("Error: test vector files must be stored in %s" % (dirTestVector))
            exit()

        #Parse the document line by line (works only for Short and Long files)
        for line in reference:
            if line.startswith('Len'):
                Len=int(line.split(' = ')[1].strip('\n\r'))
            if line.startswith('Msg'):
                Msg=line.split(' = ')[1].strip('\n\r')
            if (line.startswith('MD') or line.startswith('Squeezed')):
                MD_ref=line.split(' = ')[1].strip('\n\r')
                # If line starts with 'Squeezed', use the output length from the test vector
                if line.startswith('Squeezed'):
                    n = (len(MD_ref)//2)*8
                elif n == 0:
                    print("Error: the output length should be specified")
                    exit()

                # Perform our own computation
                MD_comp=myKeccak.Keccak((Len,Msg), r, c, n, verbose)

                #Compare the results
                if not sameString(MD_comp,MD_ref):
                    print('ERROR: \n\t type=%s\n\t length=%d\n\t message=%s\n\t reference=%s\n\t computed=%s' % (suffix, Len, Msg, MD_ref, MD_comp))
                    exit()

        print("OK\n")
        reference.close()
