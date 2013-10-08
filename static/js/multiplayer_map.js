window.goinstant = window.goinstant || {};
window.goinstant.MultiplayerMap = (function() {

/*jshint browser:true, node:false */

'use strict';

/**
 * @fileoverview
 * Contains the MultiplayerMap class, which handles the creation and
 * synchronization of a Google map.
 */

/**
 * Dependencies
 */
var google = window.google;
var async = window.async;
var _ = window._;
var $ = window.$;

var DEMO_NAMESPACE = '/goinstant/demos/map';
var MAP_STATE = DEMO_NAMESPACE + '/map_state';
var STREET_STATE = DEMO_NAMESPACE + '/street_state';

function MultiplayerMap(options) {
  this._room = options.room;
  this._container = options.container;
  this._scrollEnabled = options.scrollEnabled;
  this._streetEnabled = options.streetEnabled;
  this._throttle = options.throttle;
  this._propagate = true;

  this._map = null;
  this._street = null;

  this._$searchBar = $('#search-bar');
  this._$searchButton = $('#search-button');
  this._$streetViewButton = $('#close-street-view');
  this._$inviteButton = $('#invite-button');
  this._$buttonContainer = $('#button-container');

  // Setup the map options
  this._mapOptions = {
    zoom: 9,
    center: new google.maps.LatLng(37.774929, -122.419416),
    mapTypeId: google.maps.MapTypeId.SATELLITE,
    panControl: false,
    tilt: 45,
    scrollwheel: this._scrollEnabled,
    streetViewControl: this._streetEnabled
  };


  this._throttledKeySet = _.throttle(this._keySet, this._throttle);

  _.bindAll(
    this,
    '_setMapState',
    '_setStreetState'
  );
}

/**
 * Initialize
 * @public
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype.initialize = function(cb) {
  google.maps.visualRefresh = true;

  // Setup map
  this._map = new google.maps.Map(this._container, this._mapOptions);

  var tasks = [
    _.bind(this._setupMap, this)
  ];

  if (this._streetEnabled) {
    tasks.push(_.bind(this._setupStreet, this));
  }

  var self = this;

  async.parallel(tasks, function(err) {
    if (err) {
      return cb(err);
    }

    return cb(null, self._map);
  });
};

/**
 * Setup Map
 * @private
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._setupMap = function(cb) {
  this._mapKey = this._room.key(MAP_STATE);

  // Create map state children keys
  this._mapKey.key('center');
  this._mapKey.key('zoom');
  this._mapKey.key('type');

  var mapKeyOptions = {
    listener: this._setMapState,
    bubble: true
  };

  this._mapKey.on('set', mapKeyOptions);

  this._bindMapListeners();
  this._initializeMapState(cb);
};

/**
 * Setup Street
 * @private
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._setupStreet = function(cb) {
  this._street = this._map.getStreetView();
  this._streetKey = this._room.key(STREET_STATE);

  // Create street state children keys
  this._streetKey.key('position');
  this._streetKey.key('visible');
  this._streetKey.key('zoom');
  this._streetKey.key('pov');

  var streetKeyOptions = {
    listener: this._setStreetState,
    bubble: true
  };

  this._streetKey.on('set', streetKeyOptions);

  this._street.setVisible(false);
  this._street.setZoom(1);
  this._street.setPov({
    'heading': 0,
    'pitch': 0,
    'zoom': 1
  });

  var self = this;

  // Close street view when button pressed
  this._$streetViewButton.on('click', function() {
    self._street.setVisible(false);
  });

  this._bindStreetListeners();
  this._initializeStreetState(cb);
};

/**
 * Set Map State
 * @private
 * @param {object} value The map's state stored in an object.
 * @param {object} context A GoInstant key context object.
 */
MultiplayerMap.prototype._setMapState = function(state, context) {
  this._propagate = false;

  if (context.key === MAP_STATE + '/center') {
    var currentPos = this._map.getCenter();
    if (currentPos.lat() !== state.lat || currentPos.lng() !== state.lng) {
      var newPos = new google.maps.LatLng(state.lat, state.lng);
      this._map.panTo(newPos);
    }

  } else if (context.key === MAP_STATE + '/zoom') {
    this._map.setZoom(state);

  } else if (context.key === MAP_STATE + '/type') {
    this._map.setMapTypeId(state);

  }

  this._propagate = true;
};

/**
 * Set Street State
 * @private
 * @param {object} value The street's state stored in an object.
 * @param {object} context A GoInstant key context object.
 */
MultiplayerMap.prototype._setStreetState = function(state, context) {
  this._propagate = false;

  if (context.key === STREET_STATE + '/position') {
    var currentPos = this._street.getPosition();

    if (!currentPos || currentPos.lat() !== state.lat ||
        currentPos.lng() !== state.lng) {

      var newPos = new google.maps.LatLng(state.lat, state.lng);
      this._street.setPosition(newPos);
    }

  } else if (context.key === STREET_STATE + '/visible') {
    this._streetUI(state);
    this._street.setVisible(state);

  } else if (context.key === STREET_STATE + '/zoom') {
    this._street.setZoom(state);

  } else if (context.key === STREET_STATE + '/pov') {
    this._street.setPov(state);
  }

  this._propagate = true;
};

/**
 * Initialize Map State
 * @private
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._initializeMapState = function(cb) {
  var tasks = [
    _.bind(this._getMapState, this, 'center'),
    _.bind(this._getMapState, this, 'zoom'),
    _.bind(this._getMapState, this, 'type')
  ];

  async.parallel(tasks, cb);
};

/**
 * Initialize Street State
 * @private
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._initializeStreetState = function(cb) {
  var tasks = [
    _.bind(this._getStreetState, this, 'position'),
    _.bind(this._getStreetState, this, 'visible'),
    _.bind(this._getStreetState, this, 'zoom'),
    _.bind(this._getStreetState, this, 'pov')
  ];

  async.parallel(tasks, cb);
};

/**
 * Get Map State
 * @private
 * @param {string} property The property to get the state of (ex: center).
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._getMapState = function(property, cb) {
  var self = this;

  this._mapKey.key(property).get(function(err, state) {
    if (err) {
      return cb(err);
    }

    if (!state) {
      return cb();
    }

    self._setMapState(state, {key: MAP_STATE + '/' + property });
    return cb();
  });
};

/**
 * Get Street State
 * @private
 * @param {string} property The property to get the state of (ex: zoom).
 * @param {function} cb A callback function.
 */
MultiplayerMap.prototype._getStreetState = function(property, cb) {
  var self = this;

  this._streetKey.key(property).get(function(err, state) {
    if (err) {
      return cb(err);
    }

    if (!state) {
      return cb();
    }

    self._setStreetState(state, {key: STREET_STATE + '/' + property });
    return cb();
  });
};

/**
 * Sets a key to the passed value
 * @private
 * @param {object} key A goinstant key reference.
 * @param {object} value The value to set the key to.
 */
MultiplayerMap.prototype._keySet = function(key, value) {
  key.set(value);
};

/**
 * Bind Map Listeners
 * @private
 */
MultiplayerMap.prototype._bindMapListeners = function() {
  var self = this;

  google.maps.event.addListener(this._map, 'center_changed', function() {
    if (!self._propagate) {
      return;
    }

    var mapCenter = self._map.getCenter();
    var center = {
      'lat': mapCenter.lat(),
      'lng': mapCenter.lng()
    };

    self._throttledKeySet(self._mapKey.key('center'), center);
  });

  google.maps.event.addListener(this._map, 'zoom_changed', function() {
    if (!self._propagate) {
      return;
    }

    var zoom = self._map.getZoom();

    self._throttledKeySet(self._mapKey.key('zoom'), zoom);
  });

  google.maps.event.addListener(this._map, 'maptypeid_changed', function() {
    if (!self._propagate) {
      return;
    }

    var type = self._map.getMapTypeId();

    self._throttledKeySet(self._mapKey.key('type'), type);
  });
};

/**
 * Bind Street Listeners
 * @private
 */
MultiplayerMap.prototype._bindStreetListeners = function() {
  var self = this;

  google.maps.event.addListener(this._street, 'visible_changed', function() {
    if (!self._propagate)  {
      return;
    }

    var visible = self._street.getVisible();
    self._streetUI(visible);

    self._keySet(self._streetKey.key('visible'), visible);
  });

  google.maps.event.addListener(this._street, 'position_changed', function() {
    if (!self._propagate)  {
      return;
    }

    var streetPosition = self._street.getPosition();
    var position = {
      lat: streetPosition.lat(),
      lng: streetPosition.lng()
    };

    self._throttledKeySet(self._streetKey.key('position'), position);
  });

  google.maps.event.addListener(this._street, 'zoom_changed', function() {
    if (!self._propagate)  {
      return;
    }

    var zoom = self._street.getZoom();

    self._throttledKeySet(self._streetKey.key('zoom'), zoom);
  });

  google.maps.event.addListener(this._street, 'pov_changed', function() {
    if (!self._propagate)  {
      return;
    }

    var pov = self._street.getPov();

    self._throttledKeySet(self._streetKey.key('pov'), pov);
  });
};

/**
 * Street UI
 * @private
 * @param {boolean} visible True if street view is visible, false if not.
 */
MultiplayerMap.prototype._streetUI = function(visible) {
  if (visible) {
    this._$streetViewButton.css('display', 'inline-block');
    this._$searchBar.css('display', 'none');
    this._$searchButton.css('display', 'none');
    this._$inviteButton.css({
      'right': '6px',
      'top': this._$streetViewButton.height() + 26,
      'position': 'fixed'
    });

    this._$buttonContainer.css('right', '');

  } else {
    this._$streetViewButton.css('display', 'none');
    this._$searchBar.css('display', 'inline-block');
    this._$searchButton.css('display', 'inline-block');
    this._$inviteButton.css({
      'right': 'auto',
      'top': 'auto',
      'position': 'relative'
    });

    this._$buttonContainer.css('right', '112px');
  }
};

return MultiplayerMap;

})();
