# How to pass env varaibale on pure python script

## Build & Run the simple script
```
docker build -t triangle .
docker images 
docker run -e TR_NUMBER=10 <bff2ba77dbd1>
```

## Before Run You can check on local environment
```
TR_NUMBER=8 python3 traingle.py
```

## Push into docker hub
```
docker images
docker tag <bff2ba77dbd1> username/triangle
docker login 
docker push linuxgeekup/traingle
```