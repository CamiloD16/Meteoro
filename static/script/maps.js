function iniciarMap(){
    var coord = {lat:11.2258375 ,lng: -74.1890507};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}