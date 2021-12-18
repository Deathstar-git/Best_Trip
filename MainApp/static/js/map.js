let map;
let map_wrap = document.querySelector('.map_wrap')
let map_background = document.querySelector('.map_background')
let lat_input = document.getElementById('place_lat')
let lng_input = document.getElementById('place_lng')
let map_input = document.getElementById('map_input')

function update_coordinate_inputs(lat, lng) {
    lat_input.value = lat;
    lng_input.value = lng;
}

function set_default_coordinate_inputs_values(location) {
    if (String(lat_input.value).length == 0) {
        lat_input.value = location.lat
        lng_input.value = location.lng
    }

    else {
        location.lat = parseFloat(String(lat_input.value).replace(',', '.'))
        location.lng = parseFloat(String(lng_input.value).replace(',', '.'))
        marker = new google.maps.Marker({
            position: location,
            map: map,
            draggable: false
        });
    }
}

function initMap() {

    let location = {
        lat: 57.01528339999999,
        lng: 92.8932476
    }

    let options = {
        center: location,
        zoom: 8,
        draggable: false,
    }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((loc) => {
            location.lat = loc.coords.latitude
            location.lng = loc.coords.longitude
        })
    }

    autocomplete = new google.maps.places.Autocomplete(map_input, {
        fields: ['geometry', 'name'],
        types: ['(cities)']
    })

    autocomplete.addListener("place_changed", () => {
        place = autocomplete.getPlace();
        let location = place.geometry.location
        new google.maps.Marker({
            map: map,
            position: location,
            title: place.name
        })

        let markerBounds = new google.maps.LatLngBounds()
        markerBounds.extend(location)
        map.fitBounds(markerBounds)
        map.setZoom(8)
        update_coordinate_inputs(location.lat(), location.lng())
    })

    setTimeout(() => {
        map = new google.maps.Map(document.getElementById("map"), options)
        set_default_coordinate_inputs_values(location)
        map.panTo(location)
        map_anim(map)
    }, 100)
}

function map_anim(map){
    let posts = document.querySelectorAll(".post_wrap")
    let marker = new google.maps.Marker({
        position: new google.maps.LatLng(0, 0),
        map: map,
        draggable: false
    });

    map_background.addEventListener("click", function () {
        map_wrap.classList.remove("map_wrap_visible")
        map_background.classList.remove("map_background_visible")
    })    

    if(posts){
        posts.forEach(post => {
            post_add_map_button = post.querySelector(".post_add_map_button")
            post_lat = post.querySelector("#post_lat").value
            post_lng = post.querySelector("#post_lng").value
            let post_location = {
                lat: parseFloat(String(post_lat).replace(',', '.')),
                lng: parseFloat(String(post_lng).replace(',', '.'))
            }
            post_add_map_button.addEventListener("click", function () {
                map_wrap.classList.add("map_wrap_visible")
                map_background.classList.add("map_background_visible")
                console.log(post_location)
                map.panTo(post_location)
                marker.setPosition(post_location)
            })
        })
    }
}