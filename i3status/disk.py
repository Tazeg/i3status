#!/usr/bin/env python3

import psutil

print(psutil.disk_usage('/').percent, end='')
