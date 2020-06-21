#!/usr/bin/env python3

import psutil

print(psutil.cpu_percent(interval=1), end='')
