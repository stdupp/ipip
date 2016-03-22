#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import sys

from ipip import IP

IP.load(os.path.abspath("17monipdb.dat"))

query = sys.argv[1]
r = "  ".join(IP.find(query).split("\t"))

output = '''
<?xml version="1.0"?>
    <items>
        <item uid="%s" arg="0" valid="YES" autocomplete="%s">
            <title>%s</title>
            <icon>icon.png</icon>
        </item>
    </items>
''' % (query, query, r)
print output

