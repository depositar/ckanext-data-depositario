/* Search and fill in wikidata entries as keywords
*/
this.ckan.module('input-wikidata', function ($, _) {   
  return {
    options: {
      language: $('html').attr('lang').replace('_', '-').toLowerCase(),
      i18n: {
        noMatches: _('No matches found'),
        inputTooShort: function (data) {
          return _('Input is too short, must be at least one character')
          .ifPlural(data.min, 'Input is too short, must be at least %(min)d characters');
        },
        formatSearching: _('Searching…'),
        label: _('Label'),
        description: _('Description')
      }
    },
    initialize: function () {
      $.proxyAll(this, /ajaxData/, /initSelection/, /format/, /results/);
      if ($('html').attr('lang') == 'zh_TW') {
        locale_data = ckan.i18n.options.locale_data.ckan;
        $.extend(locale_data, this.getLocale());
      }
      this.setupInputWikidata();
    },
    getLocale: function () {
      return {
        'Searching…': [
          null,
          '搜尋中...'
        ],
        'Label': [
          null,
          '標籤'
        ],
        'Description': [
          null,
          '描述'
        ]
      };
    },
    setupInputWikidata: function () {
      var settings = {
        minimumInputLength: 1,
        multiple: true,
        ajax: {
          url: "https://www.wikidata.org/w/api.php",
          dataType: 'jsonp',
          quietMillis: 250,
          data: this.ajaxData,
          results: this.results,
          cache: true
        },
        initSelection: this.initSelection,
        formatResult: this.formatResult,
        formatNoMatches: this.formatNoMatches,
        formatInputTooShort: this.formatInputTooShort,
        formatSearching: this.formatSearching,
        formatSelection: this.formatSelection,
        escapeMarkup: function (m) { return m; }  
      };
      var select2 = this.el.select2(settings).select2('val', this.el.data('selected'));
    },
    ajaxData: function (term) {
      return {
        action: 'wbsearchentities',
        search: term,
        language: this.options.language,
        limit: 20,
        format: 'json',
        uselang: this.options.language
      };
    },
    results: function (data) {
      return {
        results: (data.search.length > 0 ? [{
          id: 'ID',
          label: this.i18n('label'),
          description: this.i18n('description'),
          children: data.search,
          disabled: true
        }] : data.search)
      };
    },
    initSelection: function (element, callback) {
      var data = [];
      var language = this.options.language;
      if(element.val()) {
        element.val().split(',').forEach(function (e) {
          var url = wdk.getEntities({ids: e});
          $.get(url, function(entities) {
            if (entities.entities) {
              $.each(entities.entities, function (id, e) {
                new_label = e.labels[language] || e.labels['zh-hant'] || e.labels.zh || e.labels.en;
                data.push({id: e.id, text: new_label.value});
              });
              callback(data);
            }
          });
        });
      }
    },
    formatResult: function (entity, container, query) {
      var markup = '<div class="row-fluid">' +
        '<div class="span2">' + entity.id + '</div>' +
        '<div class="span9">' + '<div class="row-fluid">' +
        '<div class="span3">' + entity.label + '</div>' +
        '<div class="span6">' + (entity.description || '') + '</div>' +
        '</div></div></div>';
      return markup;
    },
    formatNoMatches: function (term) {
      return !term ? this.i18n('emptySearch') : this.i18n('noMatches');
    },
    formatInputTooShort: function (term, min) {
      return this.i18n('inputTooShort', {min: min});      
    },
    formatSearching: function () {
      return this.i18n('formatSearching');
    },
    formatSelection: function (element) {
      return element.text || element.label;
    }
  };
});
