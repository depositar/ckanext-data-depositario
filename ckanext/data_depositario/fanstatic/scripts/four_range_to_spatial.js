$(document).ready(function(){
  $('#convert_from_four_range').click(function() {
    if ($.isNumeric($('#field-x_min').val()) && $.isNumeric($('#field-x_max').val()) && $.isNumeric($('#field-y_min').val()) && $.isNumeric($('#field-y_max').val())){
      if (parseFloat($('#field-x_min').val()) > parseFloat($('#field-x_max').val()) || parseFloat($('#field-y_min').val()) > parseFloat($('#field-y_max').val())){
        alert('X (Y) 之最小值需小於最大值');
      }
      else{
        var geojson = '{"type":"Polygon","coordinates":[[['+$('#field-x_min').val()+','+$('#field-y_min').val()+'],['+$('#field-x_min').val()+','+$('#field-y_max').val()+'],['+$('#field-x_max').val()+','+$('#field-y_max').val()+'],['+$('#field-x_max').val()+','+$('#field-y_min').val()+'],['+$('#field-x_min').val()+','+$('#field-y_min').val()+']]]}';
        $('#field-spatial').val(geojson);
      }
    }
    else{
      alert('請輸入完整四至座標資訊');
    }
  });
});
