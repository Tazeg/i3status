#!/usr/bin/env python3

import psutil

print(psutil.virtual_memory()[2], end='')
