/* A pagination module for select and input elements. 
*/
this.ckan.module('select2-pagination', function (jQuery) {
  return {
    options: {
      multiple: false,
      pageSize: 20
    },
    initialize: function () {
      $.proxyAll(this, /setup/, /format/);
      this.setupSelection(this.el.data('choices'));
    },
    setupSelection: function (data) {
      var self = this;
      var settings = {
        data: data,
        multiple: this.options.multiple,
        query: function(q) {
          var that = this;
          var pageSize = self.options.pageSize;
          var results = [];

          if (q.term && q.term !== '') {
            results = _.filter(that.data, function(e) {
              return e.text.toUpperCase().indexOf(q.term.toUpperCase()) >= 0;
            });
          } else if (q.term === '') {
            results = that.data;
          }

          var slicedResults = results.slice((q.page - 1) * pageSize, q.page * pageSize);

          q.callback({
            results: slicedResults,
            more: results.length >= q.page * pageSize
          });
        },
        formatNoMatches: this.formatNoMatches
      };
      var select2 = this.el.select2(settings);
      if (this.el.data('selected').length != 0) {
        select2.select2('data', this.el.data('selected'));
      }
    },
    formatNoMatches: function (term) {
      return this._('No matches found');
    }
  };
});
