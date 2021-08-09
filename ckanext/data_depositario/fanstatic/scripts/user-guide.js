this.ckan.module('intro-action', function (jQuery) {
  return {
    /* An object of module options */
    options: {
       template: [
         '<a id="intro-switch" href="#" class="btn question"><i class="fa fa-large fa-question-circle"></i></a>',
         '<i class="icon-question-sign"></i>',
         '</i>',
         '</a>'
       ].join('\n')
    },

    initialize: function () {
      intro = introJs();
      var introStart = true;
      var visited = localStorage.getItem('intro');
      introStart = visited ? false : true;
      var md = new MobileDetect(window.navigator.userAgent);
      var isMobile = md.mobile() ? true : false;

      intro.setOptions({
        overlayOpacity: 0.5,
        nextLabel: ' &rarr; ',
        prevLabel: '&larr; ',
        showStepNumbers: false,
        skipLabel: this._('Skip'),
        doneLabel: this._('Confirm'),
        steps: [
          {
            element: '.search-input',
            intro: this._('Here you can search datasets by a keyword.')
          },
	  {
	    element: '#dataset-map',
	    intro: this._('Here you can search datasets by the map.'),
	    position: 'right'
	  },
          {
            element: '[data-module="date-facet"]',
            intro: this._('Here you can search datasets by a period of time.'),
            position: 'right'
          },
          {
            element: '#facets',
            intro: this._('Here you can filter datasets.'),
            position: 'right'
          },
          {
            element: '.dataset-list',
            intro: this._('The matched datasets will list here.'),
            position: 'right'
          },
          {
            element: '#intro-switch',
            intro: this._('Click this question mark to show this help again.'),
            position: 'right'
          }
        ]
      });

      if(isMobile) {
        introStart = false;
      } else {
        this.createMark().appendTo('.breadcrumb .active');
	this.mark.on('click', this._onClick);
      }

      if(introStart) {
        localStorage.setItem('intro', 1);
        intro.start();
      }
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
