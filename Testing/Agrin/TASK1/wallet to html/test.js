async function getAirportData(name) {
  const response = await fetch('http://127.0.0.1:5000/wallet/' + name);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data)
  return data;
}
async function main() {
  const name = prompt('Enter your name:');
  // async funktio palauttaa promisen
  const airportData = await getAirportData(name);
  console.log('määrä', airportData);
  document.querySelector('#p').innerHTML = name+ ' has ' + JSON.stringify(airportData.money) + '$ in the wallet.';

}
main();