window.goinstant = window.goinstant || {};
window.goinstant.AutoComplete = (function() {

/*jshint browser:true, node:false*/

"use strict";

/**
 * @fileoverview
 * Contains the AutoComplete class, which handles creating and setting the state
 * of a list of places populated by the Google map.
 */

/**
 * Dependencies
 */
var $ = window.$;
var google = window.google;
var _ = window._;

/**
 * @constructor
 */
function AutoComplete(map, marker) {
  this._map = map;
  this._marker = marker;

  this._selecting = false;
  this._autoComplete = null;
  this._geo = null;

  _.bindAll(this, '_placeChanged', '_search');
}

/**
 * Initialize
 * @public
 */
AutoComplete.prototype.initialize = function() {
  var $input = $('#search-bar');

  this._autoComplete = new google.maps.places.Autocomplete($input[0]);
  this._autoComplete.bindTo('bounds', this._map);

  this._geo = new google.maps.Geocoder();

  google.maps.event.addListener(this._autoComplete, 'place_changed',
                                this._placeChanged);

  $('#search-button').on('click', this._search);

  var self = this;

  $('#search-bar').on('keyup', function(event) {
    if (event.keyCode === 40 || event.keyCode === 38 ) {
      self._selecting = true;
    }

    if (event.keyCode === 13 && !self._selecting)  {
      self._search();
    }
  });
};

/**
 * Place Changed
 * @private
 */
AutoComplete.prototype._placeChanged = function() {
  var place = this._autoComplete.getPlace();

  this._selecting = false;

  // Didn't find a place with auto complete.
  if (!place.geometry) {
    return;
  }

  if (place.geometry.viewport) {
    this._map.fitBounds(place.geometry.viewport);

  } else {
    this._map.setCenter(place.geometry.location);
  }

  this._marker.setPosition(place.geometry.location);
};

/**
 * Search
 * @private
 */
AutoComplete.prototype._search = function() {
  var self = this;

  var $container = $('.pac-container').children();
  var firstResult = $container.first().text();

  this._geo.geocode({ 'address': firstResult }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var lat = results[0].geometry.location.lat();
      var lng = results[0].geometry.location.lng();

      var pos = new google.maps.LatLng(lat, lng);

      self._map.setCenter(pos);

      if (self._marker) {
        self._marker.setPosition(pos);
      }
    } else {
      return;
    }
  });
};

return AutoComplete;

})();
