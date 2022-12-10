async function newuser(user, icao) {
  const response = await fetch('http://127.0.0.1:4320/signup?nimi=' + user +'&icao=' + icao);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  window.location.href="http://localhost:63342/ClearSkies_H-ryhm%C3%A4/HTML/dashboard.html#";
  return data;
}

async function newone() {
  const user = document.getElementById('user').value;
  const icao = document.getElementById('icao').value;
  const username = await newuser(user, icao);
}