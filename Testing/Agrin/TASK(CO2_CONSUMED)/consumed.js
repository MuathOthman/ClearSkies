async function consumed(name) {
  const response = await fetch('http://127.0.0.1:4995/consumed/' + name);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data)
  return data;
}
async function main() {
  const name = prompt('Enter your name:');
  const co2 = await consumed(name);
  document.querySelector('#p').innerHTML = JSON.stringify(co2.consumed);
}
main();