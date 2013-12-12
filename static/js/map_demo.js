window.goinstant = window.goinstant || {};
window.goinstant.MapDemo = (function(){

/*jshint browser:true, node:false */

"use strict";

/**
 * @fileoverview
 * Contains the MapDemo class, which connects to platform, initializes
 * components, loads the synchronized Google map and initializes map addons.
 */

/**
 * Dependencies
 */
var goinstant = window.goinstant;
var AutoComplete = goinstant.AutoComplete;
var SendInvite = goinstant.SendInvite;
var Marker = goinstant.Marker;
var MultiplayerMap = goinstant.MultiplayerMap;
var async = window.async;
var _ = window._;
var UserColors = window.goinstant.widgets.UserColors;
var UserList = window.goinstant.widgets.UserList;
var Form = window.goinstant.widgets.Form;
var Chat = window.goinstant.widgets.Chat;

/**
 * @constructor
 */
function MapDemo(config) {
  this._room = null;
  this._multiplayerMap = null;

  this._sessionId = config.sessionId;
  this._connectUrl = config.connectUrl;
  this._token = config.token;
  this._index = config.index;

  this._mapOptions = {
    container: config.container,
    scrollEnabled: config.scrollEnabled,
    streetEnabled: config.streetEnabled,
    throttle: config.throttle || 0,
    chatEnabled: config.chatEnabled
  };
}

/**
 * Initialize
 * @public
 */
MapDemo.prototype.initialize = function(cb) {

  var tasks = [
    _.bind(this._platformConnect, this),
    _.bind(this._initializeComponents, this),
    _.bind(this._initializeMap, this)
  ];

  async.series(tasks, cb);
};

/**
 * Platform Connect
 * @private
 * @param {function} cb A callback function.
 */
MapDemo.prototype._platformConnect = function(cb) {
  var self = this;

  var options = null;

  if (this._index) {
    options = {
      sessionId: '',
      guestId: this._index
    };
  }

  var connection = new goinstant.Connection(this._connectUrl, options);

  connection.connect(this._token, function(err) {
    if (err) {
      return cb(err);
    }

    self._room = connection.room(self._sessionId);

    self._room.join(function(err) {
      if (err) {
        return cb(err);
      }

      return cb();
    });
  });
};

/**
 * Initialize Components
 * @private
 * @param {function} cb A callback function.
 */
MapDemo.prototype._initializeComponents = function(cb) {
  var self = this;

  var userColors = new UserColors({ room: self._room });
  userColors.choose(function(err) {
    if (err) {
      return cb(err);
    }

    var userList = new UserList({ room: self._room });

    var formOptions = {
      key: self._room.key('goinstant/demo/map/form'),
      el: document.getElementById('search-form'),
      room: self._room
    };

    var form = new Form(formOptions);

    var tasks = [
      _.bind(userList.initialize, userList),
      _.bind(form.initialize, form)
    ];

    if (self._mapOptions.chatEnabled) {
      var chat = new Chat({ room: self._room, position: 'left' });
      tasks.push(_.bind(chat.initialize, chat));
    }

    async.parallel(tasks, cb);
  });
};

/**
 * Initialize Map
 * @private
 */
MapDemo.prototype._initializeMap = function(cb) {
  var self = this;

  this._mapOptions.room = this._room;

  this._multiplayerMap = new MultiplayerMap(this._mapOptions);
  this._multiplayerMap.initialize(function(err, map) {
    if (err) {
      return cb(err);
    }

    // Setup marker addon
    var marker = new Marker(map, self._room);
    marker.initialize(function(err) {
      if (err) {
        return cb(err);
      }

      // Setup auto-complete addon
      var autoComplete = new AutoComplete(map, marker);
      autoComplete.initialize();
    });

    // Setup invite addon
    if (!self._index) {
      var sendInvite = new SendInvite();
      sendInvite.initialize();
    }

    return cb();
  });
};

return MapDemo;

})();
