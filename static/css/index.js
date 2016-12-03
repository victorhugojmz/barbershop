var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 19.3513955, lng: -99.1504914},
    zoom: 16
  });
  var icon = {
        url : 'static/images/calavera-final.ico',
        scaledSize: new google.maps.Size(90, 90),
        origin: new google.maps.Point(0,0), 
        anchor: new google.maps.Point(0,0) 
  }
  var marker = new google.maps.Marker({
    position: {lat: 19.3513955, lng: -99.1504914},
    map: map,
    title: 'Hello World!',
    icon: icon
  });
}
marker.setMap(map);
