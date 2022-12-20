# deploy stack of elk+grafana on docker #
How to started
 , clone from : https://github.com/eliyosef578/elk-grafana.git

### What is this repository? ###
* create Elastic stack (ELK) + grafana + portainer + python script that sends data to logstash and from there to elastic  on Docker



### Dependency ###
docker + docker-compose

stages: 

### How to install ###

* clone this project

* build the docker image for python script

	* $ cd python-app
  * $ docker build -t python-send-logs .



* deploy
	* $ docker-compose up -d

### how to connect ###

* kibana
  * localhost:5601
  * If the data was sent correctly, an index named "udp-logs-12000" will be created
  * create data views with the same index name "udp-logs-12000"

* grafana
  * localhost:3000
  * username: admin
  * password: admin

* portainer
  * localhost:9000

