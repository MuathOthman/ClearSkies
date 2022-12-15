async function getAirportData(nimi){
  const response = await fetch('http://127.0.0.1:1029/location/'+ nimi);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  return data
}

function renderHTML(data) {
  const map = L.map('map').setView([data['Latitude'], data['Longitude']], 5);
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
    var singleMarker = L.marker([data['Latitude'], data['Longitude']]);
    console.log(singleMarker)
    singleMarker.addTo(map);
}

async function main() {
  let name = localStorage.getItem("textvalue");
  const locationData = await getAirportData(name);
  console.log('Location data:', locationData);
  renderHTML(locationData);
}


setTimeout(main, 100)