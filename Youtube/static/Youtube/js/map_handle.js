function initMap() {
    const myLatlng = {lat: 50.44, lng: 30.46};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: myLatlng,
        draggableCursor:'crosshair'
    });
    map.addListener("click", (mapsMouseEvent) => {
        //let coord = JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2);
        let coord = mapsMouseEvent.latLng.toJSON();
        loc_value = coord.lat.toString() + ", " + coord.lng.toString()
        document.getElementById("id_location").value = loc_value;
        document.getElementById("id_location_radius").value = 10;
    });
}