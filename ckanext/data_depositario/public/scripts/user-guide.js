this.ckan.module('intro-action', function (jQuery) {
  return {
    /* An object of module options */
    options: {
       template: [
         '<a id="intro-switch" href="#" class="btn btn-sm question"><i class="fa fa-lg fa-question-circle"></i></a>',
         '<i class="icon-question-sign"></i>',
         '</i>',
         '</a>'
       ].join('\n')
    },

    initialize: function () {
      const driver = window.driver.js.driver;
      var introStart = true;
      var visited = localStorage.getItem('intro');
      introStart = visited ? false : true;
      var md = new MobileDetect(window.navigator.userAgent);
      var isMobile = md.mobile() ? true : false;

      driverObj = driver({
        nextBtnText: ' &rarr; ',
        prevBtnText: '&larr; ',
        doneBtnText: this._('Confirm'),
        side: 'bottom',
        steps: [
          {
            element: '.search-input-group',
            popover: {
              description: this._('Here you can search datasets by a keyword.'),
              side: 'bottom'
            }
          },
	      {
	        element: '#dataset-map',
            popover: {
              description: this._('Here you can search datasets by the map.'),
              side: 'right'
            }
	      },
          {
            element: '#temporal-search',
            popover: {
              description: this._('Here you can search datasets by a period of time.'),
              side: 'right'
            }
          },
          {
            element: '.filters',
            popover: {
              description: this._('Here you can filter datasets.'),
              side: 'right'
            }
          },
          {
            element: '.dataset-list',
            popover: {
              description: this._('The matched datasets will list here.')
            }
          },
          {
            element: '#intro-switch',
            popover: {
              description: this._('Click this question mark to show this help again.'),
              side: 'right'
            }
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
        driverObj.drive();
      }
    },

    createMark: function () {
      if (!this.mark) {
        var element = this.mark = jQuery(this.options.template);
      }
      return this.mark;
    },

    _onClick: function(event) {
      driverObj.drive();
    }
  }
});
