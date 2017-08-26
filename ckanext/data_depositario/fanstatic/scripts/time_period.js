function set_time_period(start, end) {
  $('#field-temp_res').val('year');
  $('#field-temp_res').attr('readonly', true);
  $('#field-start_time').val(start);
  $('#field-start_time').attr('disabled', false);
  $('#field-start_time').attr('readonly', true);
  $('#field-end_time').val(end);
  $('#field-end_time').attr('disabled', false);
  $('#field-end_time').attr('readonly', true);
}
$('#time_period').on('select2-selecting', function(e) {
  var date = e.val.split('-');
  var start = date[0];
  var end = date[1];
  if (end == '') {
    end = $.datepicker.formatDate('yy', new Date());
  }
  set_time_period(start, end);
  if (e.val == '') {
    $('#field-temp_res').attr('readonly', false);
    $('#field-start_time').attr('readonly', false);
    $('#field-end_time').attr('readonly', false);
  }
});
