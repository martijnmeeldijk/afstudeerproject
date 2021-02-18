FROM python:3.7-slim
#FROM jjanzic/docker-python3-opencv
COPY . /SocialDistancingAi
WORKDIR /SocialDistancingAi
CMD chmod +x ./main.py
RUN pip install opencv-python scipy numpy
RUN pip install -r requirements.txt
CMD python3.7 ./main.py
