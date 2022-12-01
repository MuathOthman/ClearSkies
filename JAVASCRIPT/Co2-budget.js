async function budget(name){
  const response = await fetch('http://127.0.0.1:5000/co2_budget/' + name);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  return data
}

function renderHTML(data) {
    const p = document.getElementById('consumed-balance');
    p.innerText = data['co2_budget'] + ' kg';
}

async function main() {
  let icaoInput = localStorage.getItem("textvalue");
  console.log(icaoInput)
  const aiportData = await budget(icaoInput);
  console.log('Ariport data:', aiportData);
  renderHTML(aiportData);
}
  main()
  console.log('Ohjelma jatkuu');