/* Contact person information autofill
 */
this.ckan.module('contact_person', function (jQuery) {
  return {
    options: {
      contact_person_autofill: $('#contact_person_autofill'),
      field_contact_person: $('#field-contact_person'),
      field_contact_email: $('#field-contact_email')
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.options.contact_person_autofill.on('click', this._onAutoFillClick);
    },
    _onAutoFillClick: function() {
      this.options.field_contact_person
        .val(this.options.account_display_name);
      this.options.field_contact_email
        .val(this.options.account_email);
    }
  };
});
