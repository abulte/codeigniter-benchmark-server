# Codeigniter example app

Based on :
	
* [Codeigniter bootstrap by @vesparny](https://github.com/vesparny/codeigniter-html5boilerplate-twitter-bootstrap)
* [Codeigniter quick start tutorial](http://codeigniter.com/user_guide/tutorial/)
	
I use it to make simple Php/MySQL benchmarks on servers.

See the funkload benchmark "client" script at <https://github.com/abulte/codeigniter-benchmark-client>

Pages :

* `/` - standard home page with bootstrap stuff
* `/news` - list of news objects
* `/news/create` - form to create a news
* `/news/<slug>` - view a news

Set MySQL login & password in `application/config/database.php`.
    
    