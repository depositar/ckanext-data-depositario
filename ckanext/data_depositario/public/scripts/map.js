ckan.module('map', function (jQuery) {
  return {
    initialize: function () {
      var self = this;

      self.map = L.map('map', {
        center: [23.04, 120.18],
        zoom: 11,
        maxZoom: 18
      });

      self.gmap_api_key = this.options.gmap_config.api_key;

      $(document).ready(function() {
        $('body').append('<script src="https://maps.google.com/maps/api/js?v=3&key=' + self.gmap_api_key + '" type="text/javascript" async defer></script>');
	self.showMap();
      });
    },

    showMap: function () {
      var self = this;

      // NLSC tile layer
      var nlsc = L.tileLayer('http://maps.nlsc.gov.tw/S_Maps/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=EMAP&STYLE=_null&TILEMATRIXSET=EPSG:3857&TILEMATRIX=EPSG:3857:{z}&TILEROW={y}&TILECOL={x}&FORMAT=image/png', {
        attribution: '內政部國土測繪中心'
      });
      // Thunderforest tile layer
      var tf = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map tiles & Data by <a href="http://www.openstreetmap.org" class="external">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/2.0/" class="external">CC BY-SA</a>.'
      });
      // Google Maps tile layer
      var ggl = new L.gridLayer.googleMutant({type: 'roadmap'});
      var ggls = new L.gridLayer.googleMutant({type: 'hybrid'});

      function showPolygonArea(e) {
        var geometry = JSON.stringify(e.layer.toGeoJSON().geometry);
        var north_east = {};
	var south_west = {};

        if (e.layer.getBounds) {
	  north_east = e.layer.getBounds().getNorthEast();
	  south_west = e.layer.getBounds().getSouthWest();
        }
        var field_values = [
          {'field': '#field-spatial', 'value': geometry},
          {'field': '#field-x_min', 'value': south_west.lng || ''},
          {'field': '#field-x_max', 'value': north_east.lng || ''},
          {'field': '#field-y_min', 'value': south_west.lat || ''},
          {'field': '#field-y_max', 'value': north_east.lat || ''}
        ];
        field_values.forEach(function(field_value) {
          $(field_value.field)
            .prop('readonly', true)
            .val(field_value.value);
        });
        featureGroup.clearLayers();
        featureGroup.addLayer(e.layer);
      }

      function showPolygonAreaEdited(e) {
        e.layers.eachLayer(function(layer) {
          showPolygonArea({ layer: layer });
        });
      }

      function deleteFieldValues(e) {
        // if the layer has been deleted, remove the spatial field values, too.
        if (e.layers.getLayers().length != 0) {
          var fields = ['#field-spatial', '#field-x_min', '#field-x_max', '#field-y_min',
            '#field-y_max'];
          fields.forEach(function(field) {
            $(field).val('').prop('readonly', false);
          });
        }
      }

      // add layer control
      self.map.addLayer(tf);
      self.map.addControl(new L.control.layers({"OpenStreetMap": tf, "Google Maps": ggl, "Google Maps (衛星)": ggls, "通用版電子地圖": nlsc}));
      featureGroup = L.featureGroup().addTo(self.map);

      // add draw control
      var drawControl = new L.Control.Draw({
        edit: {
          featureGroup: featureGroup,
          poly: {
            allowIntersection: false
          }
        },
        draw: {
          polygon: {
            allowIntersection: false,
            showArea: true
          },
          circle: false,
          circlemarker: false
        }
      }).addTo(self.map);

      self.map.on('draw:created', showPolygonArea);
      self.map.on('draw:edited', showPolygonAreaEdited);
      self.map.on('draw:deleted', deleteFieldValues);

      // hide the map first
      $('#map').hide();

      // show the map if the spatial column exists
      if ($('#field-spatial').val() != '') {
        var geojson = jQuery.parseJSON($('#field-spatial').val());
        var extentLayer = L.geoJson(geojson, {style: function (feature) {
          return {color: '#444444'};
        }}).addTo(self.map);
        if (geojson.type == 'Point') {
          self.map.setView(L.latLng(geojson.coordinates[1], geojson.coordinates[0]), 9);
        } else {
          self.map.fitBounds(extentLayer.getBounds());
        }
        $('#map').show();
      }

      $('#show_map').click(function() {
        $('#map').toggle();
      });
    }
  }
});
