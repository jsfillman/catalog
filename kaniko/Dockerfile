FROM gcr.io/kaniko-project/executor:latest AS kaniko
FROM python:latest
ENV DOCKER_CONFIG /kaniko/.docker
COPY --from=kaniko /kaniko /kaniko
RUN pip install pykaniko
COPY ./ /root/
CMD while true; do sleep 1000; done