#!/usr/bin/env python

import os, sys
from ast import literal_eval as make_tuple

def rle(file_to_encode):
    encoded=[]

    with open(os.path.abspath(os.path.expanduser(file_to_encode)), 'rb') as f:
        chunk=f.read()
        if len(chunk)==0:
            print 'empty file'
            sys.exit(1)

    char = chunk[0]
    count = 1
    for i in xrange(1, len(chunk)):
        if chunk[i]==char:
            count+=1
        else:
            encoded.append((char, count))
            char=chunk[i]
            count=1
    return '\n'.join(str(t) for t in encoded) # separate each pair with newline, easier to parse

def rld(file_to_decode):
    decoded=[]

    with open(os.path.expanduser(os.path.expanduser(file_to_decode)), 'rb') as f:
        while True:
            chunk = f.readline().strip()
            # chunk=f.read(2)
            # print chunk
            if chunk != '':
                # print chunk, type(chunk)
                t = make_tuple(chunk)
                decoded.extend(t[0] * t[1])
                # decoded.extend(chunk[1]*int(chunk[0]))
                # print chunk[1]
                # print chunk[0]
                # print 'int:', int(chunk[0])
                # tmp+=1
            else:
                break
        # decoded_text=f.read(2)
        # print decoded_text[0], decoded_text[1]
        # while decoded_text != '':
        #     decoded.extend(decoded_text[1] * int(decoded_text[0]))
        #     # decoded.extend([decoded_text[1] for i in range(int(decoded_text[0]))])
        #     decoded_text=f.read(2)
        #     # print decoded_text[0], decoded_text[1]

    decoded=''.join(decoded)
    return decoded

if __name__ == '__main__':
    if len(sys.argv)>4:
        print 'usage: python week1.py [-e|-d] input output'
        sys.exit(1)
    elif len(sys.argv)==4:
        if '-e' in sys.argv:
            ind=sys.argv.index('-e')
            del sys.argv[ind]
            infile=sys.argv[1]
            outfile=sys.argv[2]
            encoded=rle(infile)
            with open(os.path.abspath(os.path.expanduser(outfile)), 'wb') as f:
                f.write(encoded)
            print 'file is successfully encoded.'
        elif '-d' in sys.argv:
            ind=sys.argv.index('-d')
            del sys.argv[ind]
            infile=sys.argv[1]
            outfile=sys.argv[2]
            decoded=rld(infile)
            with open(os.path.abspath(os.path.expanduser(outfile)), 'wb') as f:
                f.write(decoded)
            print 'file is successfully decoded.'
        else:
            print 'usage: python week1.py [-e|-d] input output'
            sys.exit(1)
    elif len(sys.argv)==3 and '-e' not in sys.argv and '-d' not in sys.argv:
        infile=sys.argv[1]
        outfile=sys.argv[2]
        encoded=rle(infile)
        with open(os.path.abspath(os.path.expanduser(outfile)), 'wb') as f:
            f.write(encoded)
        print 'file is successfully encoded.'
    else:
        print 'usage: python week1.py [-e|-d] input output'
        sys.exit(1)
