async function first(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4099/co2_budget/' + username);
}

async function second(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4029/co2_budget/' + username);
}

async function third(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4039/co2_budget/' + username);
}

async function fourth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4049/co2_budget/' + username);
}

async function fifth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4059/co2_budget/' + username);
}

async function sixth(){
  const username = localStorage.getItem("textvalue");
  const response = await fetch('http://127.0.0.1:4069/co2_budget/' + username);
}