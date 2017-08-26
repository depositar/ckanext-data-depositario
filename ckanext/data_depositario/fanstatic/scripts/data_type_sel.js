var all_fields = ['#book-fields', '#image-fields', '#spatial-type-fields']
var need_book_fields = ['books'];
var need_scanned_image_fields = ['pics_non_spatial', 'pics_spatial'];
var need_spatial_fields = ['pics_spatial', 'grid', 'vector', 'tin', 'steropair'];
var sel_data_type = $('#field-data_type').val();
function show_fields(value) {
  var fields_toggle = [false, false, false];
  if ($.inArray(value, need_book_fields) != -1) {
    fields_toggle[0] = true;
  }
  if ($.inArray(value, need_scanned_image_fields) != -1) {
    fields_toggle[1] = true;
  }
  if ($.inArray(value, need_spatial_fields) != -1) {
    fields_toggle[2] = true;
  }
  $.each(all_fields, function(index, value) {
    if (fields_toggle[index]) {$(value).show();} else {$(value).hide();}
  });
}
$(function () {show_fields(sel_data_type)});
$('#field-data_type').on('select2-selecting', function(e) {show_fields(e.val)});
