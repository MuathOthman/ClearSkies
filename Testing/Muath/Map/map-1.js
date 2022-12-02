const lista = []
let array = lista.map(Number)

async function budget(){
  let name = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:3060/location/' + name);
  console.log('response', response)
  const data = await parseFloat(response.json())
  console.log('data', data);
  lista.push(data['Latitude'])
  lista.push(data['Longitude'])
  return data
}
budget()
gameSetup()

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
async function gameSetup(){

    let name = localStorage.getItem("textvalue");
    let muath = await fetch('http://127.0.0.1:3060/location/' + name);
    console.log(muath.Latitude)

    for (let airport of muath){
      var singleMarker = L.marker([airport.Latitude, airport.Longitude]);
      console.log(singleMarker)
      singleMarker.addTo(map);
      }
  }