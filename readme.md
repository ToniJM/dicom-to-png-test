# Dicom to PNG simple script
## Description
This repository contains simple scripts for testing purposes.
These scripts convert all dicom files in a directory to png.
It also allows us to compare execution times using a single process versus time using 4 workers over multiprocessing.
## Requeriments
- python 3.9
- timeit
- matplotlib
- pydicom
- pillow
- numpy
## Instructions
To regenerate the png image comparing single process vs multiprocess:
```
python compare.py
```
To run the single process:
```
python singleprocess.py
```
To run the four woker multiprocess:
```
python singleprocess.py
```