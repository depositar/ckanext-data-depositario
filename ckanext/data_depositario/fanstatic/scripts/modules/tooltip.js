/* Add a tooltip to the element.
*/
ckan.module('tooltip', function (jQuery) {
  return {
    initialize: function () {
      this.el.tooltip();
    }
  };
});
