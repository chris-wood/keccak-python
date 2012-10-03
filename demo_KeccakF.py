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

A=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

myKeccak=Keccak.Keccak(1600)

myKeccak.KeccakF(A, True)

myKeccak.printState(A,'Final result')
