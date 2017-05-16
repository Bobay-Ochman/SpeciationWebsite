 #!/bin/bash 
timestamp=$(date +%s)
rm uploads/*
zip -r app.zip ./* .ebextensions > /dev/null
mv app.zip ../dist/$timestamp.zip 
echo $timestamp
echo -en "\007"