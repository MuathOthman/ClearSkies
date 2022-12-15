async function wallet(name) {
  const response = await fetch('http://127.0.0.1:1029/wallet/' + name);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data)
  return data;
}
async function main() {
  const name = localStorage.getItem("textvalue");
  const budget = await wallet(name);
  document.querySelector('#balance').innerHTML = JSON.stringify(budget.money) + '$';
}

main();