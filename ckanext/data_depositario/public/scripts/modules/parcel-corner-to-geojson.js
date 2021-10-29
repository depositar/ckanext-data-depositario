/* Generate GeoJson from parcel corner coordinates.
 */
this.ckan.module('parcel-corner-to-geojson', function (jQuery) {
  return {
    options: {
      x_min: $('#field-x_min'),
      x_max: $('#field-x_max'),
      y_min: $('#field-y_min'),
      y_max: $('#field-y_max'),
      spatial: $('#field-spatial')
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.el.on('click', this._onClick);
    },
    _onClick: function() {
      if ($.isNumeric(this.options.x_min.val()) &&
          $.isNumeric(this.options.x_max.val()) &&
          $.isNumeric(this.options.y_min.val()) &&
          $.isNumeric(this.options.y_max.val())) {
        if (parseFloat(this.options.x_min.val()) > parseFloat(this.options.x_max.val())
            || parseFloat(this.options.y_min.val()) > parseFloat(this.options.y_max.val())) {
          alert(this._('The value of X.max (Y.max) must be greater than the value of X.min (Y.min).'));
        }
        else {
          var geojson = '{"type":"Polygon","coordinates":[[[' +
                        this.options.x_min.val() + ',' +
                        this.options.y_min.val() + '],[' +
                        this.options.x_min.val() + ',' +
                        this.options.y_max.val() + '],[' +
                        this.options.x_max.val() + ',' +
                        this.options.y_max.val() + '],[' +
                        this.options.x_max.val() + ',' +
                        this.options.y_min.val() + '],[' +
                        this.options.x_min.val() + ',' +
                        this.options.y_min.val() + ']]]}';
          this.options.spatial.val(geojson);
        }
      }
      else {
        alert(this._('Please fill in parcel corner coordinates.'));
      }
    }
  };
});
