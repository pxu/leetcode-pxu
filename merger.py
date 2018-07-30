import shutil
import glob

outfilename="all.txt"
with open(outfilename, 'wb+') as outfile:
	for filename in glob.glob('*.txt'):
		if filename == outfilename:
			# don't want to copy the output into the output
			continue
		with open(filename, 'rb') as readfile:
			outfile.write('\n\n'.encode("utf-8"))
			outfile.write(filename.encode("utf-8"))
			outfile.write('\n\n'.encode("utf-8"))
			shutil.copyfileobj(readfile, outfile)

	for filename in glob.glob('lintcode/*.txt'):
		if filename == outfilename:
			# don't want to copy the output into the output
			continue
		with open(filename, 'rb') as readfile:
			outfile.write('\n\n'.encode("utf-8"))
			outfile.write(filename.encode("utf-8"))
			outfile.write('\n\n'.encode("utf-8"))
			shutil.copyfileobj(readfile, outfile)