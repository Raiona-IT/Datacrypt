#!/usr/bin/python

import os
import argparse

parser = argparse.ArgumentParser(description='Hide file(s) in an image')
mutex = parser.add_mutually_exclusive_group(required=True)
parser.add_argument('image', metavar='IMG', help='The image where the file(s) will be hidden')
mutex.add_argument('-d', '--decrypt', action='store_true', help='Extract any hidden files from the specified image')
mutex.add_argument('-e', '--encrypt', metavar='FILE', nargs='+', help='The file(s) to be hidden')
args = parser.parse_args()

if args.encrypt:
    files = ''
    for item in args.encrypt:
        files = files + ' ' + item
    prefix = 'crypt-'
    dirfiles=os.listdir(os.getcwd())
    valid = 1
    imgname=args.image.split('/')[::-1][0]
    while valid == 1:
        for dirf in dirfiles:
            valid = 0
            if dirf==prefix + imgname:
                prefix = prefix + 'x-'
                valid = 1
    outfile = prefix + imgname
    os.system('cat ' + args.image + ' ' + files + ' > ' + outfile)
elif args.decrypt:
    print args.decrypt
