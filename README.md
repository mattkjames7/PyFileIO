# PyFileIO
Some very basic  routines for file IO in Python



## Installation

Install via `pip3`:

```bash
pip3 install PyFileIO --user
```

or from this repo:

```bash
git clone https://github.com/mattkjames7/PyFileIO
cd PyFileIO 

#either this
python3 setup.py install --user

#or this
python3 setup.py bdist_wheel
pip3 install dist/PyFileIO-X.X.X-py3-none-any.whl
```

where `X.X.X` is the version created.



## Usage

This module contains a few different methods of loading/saving data.

### Loading/Saving Objects

This effectively uses `pickle` to load and save physical objects, e.g.:

```python
import PyFileIO as pf

#save an object
pf.SaveObject(obj,'/path/to/some/file.bin')

#load an object
obj = pf.LoadObject('/path/to/some/file.bin')
```



### Loading/Saving ASCII Data

Text files may be created and read directly:

```python
#saving text
text = 'some text, can be an array\n or just a single string'
pf.WriteASCIIFile('filename.txt',text)

#reading text
text = pf.ReadASCIIFile('filename.txt')
```

We can also use ASCII files to load `csv` files and save data stored in a simple  `numpy.recarray`:

```python
#read a csv file, which contains a header - dtype will be worked out automatically
data = pf.ReadASCIIData('somedata.csv')

#we can also save data
pf.WriteASCIIData('newfile.dat',data)
```

NOTE: this will only work with simple `dtypes` 



### Loading/Saving Binary Data

Pure binary data may be written to files using the following functions:

```python
#open a file
f = open('filename.bin','wb')

#save some stuff
ScalarToFile(x,'int64',f)		#save a single scalar integer
ArrayToFile(y,'float32',f) 		#save a floating point array
ListArrayToFile(z,'int32',f)	#save a list of integer arrays
StringToFile(s,f)				#save a string to file

#close the file
f.close()
```

We can also read the data back (remembering to use the correct dtypes!):

```python
#open a file
f = open('filename.bin','rb')

#read the stored data
x = ScalarFromFile('int64',f)		#read a single scalar integer
y = ArrayFromFile('float32',f) 		#read a floating point array
z = ListArrayFromFile('int32',f)	#read a list of integer arrays
s = StringFromFile(f)				#read a string from file

#close the file
f.close()
```



