let map;
let py_data = JSON.parse(document.getElementById("py_coord").value);
let py_lon = py_data.lon;
let py_lat = py_data.lat;
let rad = 0.02 * 400;
let marker = '380951792182'

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: py_lat, lng: py_lon},
        zoom: 8,
        draggableCursor:'crosshair'
    });
    map.addListener("click", (mapsMouseEvent) => {
        let coord = mapsMouseEvent.latLng.toJSON();
        loc_value = coord.lat.toString() + ", " + coord.lng.toString();
        console.log(loc_value);
        get_phone(coord.lat, coord.lng);
    });
    var marker = new google.maps.Marker({

        position: {lat: py_data.lat, lng: py_data.lon},

        map: map,

        title: '38050'
    });
    const phoneCircle = new google.maps.Circle({
        strokeColor: "#34a0d9",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#434eb5",
        fillOpacity: 0.35,
        map,
        center: {lat: py_data.lon, lng: 34.303407},
        radius: rad,
    });
}

function get_phone(lat, lon) {
    let request = new XMLHttpRequest();
    let url_addr = `http://127.0.0.1:5000/api/v1/get_phone?lat=${lat}&lon=${lon}`;
    console.log(url_addr);
    request.open('GET', url_addr, true);
    request.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            console.log('success')
            let resp = this.response;
            jresp = JSON.parse(resp)
            document.getElementById("phone_field").value = jresp.Phone;

            console.log(jresp);
        } else {
            // We reached our target server, but it returned an error
            console.log("We reached our target server, but it returned an error")
        }
    };
    request.onerror = function () {
        // There was a connection error of some sort
        console.log("There was a connection error of some sort")
    };
    request.send();
}