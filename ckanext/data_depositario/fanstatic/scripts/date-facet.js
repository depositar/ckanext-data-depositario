(function(ckan, moment, document) {
  ckan.module('date-facet', function($, _) {
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
        $('input', this.el).datepicker({
          dateFormat: 'yy-mm-dd'
        });

        var form = $(".search-form");
        $('<input type="hidden" />').attr({'id': 'ext_begin_date', 'name': 'ext_begin_date', 'value': this.options.default_begin}).appendTo(form);
        $('<input type="hidden" />').attr({'id': 'ext_end_date', 'name': 'ext_end_date', 'value': this.options.default_end}).appendTo(form);

        var defaultValues = {
          min: this._getDate(this.options.default_begin),
          max: this._getDate(this.options.default_end)
        };
        if (defaultValues.min === '' && defaultValues.max === '') {
          defaultValues.min = this._getDate(this.options.begin);
          defaultValues.max = this._getDate(this.options.end);
	  $('[id="ext_begin_date"]').removeAttr('value');
	  $('[id="ext_end_date"]').removeAttr('value');
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
            defaultValues: defaultValues
          })
          .on('userValuesChanged', this._handleSliderChanged);

        $('[id="field-time-period"]', this.el).change(this._setTimePeriod);
	$('.show-filters').click(this._checkForChanges);
      },
      _convertDate: function (date) {
        return moment(date).format('YYYY-MM-DD');
      },
      _getDate: function (date) {
        if (date.length !== 0 && date !== true) {
          return new Date(date);
        }
        return '';
      },
      _handleSliderChanged: function (event, data) {
	var url = document.URL;
	url = this._updateQueryStringParameter(url, 'ext_begin_date', this._convertDate(data.values.min));
	url = this._updateQueryStringParameter(url, 'ext_end_date', this._convertDate(data.values.max));
	window.location = url;
      },
      _handleUpdateURL: function (event) {
        var url = document.URL;
        url = this._updateQueryStringParameter(url, 'ext_begin_date', $('[name="begin"]', this.el).val());
        url = this._updateQueryStringParameter(url, 'ext_end_date', $('[name="end"]', this.el).val());
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
      _setTimePeriod: function (event) {
        var selected = $('[id="field-time-period"] :selected');
	if (selected.index() == 0) return;
	if (selected.data('end') == '') selected.data('end', new Date().getFullYear());
	var url = document.URL;
	url = this._updateQueryStringParameter(url, 'ext_begin_date', selected.data('start') + '-01-01');
	url = this._updateQueryStringParameter(url, 'ext_end_date', selected.data('end') + '-12-31');
	window.location = url;
      },
      _checkForChanges: function (event) {
	$('[id="field-time-period"]', this.el).css('width', '100%').css('padding', '0').css('margin', '0');
        $('[id="dateSlider"]', this.el).dateRangeSlider('resize');
      }
    };
  });
}(window.ckan, window.moment, document));
