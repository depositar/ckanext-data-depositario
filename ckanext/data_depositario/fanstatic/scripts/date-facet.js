(function(ckan, moment, document) {
  ckan.module('date-facet', function(jQuery) {
    return {
      options : {
        begin: null,
        end: null,
        default_begin: null,
        default_end: null
      },
      initialize: function () {
        $.proxyAll(this, /_/);

        this.el.removeClass('js-hide');

        var form = $(".search-form");
        $('<input type="hidden" />').attr({'id': 'ext_begin', 'name': 'ext_begin', 'value': this.options.default_begin}).appendTo(form);
        $('<input type="hidden" />').attr({'id': 'ext_end', 'name': 'ext_end', 'value': this.options.default_end}).appendTo(form);

        var defaultValues = {
          min: this._getDate(this.options.default_begin),
          max: this._getDate(this.options.default_end)
        };
        if (defaultValues.min === '' && defaultValues.max === '') {
          defaultValues.min = this._getDate(this.options.begin);
          defaultValues.max = this._getDate(this.options.end);
	  $('[id="ext_begin"]').removeAttr('value');
	  $('[id="ext_end"]').removeAttr('value');
        }

        $('<div id="dateSlider" />')
          .insertAfter($('.module-heading', this.el))
          .dateRangeSlider({
            valueLabels:"change",
            delayOut: 4000,
            bounds: {
              min: this._getDate(this.options.begin),
              max: this._getDate(this.options.end)
            },
            defaultValues: defaultValues,
            formatter: this._sliderFormatter
          })
          .on('userValuesChanged', this._handleSliderChanged);

	$('.show-filters').click(this._checkForChanges);
      },
      _convertDate: function (date) {
        return moment(date).format('YYYY');
      },
      _getDate: function (date) {
        if (date.length !== 0 && date !== true) {
          return new Date(date.toString());
        }
        return '';
      },
      _handleSliderChanged: function (event, data) {
	var url = document.URL;
	url = this._updateQueryStringParameter(url, 'ext_begin', this._convertDate(data.values.min));
	url = this._updateQueryStringParameter(url, 'ext_end', this._convertDate(data.values.max));
	window.location = url;
      },
      _handleUpdateURL: function (event) {
        var url = document.URL;
        url = this._updateQueryStringParameter(url, 'ext_begin', $('[name="begin"]', this.el).val());
        url = this._updateQueryStringParameter(url, 'ext_end', $('[name="end"]', this.el).val());
        window.location = url;
      },
      _updateQueryStringParameter: function (uri, key, value) {
        var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
        var separator = uri.indexOf('?') !== -1 ? "&" : "?";
        if (uri.match(re)) {
          return uri.replace(re, '$1' + key + "=" + value + '$2');
        } else {
          return uri + separator + key + "=" + value;
        }
      },
      _checkForChanges: function (event) {
        $('[id="dateSlider"]', this.el).dateRangeSlider('resize');
      },
      _sliderFormatter: function (value) {
        return value.getFullYear();
      }
    };
  });
}(window.ckan, window.moment, document));
