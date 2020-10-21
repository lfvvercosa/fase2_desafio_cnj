
function addMapToDocument(){
  var googleMapBaseUrl = "https://maps.googleapis.com/maps/api/js"
  var googleMapUrlKeyParams = "?key="+Credentials["google-maps"]
    +"&callback=initMap"
    +"&libraries="
    +"&v=weekly"
  var googleMap = document.createElement('script');
  googleMap.src = googleMapBaseUrl+googleMapUrlKeyParams
  googleMap.async = true
  document.getElementsByTagName('head')[0].appendChild(googleMap)
}

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: new google.maps.LatLng(-11.6182046,-50.6699791),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    gestureHandling: 'none',
    zoomControl: false
  });

  var infowindow = new google.maps.InfoWindow();

  getCourtList((locations)=>{
    populateMap(map, infowindow, locations)
  })
}

function populateMap(map, infowindow, locations) {
  var marker, i;

  for (i = 0; i < locations.length; i++) {  
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
      }
    })(marker, i));
  }
}

addMapToDocument()

