# README FILE :
# Steps to create docker image using the dockerfile
- create a folder with the dockerfile in it 
- copy the contents of the forked `EveryDream2trainer` and set up the repo by following the instructions mentioned in the original repo. 
- run the `docker build -f dock3 -t proj:myapp .`
- a docker image should be created please increase default disk size of the image as the image is quite large.
# Steps to create the docker image manually .
- Start a docker container and follow the steps below.

FILES THAT HAVE BEEN CREATED :

1. v1-inference.yaml : I installed this file from the web which was available for this repository. 

2. requirments.txt : I created the requirements.txt file after checking if the repo was running on my local system. 

3. server.py : It is the python file which is responsible for creating the Flask API and calling the train.py file. 


STEPS THAT I FOLLOWED FOR TO CREATE THE DOCKER IMAGE :

1. I created the docker container which was using python:3.9.12 : 

docker run -p 5000:5000 --network=host -i -t python:3.9.12-slim-bullseye bash


2. I copied the repository from my local system to the docker container :

docker cp /Users/harsh/Documents/StableDiffusion/EveryDream2trainer goofy_gates:/EveryDream2trainer

3. Navigated to the repo folder :

cd EveryDream2trainer

4. Installed all the dependencies that are needed using the requirements.txt file.

pip install -r requirements.txt

5. Ran the server.py which creates the Flask API.

CMD ["python", "server.py"]



STEPS THAT I FOLLOWED TO PUSH THE DOCKER IMAGE :

1. docker commit f2b2ebf05611faf9edf232ffdf84a9ffa94852e4a537e6b90a8dcf01c285839f everydream2trainerdocker:v0.1

2. docker tag everydream2trainerdocker:v0.1 harshvardhan96/everydream2trainerdocker:v0.1

3. docker push harshvardhan96/everydream2trainerdocker:v0.1



