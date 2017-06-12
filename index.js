var util = require('util'),
    fs = require('fs'),
    path = require('path'),
    request = require('request'),
    querystring = require("querystring"),
    _ = require('lodash'),
    moment = require('moment');
var cheerio = require('cheerio');
var config = require('./config.json');

module.exports = function(app, admin, passport, io, torrents){
  var isLoggedIn = function(req){
		return req.user !== undefined;
	};
  app.get('/', function(req, res){
    res.render('index', {
      user: req.user,
      logged: isLoggedIn(req)
    });
	});
  app.get('/template/:name', function(req, res){
    res.render(req.params.name);
  });
  app.post('/token', passport.authenticate('google', { failureRedirect: '/' }), function(req, res){
    admin.database().ref('/users').child(req.user.data.uid).update({
      last_connection: +moment()
    });
    res.send(true);
	});
  app.get('/users', function(req, res){
    console.log(_.map(users_connected, function(user) {
      return _.omit(user, 'client');
    }));
    res.send(_.map(users_connected, function(user) {
      return _.omit(user, 'client');
    }));
  });
  app.get('/search/place/:address', function(req, res){
    var url = 
'https://maps.googleapis.com/maps/api/geocode/json?address='+encodeURI(req.params.address)+'&key='+config.llave;
    request(url, function (err, data, body) {
      if (err){ throw err; }
      res.send(body);
    });
  });
  app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
  });
  //Handle 404
  app.use(function(err, req, res, next){
  });
  var users_connected = {};
};
String.prototype.capitalizeFirstLetter = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};
