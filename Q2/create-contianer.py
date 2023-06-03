import subprocess


subprocess.call(['unshare', '-n', '-u', '-i', '-p', '-f', '-m', '-U'])