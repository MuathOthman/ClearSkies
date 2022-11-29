async function getAirportData(icao){
  const response = await fetch('http://127.0.0.1:4000/saa/'+ icao);
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
  let icaoInput = prompt('Mikä kenttä (ICAO)?');
  const aiportData = await getAirportData(icaoInput);
  console.log('Ariport data:', aiportData);
  renderHTML(aiportData);
}
  main()
  console.log('Ohjelma jatkuu');



/*target.append(p)
    console.log('results', data)
    p.innerText += data['Temperature'];
    target.append(p)
    console.log('results', data)
    #run
  }*/