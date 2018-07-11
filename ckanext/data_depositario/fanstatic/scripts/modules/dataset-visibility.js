/* Dataset visibility toggler
 * When an organization is selected in the org dropdown then show a checkbox and
 * let user decide whether open this dataset or not
 */
this.ckan.module('dataset-visibility-checkbox', function (jQuery) {
  return {
    options: {
      organizations: $('#field-organizations'),
      visibility: $('#fieldset-private'),
      visibility_cb: $('#field-private-checkbox'),
      visibility_value: $('#field-private')
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.options.currentValue = this.options.visibility_value.val();
      this.options.organizations.on('change', this._onOrganizationChange);
      this._onOrganizationChange();
      this.options.visibility_cb.on('change', this._onPrivateChange);
    },
    _onOrganizationChange: function() {
      var value = this.options.organizations.val();
      if (value) {
        this.options.visibility
          .toggle(true);
      } else {
        this.options.visibility
	  .toggle(false);
	this.options.visibility_cb
	  .prop('checked', false);
        this.options.visibility_value
	  .val('false');
      }
    },
    _onPrivateChange: function() {
      this.options.visibility_value
        .val(this.options.visibility_cb.prop('checked'));
    }
  };
});
