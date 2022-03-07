### Features

- view your latest e-mails
- watch the time
- fetch a random quote
- select a stock and get today's change in percent from closing price.



# Smartmirror



## Installation
### From source
#### Clone repository
`$ git clone https://github.com/Slayzfiy/smartmirror.git `
#### Open repository
`$ cd smartmirror`
#### Install requirements
`$ pip install -r requirements.txt`
#### Start app
`$ python app.py`

*IP will be printed in console. Webserver runs at port 1080
open e.g: 192.168.88.30:1080*

------------

### Docker 
#### Clone repository
`$ git clone https://github.com/Slayzfiy/smartmirror.git `
#### Open repository
`$ cd smartmirror`
#### Build
`$ docker build -t smartmirror:latest . `
#### Start container
`$ docker run -p 8000:5000  smartmirror:latest`
*if you close command promt, the container will be stopped*



