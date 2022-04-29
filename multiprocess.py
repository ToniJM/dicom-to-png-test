from dicom import dicomToPng
from pathlib import Path
import multiprocessing as mp

def main(path='sample_dicoms'):
	count = 0
	files = []

	# create a pool with 4 workers
	pool = mp.Pool(processes=4)
	for file in Path(path).rglob('*'):
		if file.is_file():
			# fill list of files
			files.append(str(file))
   
	# feed the pool with the list of files
	result = pool.map(dicomToPng, files)
 
if __name__ == "__main__": 
	main() 