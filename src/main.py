#!/usr/bin/env python

import os
import argparse
import logging

import qrcode


logging.basicConfig(format="%(message)s", level=logging.INFO)
parser = argparse.ArgumentParser(epilog='./generate_barcode.exe "My text here" img.png')
parser.add_argument("text", help="")
parser.add_argument("filename", help="")
args = parser.parse_args()

destination_path = os.path.join(os.getcwd(), args.filename)
logging.info("Generating QR code...")
img = qrcode.make(args.text)
img.save(destination_path)
logging.info("SUCCESS: Image saved at {}".format(destination_path))
