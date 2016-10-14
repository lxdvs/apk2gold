import sys
import os
import fnmatch
import re

masterdict = {}
partial = ''
verbose = False


def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

# Build the R map
for file in find_files(sys.argv[1], 'R.java'):
	f = open(file, 'r')
	fparray = file.split('/')
	print("Processing: {0}".format(file))
	for line in f:
		line = line.strip()
		if line.startswith('public static final class'):
			parts = line.split(' ')
			partial = 'R.' + parts[4] + '.'
		elif line.startswith('public static final int'):
			try:
				parts = line.split(' ')
				idx = int(parts[6][:-1])
				if (idx > 100000):  # Heuristic
					assoc = partial + parts[4]
					masterdict[idx] = assoc
			except:
				pass

if verbose:
	print(repr(masterdict))

replacements = 0
files = 0

# Go through all the java files and make replacements
for file in find_files(sys.argv[1], '*.java'):
	if file.endswith('/R.java'):
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
			if verbose:
				print(str(file) + " : " + str(key) + "->" + val)
	if was_match:
		files += 1
		f = open(file, 'w')
		f.write(content)
		f.close()

print("Reassociated {0} R.* references in {1} files".format(replacements, files))
