# Leaflet.GridLayer.GoogleMutant

A [LeafletJS](http://www.leafletjs.com) plugin to use Google maps basemaps.

## Demo

[http://ivansanchez.gitlab.io/Leaflet.GridLayer.GoogleMutant/demo.html](http://ivansanchez.gitlab.io/Leaflet.GridLayer.GoogleMutant/demo.html)

## Why?

It is already possible to display Google Maps in Leaflet, but unfortunately the state of the art is far from perfect:

* [Shramov's Leaflet plugin implementation](https://github.com/shramov/leaflet-plugins) (as well as an old, not recommended [OpenLayers technique](http://openlayers.org/en/v3.0.0/examples/google-map.html)) suffer from a [big drawback](https://github.com/shramov/leaflet-plugins/issues/111): the basemap and whatever overlays are on top are *off sync*. This is very noticeable when dragging or zooming.
* [MapGear's implementation with OpenLayers](https://github.com/mapgears/ol3-google-maps) uses a different technique (decorate OL3 with GMaps methods), but has a different set of [limitations](https://github.com/mapgears/ol3-google-maps/blob/master/LIMITATIONS.md).
* [Avin Mathew's implementation](https://avinmathew.com/leaflet-and-google-maps/) uses a clever timer-based technique, but it requires jQuery and still feels jittery due to the timers.

In order to provide the best Leaflet experience, GoogleMutant uses both [DOM mutation observers](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) and `L.GridLayer` from Leaflet 1.0.0. The basemap tiles are still requested *through* the Google maps JavaScript API, but they switch places to use Leaflet drag and zoom.

## Compatibility

This plugin doesn't work on IE10 or lower, as [that browser doesn't implement DOM mutation observers](http://caniuse.com/#search=mutation). Chrome, Firefox, Safari, IE11 and Edge are fine.

## Usage

Include the GMaps JS API in your HTML, plus Leaflet:

```
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY" async defer></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.1/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.0.1/dist/leaflet.js"></script>
```

Include the GoogleMutant javascript file (alternatively, fetch a local copy with `npm install --save leaflet.gridlayer.googlemutant` or `yarn add leaflet.gridlayer.googlemutant`):

```
<script src='https://unpkg.com/leaflet.gridlayer.googlemutant@latest/Leaflet.GoogleMutant.js'></script>
```

Then, you can create an instance of `L.GridLayer.GoogleMutant` on your JS code:

```
var roads = L.gridLayer.googleMutant({
	type: 'roadmap'	// valid values are 'roadmap', 'satellite', 'terrain' and 'hybrid'
}).addTo(map);
```

It's also possible to use [custom styling](https://developers.google.com/maps/documentation/javascript/styling)
by passing a value to the `style` option, e.g.:

```
var styled = L.gridLayer.googleMutant({
	type: 'roadmap',
	styles: [
		{elementType: 'labels', stylers: [{visibility: 'off'}]},
		{featureType: 'water', stylers: [{color: '#444444'}]}
	]
}).addTo(map);
```


## Known caveats

`hybrid` mode prunes tiles before needed for no apparent reason, so the map flickers when there is a zoom change.


## Legalese

----------------------------------------------------------------------------

"THE BEER-WARE LICENSE":
<ivan@sanchezortega.es> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.

----------------------------------------------------------------------------

