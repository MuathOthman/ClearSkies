let icao = prompt('Give ICAO')

  fetch('http://127.0.0.1:3000/kentta/'+ icao)
  .then(function(response) {
    return response.json()
  })
  .then(function(data) {
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for (let m of data) {
        out += `
              <tr>
                <td>'${m.name}'</td>
                <td className="warning">'${m.icao}'</td>
              </tr>
            `;
    }
  console.log(out)
    placeholder.innerHTML = out;
  })





