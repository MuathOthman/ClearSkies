/* TEST CODE */
async function getAirportData(icao){
  const response = await fetch('http://127.0.0.1:1029/weather/'+ icao);
  console.log('response', response)
  const data = await response.json()
  console.log('Icao data', data);
  return data
}

function renderHTML(data) {
    const p = document.getElementById('degree');
    p.innerText = data['Temperature'] + '°C';
    const m = document.getElementById('desc');
    m.innerText = data['Description'];
}

async function main() {
  let icaoInput = localStorage.getItem("textvalue");
  const aiportData = await getAirportData(icaoInput);
  console.log('Airport data:', aiportData);
  renderHTML(aiportData);
}
  main()
