async function olduser(username) {
  const response = await fetch('http://127.0.0.1:5998/login/' + username);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function validate() {
  const username = document.getElementById('username').value;
  const loguser = await olduser(username);
  if (username === loguser.correct) {
    alert('Login success!');
    return false;
  } else {
    alert('Login failed!');
    console.log(loguser);
  }
}

