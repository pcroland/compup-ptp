#!/usr/bin/env python3
import argparse
import glob
import re
import signal
import subprocess
import sys

import requests

apikey = 'your-api-key'

def ptpimg(fl):
    files = {
        'file-upload': (fl, open(fl, 'rb')),
        'api_key': (None, apikey),
    }
    r = requests.post('https://ptpimg.me/upload.php', files=files).json()[0]
    return 'https://ptpimg.me/{}.{}'.format(r['code'], r['ext'])

parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-h', '--help',
                    action='help',
                    default=argparse.SUPPRESS,
                    help='Shows this help message.')
parser.add_argument('-v', '--version',
                    action='version',
                    version='compup 1.0',
                    help='Shows version.')
parser.add_argument('-i', '--images',
                    nargs='*',
                    default=argparse.SUPPRESS,
                    help='image sources.\n(default: *.png)')
parser.add_argument('-c', '--compares',
                    default='source, encode',
                    help='compare names, comma separated.\n(default: source, encode)')
parser.add_argument('-o', '--oxipng',
                    action='store_true',
                    help='use oxipng before uploading.\n(default: false)')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

signal.signal(signal.SIGINT, signal.SIG_DFL)

names = re.sub('\\s*,\\s*', ',', args.compares).split(',')
names = [x for x in names if x]

names = ', '.join(names)

print('[comparison=' + names + ']', end='', flush=True)

if not args.images:
    args.images = glob.glob('*.png')

counter = 0

for image in args.images:
    counter += 1

    if args.oxipng:
        subprocess.run(['oxipng', '-q', '-i', '0', '--strip', 'safe', image])

    url = ptpimg(image)

    if counter == len(args.images):
        print(url + '[/comparison]')
    else:
        print(url, end=' ', flush=True)
