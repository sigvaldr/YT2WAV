import subprocess
import glob
import os
url=input("Please enter youtube URL: ")
cmd = 'yt-dlp -ci -f "bestaudio[ext=m4a]" '
cmd = cmd + url
subprocess.run(cmd)
m4aFile = glob.glob('*.m4a')
fileName = m4aFile[0][:-4].replace(" ", "_")
os.rename(m4aFile[0], "output.m4a")
m4aFile = glob.glob('*.m4a')
subprocess.run("ffmpeg -i " + m4aFile[0] + " -vn -acodec pcm_s16le -ar 44100 -ac 2 " + fileName + ".wav")
os.remove("output.m4a")
print("Done.")