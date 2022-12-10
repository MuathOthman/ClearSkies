document.getElementById('namehtml').innerHTML=localStorage.getItem("textvalue");
const button = document.querySelector('.button')

button.addEventListener('click', function(){
  let country = document.getElementById("search").value
  console.log(country)
  fetch('http://127.0.0.1:3080/kentta/'+ country)
  .then(function(response) {
    return response.json()
  })
  .then(function(data) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for (let m of data) {
        out += `
              <tr>
                <td>${m.name}</td>
                <td className="warning">${m.icao}</td>
              </tr>
            `;
    }
  console.log(out)

    placeholder.innerHTML = out;
  })
})




