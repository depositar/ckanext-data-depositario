if ($('#field-temp_res').val() == '') {
  $('#field-start_time').attr('disabled', true);
  $('#field-end_time').attr('disabled', true);
}

function control_fields(value) {
  $('#field-start_time').attr('disabled', false);
  $('#field-end_time').attr('disabled', false);
  if ($.inArray(value, ['']) == 0) {
    $('#field-start_time').val('');
    $('#field-start_time').attr('disabled', true);
    $('#field-end_time').val('');
    $('#field-end_time').attr('disabled', true);
  }
}
$('#field-temp_res').change(function(e) {control_fields($('#field-temp_res').val())});
