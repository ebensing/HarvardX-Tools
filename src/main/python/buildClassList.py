#!/usr/bin/env python
'''
Created on Sep 21, 2013

@author: waldo
'''

import glob
import sys
import os

def reduceName(flist):
    '''
    Return a list of classes whose data is being dealt with
    
    This routine takes the file names supplied by edX and returns a
    list of classes that can be used to isolate the data files by
    course. The current algorithm simply removes the 'HarvardX-'
    prefix, and the '.mongo' extension; it assumes that it is fed 
    only the results of the an operation that will give examplars
    of the *.mongo files supplied. 
    
    This is something of a hack. As we continue to talk with edX 
    about naming conventions, this should be one of the few places
    that will require change.
    '''
    clist = []
    for f in flist:
        if 'HarvardX-' in f:
            clist.append(f[9: -6])
        else:
            clist.append(f[ :-6])
    return clist

def writeList(of, cl):
    '''
    Writes a class list passed in as cl to the open file of
    
    Saves a classlist to a file. The file must be opened for write
    or append. The contents of cl will be written one entry per line
    '''
    for c in cl:
        of.write(c + '\n')

def readList(inf):
    '''
    Reads a classlist from the open file inf and returns a list
    
    Returns a list of the contents of inf, with each entry in the
    list being a single line of the file. Intended to return a 
    classlist of the type written by writeList, with the newline removed
    '''
    cl = [];
    for line in inf:
        cl.append(line[ :-1])
    return cl

if __name__ == '__main__':
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    flist = glob.glob('*.mongo')
    clist = reduceName(flist)
    ofile = open('WeeklyClassList', 'w')
    writeList(ofile, clist)
    
