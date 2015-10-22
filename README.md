# raindrop-spider
A spider base on scrapy framework.

## install
```
$ apt-get install curl libffi-dev libxml2-dev libxslt1-dev -y
$ apt-get install mongodb -y

$ cd raindrop-spider
$ virtualenv env
$ source env/local/bin/activate
$ pip install -r requirement.txt
```

## Fast start
config scrapyd and then start a scrapyd server
```
$ cd raindrop-spider
$ mkdir /etc/scrapyd
$ cp etc/scrapyd.conf /etc/scrapyd
$ source env/local/bin/activate
$ scrapyd
```

deploy scrapy spider
open a new ssh tab, excute commands to deploy scrapy spider on scrapyd server
```
$ cd raindrop-spider
$ source env/local/bin/activate
$ cd spider
$ scrapyd-deploy
```

test spider
params: uid is the account id that you wanna spider
```
$ curl http://localhost:6800/schedule.json -d project=spider -d spider=gh_user -d uid=your-sns-account-id 
```

check the result
1.check log, if the spider task succeed, you could see the logs below
```
2015-10-22 15:44:44+0000 [-] Process started:  project='spider' spider='gh_user' job='cf1e9a2678d311e5bdd5080027880ca6' pid=4199 log='logs/spider/gh_user/cf1e9a2678d311e5bdd5080027880ca6.log'

2015-10-22 15:44:47+0000 [-] Process finished:  project='spider' spider='gh_user' job='cf1e9a2678d311e5bdd5080027880ca6' pid=4199 log='logs/spider/gh_user/cf1e9a2678d311e5bdd5080027880ca6.log' 
```

2.check mongodb
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

you can change the data store by edit `pipelines.py`




