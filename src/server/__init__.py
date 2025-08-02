import sys, subprocess

m = sys.argv[1].lower()

def installPKG(pkg):
    subprocess.run([sys.executable, '-m', 'pip', 'install', pkg])

try:
    from philh_myftp_biz import *
except:
    installPKG("git+https://github.com/MineFartS/Server-Package")
    from philh_myftp_biz import *
