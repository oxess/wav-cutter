#!/usr/bin/env python2

import sys
import math
import wave
import argparse
import contextlib

parser = argparse.ArgumentParser(description="Simple wav file cutter")
parser.add_argument('footage_path', type=str)
parser.add_argument('max_duration', type=int)
args = parser.parse_args()

with contextlib.closing(wave.open(args.footage_path, 'rb')) as cf:
	frames = cf.getnframes()
	rate = float(cf.getframerate())

	max_frames = int(math.ceil(args.max_duration * rate))

	if max_frames > frames:
		sys.exit("Footage is to short")

	with contextlib.closing(wave.open(args.footage_path + '.new', 'wb')) as nf:
		nf.setnchannels(cf.getnchannels())
		nf.setsampwidth(cf.getsampwidth())
		nf.setframerate(cf.getframerate())

		nf.writeframes(cf.readframes(max_frames))

print "\n[!] Created new file=%s\n" % args.footage_path + ".new"
	
