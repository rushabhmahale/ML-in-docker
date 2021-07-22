Check out my video:- (https://drive.google.com/file/d/1Xj8mNwdsvugrJAd16BcZ-FvN5xdY1t8R/view?usp=sharing)

# Ml in Docker 
I Have created an salary ML model and that ML model is run in the Docker container 

## [Model.py](https://github.com/rushabhmahale/ML-in-docker/blob/main/model.py)
This is file contain of python code i have use and ihave installed library pandas scikit-learn to predict the model 


## [Salary_Data.csv](https://github.com/rushabhmahale/ML-in-docker/blob/main/Salary_Data.csv)
This is csv file where are going to use to predict this value regarding there experience and in ml we always use csv file 

## Requirements

- docker
- Dataset
- python IDE
- Python library 

## Set up

1. first install docker in your system using cmnd yum install docker-ce --nobest -y ⚠️ create repo of docker ⚠️ Than install docker 

2. now start the docker service using cmnd systemctl start docker if you are using linux if you are using windows use this cmnd Start->Run-> services.msc 

3. check image what you have using docker images cmnd if you dont have any image use docker pull *any image you want* for example docker pull centos:7 and always use -tag

4. than i have created container using “docker run -it __name CONTAINERNAME centos:latest” 
 Inside Docker :-
- rpm -q python3
- yum install python3 -y
- pip3 install pandas
- pip3 install numpy
- pip3 install scikit-learn
- exit

5. “docker cp <src> <container_name>:<dest>” 

6. docker start CONTAINERNAME

7. docker attach CONTAINERNAME
- mkdir mlmodel
- cd mlmodel
- python3 model.py 
  
