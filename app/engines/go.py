import sys
import os
print 'hello from the engine!'
print str(sys.argv)
os.system('id')

print os.path.dirname(os.path.realpath(__file__))

folderPath = sys.argv[1]+'/'
files = os.listdir(folderPath)
fd = files[0]
path = folderPath+fd
os.system('unzip '+path+ ' -d '+folderPath)
os.system('mv /var/app/current/'+folderPath + ' '+ '/var/app/current/efs/'+folderPath)
print 'all done with the easy stuff.'
print 'About to start literally all of the analysis.'
os.chdir('/var/app/current/efs/ConSpeciFix/web/')
os.system('sh go.sh  &')
print 'we have started the devil.'