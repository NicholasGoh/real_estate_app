// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
function initMap() {

  var count = 1;

  // function to read the json file
  function readJSON(file, callback){
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType('application/json');
    xobj.open('GET', file, true);
    xobj.onreadystatechange = function(){
      if (xobj.readyState == 4 && xobj.status =='200'){
        callback(xobj.responseText);
      }
    };
    xobj.send(null);
  };

  // call to read JSON and place all the markers
  readJSON('transactions.json', function(data) {
    var mydata = JSON.parse(data);
    const markers = [];
    const properties = [];

    // extract all the properties from the JSON and push into arrays
    for (const [propName, value] of Object.entries(mydata)){
      markers.push(value);
      properties.push(propName);
    };

    // initializing a new map
    var mapOptions = {
      center: new google.maps.LatLng(markers[0].x, markers[0].y),
      zoom: 10,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapOptions);

    //Create and open InfoWindow.
    var infoWindow = new google.maps.InfoWindow();
    for (var i = 0; i < 50; i++) {
      var data = markers[i];
      var property = properties[i];
      var myLatlng = new google.maps.LatLng(data.x, data.y);
      var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: property
      });

        // Attach click event to the marker.
      (function (marker, data) {
        google.maps.event.addListener(marker, "mouseover", function (e) {
          infoWindow.setContent("<div style = 'width:200px;min-height:40px'>" + marker.title + "</div>");
          infoWindow.open(map, marker);
        });
        google.maps.event.addListener(marker, "mouseout", function (e) {
          infoWindow.close(map, marker);
        });
        google.maps.event.addListener(marker, "click", function (e) {
          console.log(marker.title + ' clicked');
          if (count <= 4){
            var cell_num = 'cell' + count.toString();
            var cell = document.getElementById(cell_num);
            cell.innerHTML = "<div style = 'width:200px;min-height:40px'>" + marker.title + "</div>";
            count ++;
            console.log(count);
          } else {
            alert('4 properties already added');
          }
        });
      })(marker, data);
    }

  });
};
