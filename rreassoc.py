#!/usr/bin/python

import sys
import os
import re
import argparse

masterdict = {}
partial = ''

parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='verbose', type=int, choices=[0, 1, 2, 3], help='verbosity level')
parser.add_argument('tree', help='source tree containing R.java files')
args = parser.parse_args()

def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if re.match(pattern, basename):
				filename = os.path.join(root, basename)
				yield filename

# Build the R map
for file in find_files(args.tree, r'R(\$.*|)\.java$'):
	f = open(file, 'r')
	fparray = file.split('/')
	#path = '.'.join(fparray[fparray.index("src")+1:-1]) + "."
	print 'Processing ' + file
	for line in f:
		line = line.strip()
		if line.startswith('public static final class'):
			parts = line.split(' ')
			partial = 'R.' + parts[4] + '.'
		elif line.startswith('public static final int'):
			try :
				parts = line.replace(' = ', '=', 1).rsplit(' ', 1)[1].split('=')
				idx = int(parts[1][:-1], 0)
				if (idx > 100000): # Heuristic
					assoc = partial + parts[0]
					if args.verbose >= 2:
						print assoc + ' = ' + str(idx)
					masterdict[idx] = assoc
			except:
				pass

if args.verbose >= 3: print repr(masterdict)

replacements = 0
files = 0

# Go through all the java files and make replacements
for file in find_files(args.tree, r'.*\.java$'):
	if re.match(r'.*\/R(\$.*|)\.java$', file):
		if args.verbose >= 1:
			print 'Skipping ' + file
		continue
	f = open(file, 'r')
	content = f.read();
	f.close()
	matches = re.finditer('\d\d\d\d\d\d*', content)
	was_match = False
	for match in matches:
		key = int(match.group())
		val = masterdict.get(key)
		if val:
			was_match = True
			replacements += content.count(str(key))
			content = content.replace(str(key), val)
			if args.verbose >= 1:
				print str(file) + ': ' + str(key) + ' -> ' + val
	if was_match:
		files += 1
		f = open(file, 'w')
		f.write(content)
		f.close()

print 'Reassociated %s R.* references in %s files' % (replacements, files)
