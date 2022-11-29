async function wallet(name) {
  const response = await fetch('http://127.0.0.1:5000/wallet/' + name);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data)
  return data;
}
async function main() {
  const name = prompt('Enter your name:');
  const budget = await wallet(name);
  document.querySelector('#p').innerHTML = name+ ' has ' + JSON.stringify(budget.money) + '$ in the wallet.';
}
main();