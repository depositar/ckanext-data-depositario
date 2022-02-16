/* Apply select2 to select boxes.
*/
ckan.module('select2-enabler', function (jQuery) {
  return {
    initialize: function () {
      this.el.select2();
    }
  };
});
