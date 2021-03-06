# Copyright (C) 2016-2017 Jurriaan Bremer.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

import os

from sflock import unpack

def test_attributes():
    for filename in os.listdir("tests/files"):
        if os.path.isdir("tests/files/%s" % filename):
            continue

        if "encrypted" in filename:
            continue

        f = unpack("tests/files/%s" % filename)
        f.to_dict()
