"""Simple funtion that copy a Dicom to PNG.""" 
 
import os
from pathlib import Path
from pydicom import dcmread
from pydicom.errors import InvalidDicomError
from pydicom.pixel_data_handlers.util import convert_color_space
from PIL import Image

"""Converts a dicom file to png"""
def dicomToPng(path, results_path='results/'):
	try:
		ds = dcmread(path)
		pa = ds.pixel_array
	except:
		# return if not a dicom file or the file is corrupt
		return False
 
	# if array has more dimensions it is a sequence/video 
	if ds.pixel_array.ndim > 3:
		pa = ds.pixel_array[0]
	
	# fix green image
	imgArray = convert_color_space(pa, current='YBR_FULL_422', desired='RGB')
 
	# create image and save
	image = Image.fromarray(imgArray)
	image.save(results_path + Path(path).stem + '.png', format="png")
 
	# image.show()
	return True
