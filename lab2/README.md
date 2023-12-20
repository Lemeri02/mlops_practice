```commandline
https://www.jenkins.io/doc/book/installing/docker/
```

```commandline
docker network create jenkins
```

```commandline
docker build -t myjenkins-blueocean:2.426.2-1 .
```

```commandline
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.426.2-1
```


```commandline
0.0.0.0:8080 или localhost:8080
```

```commandline
sudo docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```

В Jenkins установить Python 1.3  в управлении плагинами