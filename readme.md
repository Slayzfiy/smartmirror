### Features

- view your latest e-mails
- watch the time
- fetch a random quote
- select a stock and get today's change in percent from closing price.



# Smartmirror


[<img src="https://i.imgur.com/tLravU7.png[<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)">](http://google.com.au/)
## Installation
[Install from source](#from-source)

[Install with docker](#docker)

### From source
#### 1. Clone repository
`$ git clone https://github.com/Slayzfiy/smartmirror.git `
#### 2. Open repository directory
`$ cd smartmirror`
#### 3. Install requirements
`$ pip install -r requirements.txt`
#### Start app
`$ python app.py`

*IP will be printed in console. Webserver runs at port 1080
open e.g: 192.168.88.30:1080*

------------

### Docker 
#### 1. Clone repository
`$ git clone https://github.com/Slayzfiy/smartmirror.git `
#### 2. Open repository directory
`$ cd smartmirror`
#### 3. Build
`$ docker build -t smartmirror:latest . `
#### 4. Start container
`$ docker run -p 8000:5000  smartmirror:latest`
*if you close command promt, the container will be stopped*



