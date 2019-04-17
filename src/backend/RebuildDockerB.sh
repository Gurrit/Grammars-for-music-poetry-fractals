#!/bin/bash
imageName=xx:backend
containerName=backend-container

docker build -t $imageName -f Dockerfile  .

echo Delete old container...
docker rm -f $containerName

echo Run new container...
docker run -d -p 88:88 --name $containerName $imageName

#http://192.168.99.100/
#run chmod +x rebuildDocker.sh then ./rebuildDocker.sh make sure nothing else is running on port 80. When you want to update images/container (to see changes in frontend)