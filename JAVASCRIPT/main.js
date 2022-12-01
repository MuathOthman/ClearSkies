document.getElementById('namehtml').innerHTML=localStorage.getItem("textvalue");


async function getAirportData(icao){
  const response = await fetch('http://127.0.0.1:3040/saa/'+ icao);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
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
  console.log('Ariport data:', aiportData);
  renderHTML(aiportData);
}
  main()


async function budget(name){
  const response = await fetch('http://127.0.0.1:3000/co2_budget/' + name);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  return data
}

function renderHTML1(data) {
    const p = document.getElementById('consumed-balance');
    p.innerText = data['co2_budget'] + ' kg';
}

async function main1() {
  let icaoInput = localStorage.getItem("textvalue");
  console.log(icaoInput)
  const aiportData = await budget(icaoInput);
  console.log('Ariport data:', aiportData);
  renderHTML1(aiportData);
}
  main1()
  console.log('Ohjelma jatkuu');
