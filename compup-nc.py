#!/usr/bin/env python3
import argparse
import glob
import math
import os
import re
import signal
import subprocess
import sys

import requests

def keksh(fl):
    files = {'file': open(fl, 'rb')}
    r = requests.post('https://kek.sh/api/v1/posts', files=files).json()['filename']
    link = 'https://i.kek.sh/' + r
    return link

parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-h', '--help',
                    action='help',
                    default=argparse.SUPPRESS,
                    help='shows help message')
parser.add_argument('-v', '--version',
                    action='version',
                    version='compup 1.0',
                    help='show version')
parser.add_argument('-i', '--images',
                    nargs='*',
                    default=argparse.SUPPRESS,
                    help='image sources.\n(default: *.png)')
parser.add_argument('-c', '--compares',
                    default='source, encode',
                    help='compare names, comma separated.')
parser.add_argument('-n', '--number',
                    default=argparse.SUPPRESS,
                    help='number of images in a row. (default: number of compare names)')
parser.add_argument('-w', '--width',
                    default='500',
                    help='width of the image row')
parser.add_argument('-o', '--oxipng',
                    action='store_true',
                    help='use oxipng before uploading')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

signal.signal(signal.SIGINT, signal.SIG_DFL)

names = re.sub('\\s*,\\s*', ',', args.compares).split(',')
names = [x for x in names if x]

if hasattr(args, 'number'):
    length = int(args.number)
else:
    length = len(names)

names = ' vs. '.join(names)

width = math.floor(int(args.width) / length - 5)
#print(thumb_width)

print('[center][size=12pt][highlight]' + names + '[/highlight][/size]\n')

if not args.images:
    args.images = glob.glob('*.png')

counter = 0

for image in args.images:
    counter += 1

    if args.oxipng:
        subprocess.run(['oxipng', '-q', '-i', '0', '--strip', 'safe', image])

    subprocess.run(['ffmpeg', '-y', '-v', 'quiet', '-i', image, '-vf', f'scale={width}:-1', 'temp.jpg'])
    url = keksh(image)
    thumb_url = keksh('temp.jpg')

    if counter == len(args.images):
        print('[url=' + url + '][img]' + thumb_url + '[/img][/url][/center]')
    else:
        if not counter % length == 0:
            print('[url=' + url + '][img]' + thumb_url + '[/img][/url] ', end='', flush=True)
        else:
            print('[url=' + url + '][img]' + thumb_url + '[/img][/url]')

os.remove('temp.jpg')
