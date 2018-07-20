/* Maintainer information autofill
 */
this.ckan.module('maintainer', function (jQuery) {
  return {
    options: {
      maintainer_autofill: $('#maintainer_autofill'),
      field_maintainer_name: $('#field-maintainer_name'),
      field_maintainer_mail: $('#field-maintainer_mail')
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.options.maintainer_autofill.on('click', this._onMaintainerAutoFillClick);
    },
    _onMaintainerAutoFillClick: function() {
      this.options.field_maintainer_name
        .val(this.options.account_display_name);
      this.options.field_maintainer_mail
        .val(this.options.account_email);
    }
  };
});
