let map;

function iniciarMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center:{lat:11.2258375 ,lng: -74.1890507},
    zoom: 8,
  });
}