const button = document.querySelector('.button')
let rank = 1

fetch('http://127.0.0.1:3090/leaderboard/')
.then(function(response) {
  return response.json()
})
.then(function(data) {
  let placeholder = document.querySelector("#data-output");
  let out = "";
  for (let m of data) {
    out += `
             <tr>
               <td>${rank}</td>
               <td>${m.name}</td>
               <td>${m.coconsumed}</td>
               <td>${m.weathercard}</td>
             </tr>
            `;
    rank+=1
  }
  console.log(out)

    placeholder.innerHTML = out;
  })





