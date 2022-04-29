from dicom import dicomToPng
from pathlib import Path

def main(path='sample_dicoms'): 
	"""Launcher."""
	# init the GUI or anything else 
	count = 0
	for path in Path('sample_dicoms').rglob('*'):
		if path.is_file():
			st = str(path)
			if dicomToPng(st):
				count = count + 1
				# print(count)
 
if __name__ == "__main__": 
	main() 