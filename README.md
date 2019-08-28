# python-scripts

## [pw](pw.py) - a python commandline password generator
###### [(view source)](https://github.com/ckrmml/python-scripts/blob/master/pw.py)
#### usage
    python-scripts $ python pw.py --help
    usage: pw.py [-h] [-c int] [-l int] [-a l/u/b] [-n] [-s] [-o] [-v]

    RndmPW (v0.1): just another python cmd-line password generator

    optional arguments:
     -h, --help            show this help message and exit
     -c int, --count int   Number of passwords that get generated (default: 10)
     -l int, --length int  Length of passwords (default: 16)
     -a l/u/b, --alpha l/u/b
                           Use alphabet (lower-case/upper-case/both) (default: b)
     -n, --num             Use numbers (default: False)
     -s, --special         Use special characters (default: False)
     -o, --one-time        Use characters only one time per pw (default: False)
     -v, --version         show program's version number and exit

----------------------------------------------

## [duplicate](duplicate.py) - Find duplicate files
###### [(view source)](https://github.com/ckrmml/python-scripts/blob/master/duplicate.py)
#### usage:
    python-scripts $ python duplicate.py
    Usage: python dupFinder.py folder or python dupFinder.py folder1 folder2 folder3

#### credits:
[Andres Torres](https://www.pythoncentral.io/finding-duplicate-files-with-python/)  

----------------------------------------------

## [progress](progress.py) - Python Progress Bar
###### [(view source)](https://github.com/ckrmml/python-scripts/blob/master/progress.py)
#### usage:
Call in a loop to create terminal progress bar  

    print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):

    iteration   - Required  : current iteration (Int)
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    bar_length  - Optional  : character length of bar (Int)

#### credits:
[aubricus](https://github.com/aubricus)  
[src origin](https://gist.github.com/aubricus/f91fb55dc6ba5557fbab06119420dd6a)  

# License
If not stated otherwise here, `LICENSE = NULL`  
-> ```duplicate.py```: none given at source  
-> ```progress.py```: none given at source
