const map = L.map('map');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {

  // Specify the maximum zoom of the map
  maxZoom: 19,

  // Set the attribution for OpenStreetMaps
  attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Set the view of the map
// with the latitude, longitude and the zoom value
map.setView([48.8584, 2.2945], 16);