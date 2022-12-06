const latlangs = []
var map = L.map('map').setView([60.1699,24.9384], 14);
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
 });
 googleStreets.addTo(map);

 // Satelite Layer
googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
   maxZoom: 20,
   subdomains:['mt0','mt1','mt2','mt3']
 });
googleSat.addTo(map);
/*===================================================
                      DATA
===================================================*/

async function getAirportData(nimi){
  const response = await fetch('http://127.0.0.1:3060/location/'+ nimi);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  return data
}

async function main() {
  let name = localStorage.getItem("textvalue");
  const locationData = await getAirportData(name);
  console.log('Location data:', locationData);
  renderHTML(locationData);
}

function renderHTML(data) {
/*===================================================
                  Location-Marker
===================================================*/
    var singleMarker = L.marker([data['Latitude'], data['Longitude']]);
    map.panTo(new L.LatLng(data['Latitude'], data['Longitude']));
    console.log(singleMarker)
    singleMarker.addTo(map);
    latlangs.push(singleMarker.getLatLng());
}

main()


/*===================================================
                      Next-location
===================================================*/
const button = document.querySelector('.button')

button.addEventListener('click', secondICAO)

async function secondICAO() {
  let name = localStorage.getItem("textvalue");
  let icao = document.getElementById("search").value
  console.log(icao)
  const response = await fetch('http://127.0.0.1:3070/location?nimi='+ name + '&icao=' + icao);
  console.log('response', response)
  const icao_data = await response.json()
  console.log('data', icao_data);
  const singleMarker1 = L.marker([icao_data['Latitude'], icao_data['Longitude']]);
  console.log(singleMarker1)
  singleMarker1.addTo(map);
  latlangs.push(singleMarker1.getLatLng());
  var polyline = L.polyline(latlangs, {color: 'red'}).addTo(map);
  // zoom the map to the polyline
  map.fitBounds(polyline.getBounds());
  const database = await fetch('http://127.0.0.1:3078/location?nimi='+ name + '&icao=' + icao);
  budgetMain()
}



async function budget(nimi){
  const response = await fetch('http://127.0.0.1:3099/co2_budget/'+ nimi);
  console.log('response', response)
  const dataC02 = await response.json()
  console.log('data', dataC02);
  return dataC02
}


function budgetC02(dataC02) {
    if (dataC02['co2consumed'] > dataC02['co2budget']){
      popup()
    } else {
      alert('Jatka')
    }
}


async function budgetMain(){
  let nimi = localStorage.getItem("textvalue");
  const data = await budget(nimi)
  budgetC02(data);
}

function popup(){
  var blur = document.getElementById('blur');
  blur.classList.toggle('active');
  var blur = document.getElementById('popup');
  blur.classList.toggle('active')
}


async function restart(){
  let name = localStorage.getItem("textvalue");
  const restart = await fetch('http://127.0.0.1:3033/sql/' + name);
  window.location.href="http://localhost:63342/ClearSkies_H-ryhm%C3%A4/HTML/dashboard.html#";
}