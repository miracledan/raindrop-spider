# raindrop-spider
A simple distribute spider based on scrapy framework.

* [Reference](https://github.com/miracledan/raindrop-spider/blob/master/README.md#reference)
* [Install](https://github.com/miracledan/raindrop-spider/blob/master/README.md#install)
* [Fast start](https://github.com/miracledan/raindrop-spider/blob/master/README.md#fast-start)
* [Development](https://github.com/miracledan/raindrop-spider/blob/master/README.md#development)

## Reference
[scrapy](https://github.com/scrapy/scrapy)<br>
[scrapyd](https://github.com/scrapy/scrapyd)<br>
[scrapyd-client](https://github.com/scrapy/scrapyd-client)<br>
[mongodb](https://www.mongodb.org/)<br>

## Install
```
$ apt-get install curl libffi-dev libxml2-dev libxslt1-dev -y
$ apt-get install mongodb -y

$ cd raindrop-spider
$ virtualenv env
$ source env/local/bin/activate
$ pip install -r requirement.txt
```

## Fast start
### config scrapyd and then start a scrapyd server
```
$ cd raindrop-spider
$ mkdir /etc/scrapyd
$ cp etc/scrapyd.conf /etc/scrapyd
$ source env/local/bin/activate
$ scrapyd
```

### deploy scrapy spider
open a new ssh tab, excute commands to deploy scrapy spider on scrapyd server
```
$ cd raindrop-spider
$ source env/local/bin/activate
$ cd spider
$ scrapyd-deploy
```

### test spider
params: uid is the sns account id that you wanna spider
```
$ curl http://localhost:6800/schedule.json -d project=spider -d spider=gh_user -d uid=account-id 
```

### check the result
1.check log<br>
you would see the logs below if the spider task succeed
```
2015-10-22 15:44:44+0000 [-] Process started:  project='spider' spider='gh_user' 
job='cf1e9a2678d311e5bdd5080027880ca6' pid=4199 
log='logs/spider/gh_user/cf1e9a2678d311e5bdd5080027880ca6.log'

2015-10-22 15:44:47+0000 [-] Process finished:  project='spider' spider='gh_user' 
job='cf1e9a2678d311e5bdd5080027880ca6' pid=4199 
log='logs/spider/gh_user/cf1e9a2678d311e5bdd5080027880ca6.log' 
```

2.check mongodb<br>
you could check mongodb after seconds
```
$ mongo
> use raindrop
```

you can check the collections by command like this
```
> show collections
```

you can check data in collections by commad like this
```
> db.gh_user.find({})
```

## Development

### develop your own spider






