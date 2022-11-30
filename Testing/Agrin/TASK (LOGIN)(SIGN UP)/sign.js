async function newuser(user) {
  const response = await fetch('http://127.0.0.1:5000/signup/' + user);
  console.log('response', response);
  const data = await response.json();
  console.log('data', data);
  return data;
}

async function newone() {
  const user = document.getElementById('user').value;
  const username = await newuser(user);
  const hasbulla = username.old
  if (hasbulla) {
    alert('Username already taken!');
  } else {
    alert('Welcome to ClearSkies!');
  }
}