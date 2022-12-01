const lista = []

async function budget(){
  let name = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:3060/location/' + name);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  lista.push(data['Latitude'])
  lista.push(data['Longitude'])
  alert(lista[0])
  return data
}
budget()
alert(lista[0])

const map = L.map('map').setView([31.7226009369, 35.9931983948], 5);
const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright%22%3EOpenStreetMap</a> contributors'
}).addTo(map);

googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
   maxZoom: 20,
   subdomains:['mt0','mt1','mt2','mt3']
 });
googleSat.addTo(map);

/*===================================================
                      MARKER
===================================================*/

var singleMarker = L.marker([31.7226009369, 35.9931983948]);
console.log(singleMarker)
singleMarker.addTo(map);







