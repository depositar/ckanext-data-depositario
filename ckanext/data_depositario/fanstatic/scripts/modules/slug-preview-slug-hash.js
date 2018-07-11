/* Modified version of ckan's slug-preview.js.
 * It generates sha1 hash as slug when the slugified name is empty.
 */
this.ckan.module('slug-preview-slug-hash', function (jQuery) {
  return {
    options: {
      prefix: '',
      placeholder: '<slug>'
    },

    initialize: function () {
      var sandbox = this.sandbox;
      var options = this.options;
      var el = this.el;
      var _ = sandbox.translate;

      var slug = el.slug();
      var parent = slug.parents('.control-group');
      var preview;

      if (!(parent.length)) {
        return;
      }

      // Leave the slug field visible
      if (!parent.hasClass('error')) {
        preview = parent.slugPreview({
          prefix: options.prefix,
          placeholder: options.placeholder,
          i18n: {
            'URL': this._('URL'),
            'Edit': this._('Edit')
          }
        });

        // If the user manually enters text into the input we cancel the slug
        // listeners so that we don't clobber the slug when the title next changes.
        slug.keypress(function () {
          if (event.charCode) {
            sandbox.publish('slug-preview-modified', preview[0]);
          }
        });

        sandbox.publish('slug-preview-created', preview[0]);

        // Horrible hack to make sure that IE7 rerenders the subsequent
        // DOM children correctly now that we've render the slug preview element
        // We should drop this horrible hack ASAP
        if (jQuery('html').hasClass('ie7')) {
          jQuery('.btn').on('click', preview, function(){
            jQuery('.controls').ie7redraw();
          });
          preview.hide();
          setTimeout(function() {
            preview.show();
            jQuery('.controls').ie7redraw();
          }, 10);
        }
      }

      // Watch for updates to the target field and update the hidden slug field
      // triggering the "change" event manually.
      sandbox.subscribe('slug-target-changed', function (value) {
        slug.val(value).trigger('change');
        // Generate sha1 hash as slug when the slugified name is empty.
        if (slug.val() == '' && value != '') {
          slug.val(sha1(value).substr(0, 5)).trigger('change');
        }
      });
    }
  };
});
