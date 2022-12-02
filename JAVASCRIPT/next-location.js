var map = L.map('map').setView([40.7128,-74.0060], 4);
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
    console.log(singleMarker)
    singleMarker.addTo(map);

    map = L.map('map').setView([data['Latitude'], data['Longitude']], 4);

}

main()


/*===================================================
                      Next-location
===================================================*/
const button = document.querySelector('.button')

button.addEventListener('click', secondICAO)

async function secondICAO() {
  let icao = document.getElementById("search").value
  console.log(icao)
  const response = await fetch('http://127.0.0.1:3070/location/'+ icao);
  console.log('response', response)
  const icao_data = await response.json()
  console.log('data', icao_data);
  var singleMarker1 = L.marker([icao_data['Latitude'], icao_data['Longitude']]);
  console.log(singleMarker1)
  singleMarker1.addTo(map);

}




