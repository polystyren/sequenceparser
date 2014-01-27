# scons: pySequenceParser

from pySequenceParser import sequenceParser
import tempfile
import os
import shutil

from nose.tools import *

root_path = ''

print("init test !!")

def setUp():
	global root_path
	# for compatibility with python 2...
	#root_path = tempfile.TemporaryDirectory()
	root_path = tempfile.mkdtemp()
	print("setUp:", root_path)
	files_to_create = [
		"plop.txt",
		"foo.001.png",
		"foo.002.png",
		"foo.003.png",
		"foo.006.png",
		"a.1",
		"a.2",
		"4",
		"5",
		"6",
		"11",
		]
	for f in files_to_create:
		# create an empty file
		ff = os.path.join(root_path, f)
		print("ff:", ff)
		open(ff, 'w').close()
	dirs_to_create = [
		"dir1",
		"dir2",
		"dir3",
		"dir_d",
		"dir_f",
		]
	for d in dirs_to_create:
		dd = os.path.join(root_path, d)
		print("dd:", dd)
		os.mkdir(dd)


def tearDown():
	global root_path
	print("tearDown:", root_path)
	shutil.rmtree(root_path)


def testBrowse():
	global root_path
	items = sequenceParser.browse(root_path)
	print("items:", items)
	for item in items:
		print("item:", item)
		print("item:", item._folder)
		print("item:", item._filename)
		print("item:", item._type)
		if item._type == 1:
			print("item seq:", item._sequence.getAbsoluteFirstFilename())
			print("item seq:", item._sequence.getFirstTime(), item._sequence.getLastTime(), item._sequence.getDuration(), item._sequence.getStandardPattern())


