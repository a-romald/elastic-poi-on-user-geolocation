var map;
var markerObjects = [];
var markerCluster;
var infowindow;

var clusterStyles = [
    {
        url: '/media/img/cluster.png',
        textSize: 12,
        width: 42,
        height: 75
    },
];




String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}



function getMarkers(lat, lon) {
	icons = {
         "museum": {
             size: new google.maps.Size(50, 50),
             origin: new google.maps.Point(0, 0),
             anchor: new google.maps.Point(0, 60),
             url: "/media/img/museum.png"
         },
         "airport": {
              size: new google.maps.Size(50, 50),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(20, 60),
              url: "/media/img/airport.png"
          },
          "hotel": {
              size: new google.maps.Size(50, 50),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(20, 60),
              url: "/media/img/hotel.png"
           }
    }

	$.ajax({
		  type: "GET",
		  url: "/poi/",
		  data: { lat: lat, lon: lon },
		  dataType: "json",
	  	  success: function(data){
			    var points = data.points;
          markerObjects = [];
          $.each(points, function(i, point) {
		        	var mlat = point.lat;
		        	var mlon = point.lon;
		        	var mtitle = point.title;
		        	var maddress = (point.address != null) ? point.address : '';
		        	var mcity = point.city;
		        	var mcountry = point.country;
		        	var type = point.type;
		        	var micon = '';
		        	if (type) micon = icons[type];
	                
		        	var LatLong = new google.maps.LatLng(mlat, mlon);
    					var marker = new google.maps.Marker({
    					  position: LatLong,
    					  map: map,
    					  title: mtitle,
    					  icon: micon
    					});
    					marker.setMap(map);				

    					infowindow = new google.maps.InfoWindow();
    					
    					google.maps.event.addListener(marker, "click", function() {
    					  infowindow.open(map, marker);
    					  infowindow.setContent("<h4>" + type.capitalize() + "</h4>" + mtitle + "<br>" + mcity + ", " + mcountry + "<br>" + maddress );
    					});

    					markerObjects.push(marker);
		      });
			    
  				markerCluster = new MarkerClusterer(map, markerObjects, {styles: clusterStyles});
  				//console.log(markerObjects);

		  } // end success ajax
	});
	
}





function dragMap() {
    icons = {
         "museum": {
             size: new google.maps.Size(50, 50),
             origin: new google.maps.Point(0, 0),
             anchor: new google.maps.Point(0, 60),
             url: "/media/img/museum.png"
         },
         "airport": {
              size: new google.maps.Size(50, 50),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(20, 60),
              url: "/media/img/airport.png"
          },
          "hotel": {
              size: new google.maps.Size(50, 50),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(20, 60),
              url: "/media/img/hotel.png"
           }
    }

    var bounds =  map.getBounds();    

    var top_left_lat  =   map.getBounds().getNorthEast().lat();
    var top_left_lon   =   map.getBounds().getSouthWest().lng();
    var bottom_right_lat  =   map.getBounds().getSouthWest().lat();
    var bottom_right_lon   =   map.getBounds().getNorthEast().lng();
    
    //do whatever you want with those bounds
    $.ajax({
      type: "GET",
        url: "/get_draged/",
        data: { top_left_lat: top_left_lat, top_left_lon: top_left_lon, bottom_right_lat: bottom_right_lat, bottom_right_lon: bottom_right_lon },
        dataType: "json",
          success: function(data){
            var points = data.points;            
            markerCluster.clearMarkers();
            markerObjects = [];
            $.each(points, function(i, point) {
                var mlat = point.lat;
                var mlon = point.lon;
                var mtitle = point.title;
                var maddress = (point.address != null) ? point.address : '';
                var mcity = point.city;
                var mcountry = point.country;
                var type = point.type;
                var micon = '';
                if (type) micon = icons[type];
                    
                var LatLong = new google.maps.LatLng(mlat, mlon);
                var marker = new google.maps.Marker({
                  position: LatLong,
                  map: map,
                  title: mtitle,
                  icon: micon
                });
                marker.setMap(map);       

                infowindow = new google.maps.InfoWindow();
                
                google.maps.event.addListener(marker, "click", function() {
                  infowindow.open(map, marker);
                  infowindow.setContent("<h4>" + type.capitalize() + "</h4>" + mtitle + "<br>" + mcity + ", " + mcountry + "<br>" + maddress );
                });
                
                markerObjects.push(marker);
            });
            
            markerCluster = new MarkerClusterer(map, markerObjects, {styles: clusterStyles});
        } // end success ajax
    });
    
}





function initGoogleMap(lat, lon) {
	
    var area_lat = parseFloat(lat);
    var area_lng = parseFloat(lon);
    var zoom = 13;
    var latLong = new google.maps.LatLng(lat, lon);
    map = new google.maps.Map(document.getElementById('map'), {
        center: latLong,
        zoom: zoom,
        zoomControl: true,
        mapTypeControl: true,
        scaleControl: false,
        scrollwheel: false,
        streetViewControl: true,
        rotateControl: true,
        mapTypeControlOptions: {
            mapTypeIds: [
                google.maps.MapTypeId.ROADMAP,
                google.maps.MapTypeId.TERRAIN,
                google.maps.MapTypeId.SATELLITE,
                google.maps.MapTypeId.HYBRID
            ]
        }
    });
    //Grayscale map
	  var style = [{ "elementType": "geometry", "stylers": [{ "saturation": -100 }]}];
    var mapType = new google.maps.StyledMapType(style, {name:"Grayscale"});
    map.mapTypes.set('grey', mapType);
    map.setMapTypeId('grey');
    //map.setMapTypeId(google.maps.MapTypeId.ROADMAP);

    getMarkers(lat, lon);


    //also event 'bounds_changed', 'zoom_changed'
    google.maps.event.addListener(map, 'dragend', function() {            
            dragMap();            
    });

    google.maps.event.addListener( map, 'zoom_changed', function(){
          google.maps.event.trigger(this, 'dragend');} 
    );
	
}






function show_map(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    
    //document.write(latitude + ', ' + longitude);
    initGoogleMap(latitude, longitude)
}



function error(msg) {
	/*var p = document.querySelector("p");
	switch (msg.code) {
		case 1: message = 'PERMISSION_DENIED'; break;
		case 2: message = 'POSITION_UNAVAILABLE'; break;
		case 3: message = 'TIMEOUT'; break;
	}
	p.innerHTML = 'Geolocation error: ' + message;*/
	initGoogleMap(51.509865, -0.118092) //London
}



function get_location() {	
	if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(show_map, error, {
			enableHighAccuracy: false,
			timeout: 200000,
			maximumAge: 0
		});
  }
  else {
      //no native support
  }
}



function toggleAllMarkers() {
    for (var i = 0; i < markerObjects.length; i++) {
          markerObjects[i].setVisible(true);
    }
    markerCluster.addMarkers(markerObjects);

    $('#checkMuseum').prop('checked', false);
    $('#checkAirport').prop('checked', false);
    $('#checkHotel').prop('checked', false);     
}



function toggleMarkers(){    
    $( "#checkAll" ).prop( "checked", false );
    
    var allChecked = [];
    $('input.gmarker:checkbox:checked').each(function () {
        allChecked.push($(this).val());
    });

    if (allChecked.length > 0) {
        for (var i = 0; i < markerObjects.length; i++) {
            markerObjects[i].setVisible(false);
        }
        markerCluster.clearMarkers();

        allChecked.forEach(function(ch) {
            if (icons.hasOwnProperty(ch)) {
                pict = icons[ch].url;
                for (var i = 0; i < markerObjects.length; i++) {
                    if (markerObjects[i].icon.url == pict) {
                        markerObjects[i].setVisible(true);
                        markerCluster.addMarker(markerObjects[i]);
                    }
                }
            }            
        });
    }
    else {
        $( "#checkAll" ).prop( "checked", true );
        for (var i = 0; i < markerObjects.length; i++) {
            markerObjects[i].setVisible(true);
        }
        markerCluster.addMarkers(markerObjects);        
    }
}





//navigator.geolocation.getCurrentPosition(show_map, handle_error); //Call it so possible
window.onload = function() {
    get_location();
}