async function newuser(user, icao) {
  const response = await fetch('http://127.0.0.1:4320/signup/' + user + '/' + icao);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function newone(event) {
  event.preventDefault();
  poista();
  const icao = document.getElementById('icao').value;
  const user = document.getElementById('user').value;
  const username = await newuser(user);
  const hasbulla = username.old
  const airport = await newuser(user, icao);
  const khabib = airport.icao
  if (hasbulla) {
      alert('Username already taken!');
  }
  else if (khabib) {
    alert('Incorrect ICAO-Code!');
  }
  else {
     window.location.href = 'http://localhost:63342/ClearSkies_game/HTML/dashboard.html?';
     localStorage.setItem('textvalue', user);
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