#!/usr/bin/env python
# Author: Nick Zwart
# Date: 2016dec09
# Brief: This script runs tar on the given file or directory then runs md5sum
# on the resulting tar.

md5sum = '/opt/local/bin/gmd5sum'
tar = '/usr/bin/tar'
nice = '/usr/bin/nice'
time = '/usr/bin/time'
rm = '/bin/rm'

import os
import sys
import subprocess as sp

if len(sys.argv) != 2:
    print("USAGE: %s <path>" % sys.argv[0])
    print("Output: <path>.tar <path>.tar.md5sum")
    sys.exit(1)

# input params
path = sys.argv[1]
output_tar = path+'.tar'
output_md5 = output_tar+'.md5'

# print usage if needed
if not os.path.exists(path):
    print("Invalid Path: %s" % path)
    sys.exit(1)

def check_output(fn):
    if os.path.exists(fn):
        print("Output File Already Exists: %s" % fn)
        print("Removing File...")
        sp.check_call("%s -v %s" % (rm, fn), shell=True)

# delete target files if they exist
check_output(output_tar)
check_output(output_md5)

# perform tar and md5sum
if os.path.exists(path):
    print("Performing TAR on %s..." % path)
    sp.check_call("%s %s -n 19 %s cvf %s %s" % (time, nice, tar, output_tar, path), shell=True)
    print("Performing MD5SUM on %s..." % output_tar)
    sp.check_call("%s %s > %s" % (md5sum, output_tar, output_md5), shell=True)
