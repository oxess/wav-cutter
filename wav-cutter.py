#!/usr/bin/env python

import wave

def cut_footage(footage_path, max_duration, footage_dest=None):
	'''
	Cut footage file to max duration in seconds

	Args:
		footage_path (str): Path to footage file
		max_duration (int): Max duration of footage (in seconds)
		footage_dest (str): Destination path to new footage (default: None)
	
	Raises:
		IOError: Files I/O problem
		wave.Error: Wave library errors

	'''
	import math
	from contextlib import closing

	destination_footage_path = footage_dest or footage_path + '.new'

	with closing(wave.open(footage_path, 'rb')) as cf:
		frames = cf.getnframes()
		rate = float(cf.getframerate())
		max_frames = int(math.ceil(max_duration * rate))

		if max_frames > frames:
			max_frames = frames

		with closing(wave.open(destination_footage_path, 'wb')) as nf:
			nf.setnchannels(cf.getnchannels())
			nf.setsampwidth(cf.getsampwidth())
			nf.setframerate(cf.getframerate())
			nf.writeframes(cf.readframes(max_frames))

def main():
	import os
	import sys
	import argparse

	parser = argparse.ArgumentParser(description="Simple wav file cutter")
	parser.add_argument('footage_path', type=str)
	parser.add_argument('max_duration', type=int)
	parser.add_argument('--footage_dest', type=str, default=None)
	args = parser.parse_args()

	try:
		if not os.path.exists(args.footage_path):
			sys.exit("File %s not exists" % args.footage_path)

		if not os.access('.', os.W_OK):
			sys.exit("This directory is not writable")

		cut_footage(args.footage_path, args.max_duration, args.footage_dest)
	except IOError as x:
		sys.exit(x)
	except wave.Error as x:
		sys.exit(x)

if __name__ == "__main__":
	main()
