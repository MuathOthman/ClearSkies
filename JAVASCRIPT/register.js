async function newuser(user, icao) {
  const response = await fetch('http://127.0.0.1:4400/signup/' + user + '/' + icao);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function newone(event) {
  event.preventDefault();
  poista();
  const user = document.getElementById('user').value;
  const icao = document.getElementById('icao').value;
  const username = await newuser(user, icao);
  if (user === username.old) {
    alert('Username already taken!');
  } else {
    window.location.href = 'http://localhost:63342/ClearSkies_new/HTML/dashboard.html?_ijt=kaj6c5pe3pbm2pcqntibjj9h2u&_ij_reload=RELOAD_ON_SAVE';
    localStorage.setItem('textvalue', user);
    return false;
  }
}

document.querySelector('#signup').addEventListener('submit', newone);

function poista() {
  localStorage.removeItem('thunderstrom');
  localStorage.removeItem('drizzle');
  localStorage.removeItem('rain');
  localStorage.removeItem('snow');
  localStorage.removeItem('clouds');
  localStorage.removeItem('haze');
  localStorage.removeItem('clear');
}

