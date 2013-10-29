"use strict";

var _ = require('lodash');
var url = require('url');

var util = exports;

/*
 * This util is required to allow for local development
 * and environ override for heroku deployments
 */

util.overrideConfig = function (config) {

  /* SET FORCE SSL; DEFAULT '' */
  config.force_ssl = process.env.FORCE_SSL;

  /* REDIS URL OVERRIDE: LOCAL redis */
  config.redisurl = process.env.REDISCLOUD_URL || config.redisurl;

  /* PRE PARSE REDIS URL */
  var redis = url.parse(config.redisurl);
  config.redis = {
    host: redis.hostname,
    port: redis.port
  };

  /* PULL OUT PASSWORD IF PRESENT */
  if (redis.auth) {
    var redisAuth = redis.auth.split(":");
    config.redis.pass = redisAuth[1];
  }

  /* EXPRESS SECRET OVERIDES */
  config.expressSecret = process.env.EXPRESS_SECRET || config.expressSecret;

  /* SENDGRID OVERRIDES */
  if (!config.sendgrid) {
    config.sendgrid = {};
  }

  config.sendgrid = _.defaults(config.sendgrid, {
    user: process.env.SENDGRID_USER,
    password: process.env.SENDGRID_PASSWORD
  });


  /* TWILIO OVERRIDES */
  if (config.twilio) {
    config.twilio = _.defaults(config.twilio, {
      auth_token: process.env.TWILIO_AUTH_TOKEN,
      accountSid: process.env.TWILIO_ACCOUNT_SID,
      number: process.env.TWILIO_NUMBER
    });

  }


  /* PLATFORM OVERRIDES */
  if (config.platform) {

    /* Host Env Override */
    config.platform.host = process.env.PLATFORM_HOST || config.platform.host;

    config.platform = _.defaults(config.platform, {
      account: process.env.PLATFORM_ACCOUNT,
      app: process.env.PLATFORM_APP,
      secret: process.env.PLATFORM_SECRET
    });

  }


  /* GOOGLE ANALYTICS OVERRIDES */
  if (!config.ga) {
    config.ga = {};
  }

  config.ga = _.defaults(config.ga, {
    account: process.env.GA_ACCOUNT,
    domain: process.env.GA_DOMAIN
  });


  /* TYPEKIT OVERRIDES */
  config.typekit_url = process.env.TYPEKIT_URL || config.typekit_url;

  return config;
};
