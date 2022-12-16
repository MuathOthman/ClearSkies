document.getElementById('namehtml').innerHTML=localStorage.getItem("textvalue");
document.getElementById('name').innerHTML=localStorage.getItem("textvalue");
async function getAirportData(icao){
  const response = await fetch('http://127.0.0.1:1029/weather/'+ icao);
  console.log('response', response)
  const data = response.json()
  console.log('Weather data', data);
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




async function budget(name){
  const response = await fetch('http://127.0.0.1:1029/budget/' + name);
  console.log('response', response)
  const data = await response.json()
  console.log('Budget data', data);
  return data
}

function renderHTML1(data) {
    const p = document.getElementById('consumed-balance');
    p.innerText = data['co2consumed'] + ' kg/' +  '                ' + data['co2budget'] + ' kg';
}

async function main1() {
  let icaoInput = localStorage.getItem("textvalue");
  console.log(icaoInput)
  const aiportData = await budget(icaoInput);
  console.log('Data:', aiportData);
  renderHTML1(aiportData);
}


main()
setTimeout(main1, 80)