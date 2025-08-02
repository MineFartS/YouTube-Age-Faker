from philh_myftp_biz import *
import sys

m = sys.argv[1].lower()

print(m)

if m == 'setup':
    ''
    
elif m == 'run':
    
    with web.browser() as b:
        b.open('https://YouTube.com')
