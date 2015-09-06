"""
Author  - Alex Boese Sept 2015
Purpose - Basic File manipulation for image uploads 

To Do   - Change Filename to describe time and/or detection of objects
"""
#!/usr/bin/env python3
import os
import shutil
import sys
import exifread
import datetime
# Open image file for reading (binary mode)


dr  = sys.argv[1]
dr2 = sys.argv[2]
files = os.listdir(dr)
for f in [f for f in files if os.path.isfile(dr+"/"+f)]:
    ff = open(dr+"/"+f, 'rb')
    tags = exifread.process_file(ff)
    try:
        temp = str(tags['EXIF DateTimeOriginal'])
        ts = datetime.datetime.strptime(temp, "%Y:%m:%d %H:%M:%S")
        folder = str(ts.year) + '_' + str(ts.month) + '_' + str(ts.day)

        if not os.path.exists(folder):
            os.makedirs(folder)
        shutil.move(dr+"/"+f, dr2 + "/" +folder+"/"+f)
        print("Moved "+ f + "  to " + folder)
    except:
        #e = sys.exc_info()[0]
        #print("Error: "+ str(e))
        print("skipped "+f)        
