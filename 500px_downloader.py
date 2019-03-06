#! /usr/bin/env python3

import os
import subprocess
import argparse
import download as d

DOWNLOAD_FOLDER=subprocess.run(["xdg-user-dir","DOWNLOAD"],stdout=subprocess.PIPE).stdout.decode("utf-8").strip() 


parser = argparse.ArgumentParser(description="A simple 500px image downloader.",epilog='''
    Released under GPL v3.
    (c) 2019 Massimo Girondi
    https://github.com/MassimoGirondi/500px_downloader''')
parser.add_argument("urls", metavar="url", type=str, nargs='+', help="The URL of the image")
parser.add_argument("--folder", dest="folder", help="The folder to save the file (optional, default is "+DOWNLOAD_FOLDER+")")
parser.set_defaults(folder=DOWNLOAD_FOLDER)
args = parser.parse_args()


for u in args.urls:
    d.downloader(u,args.folder)
