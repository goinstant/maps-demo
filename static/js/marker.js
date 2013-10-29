window.goinstant = window.goinstant || {};
window.goinstant.Marker = (function() {

/*jshint browser:true, node:false*/

"use strict";

/**
 * @fileOverview
 * Contains the Marker class, which handles setting and syncing markers on maps.
 */

/**
 * Dependencies
 */
var google = window.google;
var _ = window._;

/**
 * @constructor
 */
function Marker(map, room) {
  this._map = map;
  this._room = room;
  this._key = null;
  this._marker = null;

  _.bindAll(this, '_getState', '_setState');
}

/**
 * Initializes the synchronized marker
 * @public
 * @param {function} cb A callback function.
 */
Marker.prototype.initialize = function(cb) {
  this._marker = new google.maps.Marker({ map: this._map });

  var self = this;

  this._key = this._room.key('goinstant/demo/map/marker');
  this._key.get(function(err, value) {
    if (err) {
      return cb(err);
    }

    if (!value) {
      var pos = self._map.getCenter();
      self.setPosition(pos);

    } else {
      self._setState(value);
    }
    // Bind events
    google.maps.event.addListener(self._map, 'click', self._getState);

    self._key.on('set', self._setState);

    return cb();
  });
};

/**
 * Set Position
 * @public
 * @param {object} pos A google maps Position object.
 */
Marker.prototype.setPosition = function(pos) {
  this._marker.setPosition(pos);
  var state = {
    lat: pos.lat(),
    lng: pos.lng()
  };

  this._key.set(state);
};

/**
 * Gets the state of the local marker and stores that state in Platform.
 * @private
 * @param {object} event Map click event object.
 */
Marker.prototype._getState = function(event) {
  this._marker.setPosition(event.latLng);
  this._marker.setVisible(true);
  var state = {
    lat: event.latLng.lat(),
    lng: event.latLng.lng()
  };

  this._key.set(state);
};

/**
 * Sets the state of the local marker based on the state stored in Platform.
 * @private
 * @param {object} state The state of the marker
 */
Marker.prototype._setState = function(state) {
  if (!_.isObject(state)) {
    return;
  }

  var pos = new google.maps.LatLng(state.lat, state.lng);
  this._marker.setPosition(pos);
  this._marker.setVisible(true);
};

return Marker;

})();
