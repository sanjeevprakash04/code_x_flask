import pandas as pd
from xml.etree.ElementTree import ElementTree as ET

xmltree = ET()

baseFile = xmltree.parse(r'export\rungs\Rungs0to60_from_R042_FRQ.l5x')
newFile = xmltree.parse(r'export\rungs\RA_RUNGS_FRQ.l5x')

baseFileIter = xmltree.iter('Tag')
newFileIter = xmltree.iter('Tag')

test1 = baseFile.find('Description').text
test2 = newFile.find('Description').text


for i in newFileIter:
    for x in baseFileIter:
        if test1 == test2:
            print("Yes!")