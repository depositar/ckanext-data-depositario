$('.show-filters').click(function() {
  setTimeout(function() {
    // Update the map when the filters for mobile are displayed
    map.invalidateSize();
    map.fitBounds([[21.86, 119.18], [25.37, 122.34]]);
  }, 10);
});
