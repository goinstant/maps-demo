/*jshint node:true*/
"use strict";

exports = module.exports = function(app, config) {

  var platform = config.platform;
  var asset = platform.asset;
  var assetHost = asset.subdomain + '.' + platform.host;
  var assetUrl = assetHost + asset.path;
  var accountAppString = platform.account + '/' + platform.app;

  var jwtSimple = require('jwt-simple');
  var twilio = require('twilio');
  var util = require('util');
  var Validator = require('validator').Validator;
  var sanitize = require('validator').sanitize;

  var SendGrid = require('sendgrid');
  var sendGrid = new SendGrid(
    config.sendgrid.user,
    config.sendgrid.password,
    config.sendgrid.options
  );

  // Prevents throwing an exception
  Validator.prototype.error = function() {
    return false;
  };

  var validator = new Validator();

  var twilioClient = new twilio.RestClient(
    config.twilio.accountSid,
    config.twilio.auth_token
  );

  app.get('/', function(req, res) {
    var sessionId = req.session.sessionId || null;
    var user = req.session.user;

    return res.render('homepage', {
      sessionId: sessionId,
      user: user
    });
  });

  app.get('/thankyou', function(req, res) {
    return res.render('thankyou');
  });

  app.get('/map/:session', authenticationValid, function(req, res) {
    var token = req.session.user.token;
    var sessionId = req.session.sessionId = req.params.session;

    var data = {
      platformHost: assetHost,
      platformAsset: assetUrl,
      platformConnect: platform.host + '/' + accountAppString,
      platformToken: token,
      sessionId: sessionId
    };

    return res.render('map', data);
  });

  app.get('/hiw-demo/:session/:user', function(req, res) {
    var name = req.params.user;
    var session = req.params.session;

    var validId = validator.check(session).is(/^(?:hiw-)?\d{5}$/);
    if (!validId) {
      return error(res, "Invalid sessionId");
    }

    // These are the only 2 valid user params, only used for how it works demo.
    if (name !== "User 1" && name !== "User 2") {
      return error(res, "Invalid demo user");
    }

    var uid = randomNumber();
    var token = createJwt(name, uid);

    var data = {
      platformHost: assetHost,
      platformAsset: assetUrl,
      platformConnect: platform.host + '/' + accountAppString,
      platformToken: token,
      sessionId: session,
      index: uid
    };

    return res.render('hiw-demo', data);
  });

  app.post('/auth', function(req, res) {
    var uid = randomNumber();
    var displayName = sanitize(req.body.displayName).xss();
    var token = createJwt(displayName, uid);

    req.session.user = {
      name: displayName,
      uid: uid,
      token: token
    };

    if (!req.session.sessionId) {
      req.session.sessionId = randomNumber();
    }

    req.session.save(function() {
      res.redirect('/map/' + req.session.sessionId);
    });
  });

  app.post('/invite/sms', authenticationValid, function(req, res) {
    var sessionId = req.session.sessionId;

    var inviteUrl = req.protocol + '://' + req.host + '/map/' + sessionId;

    var number = req.body.number;
    var validNumber = validator.check(number).is(/^(?:\+\d)?\d{10}$/);
    if (!validNumber) {
      return error(res, "Invalid SMS number");
    }

    var username = sanitize(req.session.user.name).xss();

    var opts = {
      to: req.body.number,
      from: config.twilio.number,
      body: util.format(
          config.twilio.invite_body,
          username,
          inviteUrl
        )
    };
    twilioClient.sms.messages.create(opts, function(err) {
      if (err) {
        res.statusCode = 500;
        return res.send(err.message);
      }
      res.send('OK');
    });
  });

  app.post('/invite/email', authenticationValid, function(req, res) {
    var sessionId = req.session.sessionId;

    var inviteUrl = req.protocol + '://' + req.host + '/map/' + sessionId;

    var email = req.body.email;
    var validLen = validator.check(email).len(6, 64);
    var validEmail = validator.check(email).isEmail();
    if (!validLen || !validEmail) {
      return error(res, "Invalid email");
    }

    var username = sanitize(req.session.user.name).xss();

    sendGrid.send({
      to: email,
      from: 'noreply@goinstant.com',
      subject: 'GoInstant Maps Demo Invitation',
      html: util.format(
        config.sendgrid.invite_body,
        username,
        username,
        inviteUrl,
        username,
        username)
    }, function(success, message) {

      /* TODO: This is a little gross but success returns null on success, will submit a PR to fix */
      if (message.message !== 'success') {
        res.statusCode = 500;
        return res.send(message);
      }
      res.send(message);
    });
  });

  function error(res, msg) {
    res.statusCode = 400;
    res.send('Error: ' + msg);
  }

  function createJwt(name, uid) {
    var secret = new Buffer(config.platform.secret, 'base64');
    var claims = {
      iss: 'demos.goinstant.org',
      sub: ''+ uid, //TODO: When #629 is done this doesn't need to be a string.
      dn: name
    };

    return jwtSimple.encode(claims, secret);
  }

  function authenticationValid(req, res, next) {

    // validate the session param
    if (req.params.session) {
      var validId = validator.check(req.params.session).is(/^\d{5}$/);
      if (!validId) {
        return error(res, "Invalid sessionId");
      }
    }

    if (req.session.user && req.session.user.token) {
      return next();

    } else {
      req.session.sessionId = req.params.session;
      res.redirect('/');
    }
  }

  function randomNumber() {
    return Math.floor(Math.random() * 90000) + 10000;
  }
};
