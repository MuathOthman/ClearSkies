async function olduser(username) {
  const response = await fetch('http://127.0.0.1:3010/login/' + username);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function validate(event) {
  event.preventDefault()
  poista()
  const username = document.getElementById('username').value;
  const loguser = await olduser(username);
  if (username === loguser.correct) {
    window.location.href="http://localhost:63342/ClearSkies_H-ryhm%C3%A4/HTML/dashboard.html?_ijt=5rm6h00jei6cjs1m6mo0e0g7in&_ij_reload=RELOAD_ON_SAVE";
    localStorage.setItem("textvalue", username)
    return false;
  } else {
    alert('Login failed!');
    console.log(loguser);
  }
}
document.querySelector('#login').addEventListener('submit', validate)


function poista(){
  localStorage.removeItem('thunderstrom')
  localStorage.removeItem('drizzle')
  localStorage.removeItem('rain')
  localStorage.removeItem('snow')
  localStorage.removeItem('clouds')
  localStorage.removeItem('haze')
  localStorage.removeItem('clear')
}
