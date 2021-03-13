// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
function initMap() {
    var j = JSON.parse(data);
    console.log(j[0].property_1);
    const hall2 = { lat: 1.2423, lng: 103.83684};

    const map = new google.maps.Map(document.getElementById("googleMap"), {
      zoom: 15,
      center: hall2,
    });

    const contentString =
      '<div id="content">' +
      '<div id="siteNotice">' +
      "</div>" +
      '<h1 id="firstHeading" class="firstHeading">NTU</h1>' +
      '<div id="bodyContent">' +
      "<p><b>NTU</b>, also referred to as <b>Pulau NTU</b>, is a place where people's "+
      "hopes and dreams go to die.</p>" +
      '<p>Attribution: NTU, <a href="#"</a> ' +
      "(last visited June 22, 2021).</p>" +
      "</div>" +
      "</div>";
    const infowindow = new google.maps.InfoWindow({
      content: contentString,
    });
    const marker = new google.maps.Marker({
      position: hall2,
      map
    });
    marker.addListener("mouseover", () => {
        infowindow.open(map, marker);
    });
    marker.addListener('mouseout', ()=>{
        infowindow.close(map, marker);
    })
    marker.addListener('click', ()=>{
        var a = document.getElementById('newtable').insertRow(0);
        var b = a.insertCell(0);
        var c = a.insertCell(1);
        var d = a.insertCell(2);
        b.innerHTML = 'Id'
        c.innerHTML = "row";
        d.innerHTML = contentString;
    })
  }
