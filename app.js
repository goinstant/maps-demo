/*jshint node:true*/
"use strict";

var http = require('http');
var express = require('express');
var ejsLocals = require('ejs-locals');
var RedisStore = require('connect-redis')(express);

var localUtil = require('./lib/util');
var overrideConfig = localUtil.overrideConfig;

/* Load Base config and fall back on process.env for any unset values */
var baseConfig = require('json-config')();
var config = overrideConfig(baseConfig);

/* Init express */
var app = express();

app.configure(function() {
  app.set('env', process.env.NODE_ENV || 'local');
  app.set('port', process.env.PORT || config.server.listen);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'ejs');

  app.engine('ejs', ejsLocals);
  app.locals({
    _layoutFile: 'layout',
    title: 'GoInstant Maps Demo',
    typekitUrl: config.typekit_url
  });

  app.use(express.logger('dev'));
  app.use(express.cookieParser());
  app.use(express.bodyParser());
  app.use(express.session({
    secret: config.expressSecret,
    store: new RedisStore(config.redis)
  }));
  app.use(express.methodOverride());
  app.use('/static', express.static(__dirname + '/static'));

});


/* Ensure SSL Enabled on heroku */
app.all('*', function (req, res, next) {
  if (!process.env.FORCE_SSL) {
    /* do not force */
    return next();

  }

  if (req.get('x-forwarded-proto') != "https") {
    res.set('x-forwarded-proto', 'https');
    return res.redirect('https://' + req.get('host') + req.url);

  }

  return next();

});

/* Include all routes */
require('./lib/routes')(app, config);

http.createServer(app).listen(app.get('port'), function() {
  console.log('App is listening on port ' + app.get('port'));
});
