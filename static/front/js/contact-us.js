function loadMap() {
    let map = new AMap.Map('map');
    let position = [114.805750, 37.294399];
    map.setCenter(position);

    let marker = new AMap.Marker({
        position: position
    });
    map.add(marker);
    map.setZoom(16);
}

window.onload = loadMap;
