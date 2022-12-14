async function first(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/first/' + username);
}

async function second(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/second/' + username);
}

async function third(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/third/' + username);
}

async function fourth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/fourth/' + username);
}

async function fifth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/fifth/' + username);
}

async function sixth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:1029/sixth/' + username);
}