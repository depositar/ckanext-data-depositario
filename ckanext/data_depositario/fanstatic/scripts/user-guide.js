this.ckan.module('intro-action', function (jQuery, _) {
  return {
    /* An object of module options */
    options: {
      /* Locale options can be overidden with data-module-i18n attribute */
      i18n: {
        keywordSearch: _('Here you can search datasets by a keyword.'),
        spatialSearch: _('Here you can search datasets by the map.'),
        temporalSearch: _('Here you can search datasets by a period of time.'),
        filter: _('Here you can filter datasets.'),
        datasetList: _('The matched datasets will list here.'),
        showHelp: _('Click this question mark to show this help again.'),
        skip: _('Skip'),
        done: _('Confirm')
      },
       template: [
         '<i id="intro-switch" class="icon-question-sign icon-large pull-right">',
         '</i>'
       ].join('\n')
    },

    initialize: function () {
      intro = introJs();
      var introStart = true;
      var visited = localStorage.getItem('intro');
      introStart = visited ? false : true;
      var md = new MobileDetect(window.navigator.userAgent);
      var isMobile = md.mobile() ? true : false;

      if(jQuery('html').attr('lang') == 'zh_TW') {
        locale_data = ckan.i18n.options.locale_data.ckan;
        jQuery.extend(locale_data, this.getLocale());
      }

      intro.setOptions({
        overlayOpacity: 0.5,
        nextLabel: ' &rarr; ',
        prevLabel: '&larr; ',
        showStepNumbers: false,
        skipLabel: this.i18n('skip'),
        doneLabel: this.i18n('done'),
        steps: [
          {
            element: '.search-input',
            intro: this.i18n('keywordSearch')
          },
	  {
	    element: '#dataset-map',
	    intro: this.i18n('spatialSearch'),
	    position: 'right'
	  },
          {
            element: '[data-module="date-facet"]',
            intro: this.i18n('temporalSearch'),
            position: 'right'
          },
          {
            element: '#facets',
            intro: this.i18n('filter'),
            position: 'right'
          },
          {
            element: '.dataset-list',
            intro: this.i18n('datasetList'),
            position: 'right'
          },
          {
            element: '#intro-switch',
            intro: this.i18n('showHelp'),
            position: 'right'
          }
        ]
      });

      if(isMobile) {
        introStart = false;
      } else {
        this.createMark().appendTo('.breadcrumb .active');
	this.mark.css({
          'cursor': 'pointer',
	  'color': '#d9534f'
        });
	this.mark.on('click', this._onClick);
      }

      if(introStart) {
        localStorage.setItem('intro', 1);
        intro.start();
      }
    },

    getLocale: function () {
      return {
        "Here you can search datasets by a keyword.": [
          null,
          "您可以在此進行關鍵字搜尋。"
        ],
        "Here you can search datasets by the map.": [
          null,
          "您可以在此進行空間搜尋。"
        ],
        "Here you can search datasets by a period of time.": [
          null,
          "您可以在此進行時間搜尋。"
        ],
        "Here you can filter datasets.": [
          null,
          "您可以在此過濾資料集。"
        ],
        "The matched datasets will list here.": [
          null,
          "符合搜尋條件的資料集將顯示在這裡。"
        ],
        "Click this question mark to show this help again.": [
          null,
          "點選此問號按鈕再次觀看導覽。"
        ],
        "Skip": [
          null,
          "略過"
        ]
      };
    },

    createMark: function () {
      if (!this.mark) {
        var element = this.mark = jQuery(this.options.template);
      }
      return this.mark;
    },

    _onClick: function(event) {
      intro.start();
    }
  }
});
