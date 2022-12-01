async function money_to_co2(username) {
  const response = await fetch('http://127.0.0.1:4005/transfer/' + username);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function transfer() {
  const username = document.getElementById('username').value;
  const loguser = await money_to_co2(username);
  if (username === loguser.correct) {
    alert('Login success!');
    return false;
  } else {
    alert('Login failed!');
    console.log(loguser);
  }
}