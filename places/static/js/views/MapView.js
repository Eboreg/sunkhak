/**
 * Vyn har direkt kännedom om modellen då det ej finns anledning att ha någon Collection (vi använder bara en karta).
 * Förändringar i geolocation räknas som en användarinteraktion och tas omhand här.
 * 
 * Properties
 * el : kartelementet
 * model : sunkhak.Map (används ännu bara för att ange defaultvärden; kan ej hämta eller lagra några data någonstans)
 * map : 
 * mapEvents : lyssnar efter events på 'map'
 * 
 * Events:
 * 	Backbone.'mapview:map:idle' : UserPlaceView ritar ut användarmarkör (om position finns)
 */
define([
	'backbone',
	'underscore',
	'leaflet',
	'leaflet-markercluster',
	'settings',
	'models/Map',
	'leaflet-usermarker',
], function(Backbone, _, L, markercluster, settings, Map) {
	var MapView = Backbone.View.extend({
		el : '#map-element',
		model : new Map(),
		// Vi kan inte använda events-hashen eftersom den behandlas före initialize(), varför ej map:* kommer att funka
		mapEvents : {
			'load' : 'onMapReady',
			'click' : 'onMapClick',
			'zoomend' : 'onMapZoomEnd',
			'moveend' : 'onMapMoveEnd',
			'locationfound' : 'onMapLocationFound',
		},
	
		initialize : function(options) {
			this.markercluster = L.markerClusterGroup({
				maxClusterRadius : settings.maxClusterRadius,
			});
			this.map = L.map(this.el, {
				maxZoom : settings.maxZoom,
				zoomControl : false,
				attributionControl : false,
			});
			this.listenTo(this.model, 'change:userLocation', this.onUserLocationChange);
			this.bindMapEvents();
		},
		render : function() {
			if (!this.model.get('rendered')) {
				L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(this.map);
				L.control.attribution({
					position : 'bottomleft',
				}).addAttribution('Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>')
					.addTo(this.map);
				// Triggar map:load som kör this.onMapReady():
				this.map.setView(this.model.get('location'), this.model.get('zoom'));
			}
			return this;
		},
		reloadMapSize : function() {
			this.map.invalidateSize({ pan : false });
		},
		// fullZoom = bool
		panTo : function(latlng, fullZoom) {
			fullZoom = fullZoom || false;
			if (!fullZoom)
				this.map.flyTo(latlng);
			else
				this.map.flyTo(latlng, 17);
		},
		panToIfOutOfBounds : function(latlng) {
			var bounds = this.map.getBounds();
			if (!bounds.contains(latlng)) {
				this.map.flyTo(latlng);
			}
		},
		zoomInFull : function() {
			this.map.setZoom(settings.maxZoom);
		},
		// Triggas av ikonklick i MenuBarView
		gotoUserLocation : function() {
			if (null === this.model.get('userLocation')) {
				this.map.locate({
					watch : true,
					locate : true,
					setView : false,
					maxZoom : 15,
					enableHighAccuracy : true,
				});
			} else {
				this.map.flyTo(this.model.get('userLocation').latlng, 17);
			}
		},

		// KART-EVENTS
		// Triggas av load-event från map 
		// Körs alltså alltid efter this.render()
		onMapReady : function() {
			this.model.set('rendered', true);
			this.trigger('rendered');
			this.map.addLayer(this.markercluster);
		},
		onMapMoveEnd : function() {
			this.model.set('location', this.map.getCenter());
		},
		onMapZoomEnd : function() {
			this.model.set('zoom', this.map.getZoom());
		},
		onMapLocationFound : function(location) {
			this.model.set('userLocation', location);
			this.trigger('map-location-found', location);
		},

		// DOM-EVENTS
		// Klickat någonstans på kartan men ej på en marker
		onMapClick : function() {
			this.trigger('map-click');
		},

		// MODELL-EVENTS
		onUserLocationChange : function(model, value) {
			if (!this.userMarker) {
				this.userMarker = L.userMarker(value.latlng, {
					smallIcon : true,
				}).addTo(this.map);
				this.map.flyTo(value.latlng, 17);
			}
			this.userMarker.setLatLng(value.latlng);
			this.userMarker.setAccuracy(value.accuracy);
		},

		/**
		 * Delegerar alla Leaflet-events till View-events med namn 'map:<leaflet-eventnamn>'.
		 * Binder även explicit angivna lyssnare till Leaflet-events via this.mapEvents.
		 */
		bindMapEvents : function() {
			var mapEventNames = [
				'click', 'dblclick', 'mousedown', 'mouseup', 'mouseover', 'mouseout', 'mousemove', 'contextmenu', 'focus', 
				'blur', 'preclick', 'load', 'unload', 'viewreset', 'movestart', 'move', 'moveend', 'dragstart', 'drag',
				'dragend', 'zoomstart', 'zoomend', 'zoomlevelschange', 'resize', 'autopanstart', 'layeradd', 'layerremove',
				'baselayerchange', 'overlayadd', 'overlayremove', 'locationfound', 'locationerror', 'popupopen', 'popupclose'
			];
			_.each(mapEventNames, function(mapEventName) {
				var handler = function() {
					//console.log('map:'+mapEventName);
					this.trigger('map:'+mapEventName);
				};
				handler = _.bind(handler, this);
				this.map.on(mapEventName, handler);
			}, this);
			_.each(this.mapEvents, function(handler, event) {
				handler = _.isString(handler) ? this[handler] : handler;
				if (_.isFunction(handler)) {
					handler = _.bind(handler, this);
					this.map.on(event, handler);
				}
			}, this);
		},
	});
	return MapView;
});

