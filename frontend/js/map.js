var infowindow = undefined
var map = undefined
var markers = []

function addMapToDocument(){
  var googleMapBaseUrl = "https://maps.googleapis.com/maps/api/js"
  var googleMapUrlKeyParams = "?key="+Credentials["google-maps"]
    +"&callback=initMap"
    +"&libraries="
    +"&v=weekly"
  var googleMap = document.createElement('script');
  googleMap.setAttribute("async", "")
  googleMap.src = googleMapBaseUrl+googleMapUrlKeyParams
  googleMap.async = true
  document.getElementsByTagName('head')[0].appendChild(googleMap)
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: new google.maps.LatLng(-15.6182046,-50.6699791),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    gestureHandling: 'none',
    zoomControl: false
  });

  infowindow = new google.maps.InfoWindow();



}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
  for (let i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
  setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}

function populateMap(map, infowindow, locations) {
  var marker, i;

  deleteMarkers()

  for (i = 0; i < locations.length; i++) { 
     
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });

    markers.push(marker)

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      
      return function() {
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
      }
    })(marker, i));
  }
}

addMapToDocument()

