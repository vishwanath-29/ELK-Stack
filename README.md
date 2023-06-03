
# ELK Stack

ELK Stack is one of the well known and popular framework used for many realtime use cases such as logging, log analysis and its visualization as well. It is an set of open source tools that work together to give the real time data analysis. 
It consists of three major components
- **E**lasticsearch
- **L**ogstash
- **K**ibana\

Logstash collects data from various sources, processes it,transforms it, processes it and send it to elasticsearch. Elasticsearch saves data in a document format and then kibana is used for visualization. This repo mainly focuses on bringing all together in a single component. Generally we are required to install them separately and do a lot of tasks, this reduces the hassle. Generally beats are used to stream data to logstash.Filebeat is also included in the compose as it is there to verify if everything is working.



## Deployment

To deploy this ELK stack, you require docker. The below provides a way to install docker in an apt package manager method, do check the official documentation of docker to install in your respective machines as well.

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
For changing the configurations of logstash,filebeat you can use the files provided as they are mounted to the container, changes made in the files will be reflected in the container, just make sure to down the compose and up it again after making changes.\
To run the ELK stack just run the following command 
```bash
docker-compose up
```
Wait for few mins, it will pull the 8.8.0 image version and build the stack, after sometime you can verify by going to localhost:5061 to see kibana UI\
To verify if everything is working fine, run the logging_script
```bash
python logging_script.py
```
This will write logs to local filesystem, filebeat will write it to logstash which will forward the same to elasticsearch. You can check official documentation of elasticsearch to query the data either through Kibana dev tools or through CLI
