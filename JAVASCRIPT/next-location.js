const latlangs = []
const id = []
var map = L.map('map').setView([60.1699,24.9384], 14);
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
 });
 googleStreets.addTo(map);

 // Satelite Layer
googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
   maxZoom: 20,
   subdomains:['mt0','mt1','mt2','mt3']
 });
googleSat.addTo(map);
/*===================================================
                      DATA
===================================================*/

async function getAirportData(nimi){
  const response = await fetch('http://127.0.0.1:1029/location/'+ nimi);
  console.log('response', response)
  const data = await response.json()
  console.log('data', data);
  return data
}

async function main() {
  let name = localStorage.getItem("textvalue");
  const locationData = await getAirportData(name);
  console.log('Location data:', locationData);
  renderHTML(locationData);
}

function renderHTML(data) {
/*===================================================
                  Location-Marker
===================================================*/
    var singleMarker = L.marker([data['Latitude'], data['Longitude']]);
    map.panTo(new L.LatLng(data['Latitude'], data['Longitude']));
    console.log(singleMarker)
    singleMarker.addTo(map);
    latlangs.push(singleMarker.getLatLng());
}

main()


/*===================================================
                      Next-location
===================================================*/
const button = document.querySelector('.button')

button.addEventListener('click', secondICAO)

async function secondICAO() {
  let name = localStorage.getItem("textvalue");
  let icao = document.getElementById("search").value
  console.log(icao)
  const response = await fetch('http://127.0.0.1:1029/nextlocation?nimi='+ name + '&icao=' + icao);
  console.log('response', response)
  const icao_data = await response.json()
  console.log('data', icao_data);
  const singleMarker1 = L.marker([icao_data['Latitude'], icao_data['Longitude']]);
  console.log(singleMarker1)
  singleMarker1.addTo(map);
  latlangs.push(singleMarker1.getLatLng());
  var polyline = L.polyline(latlangs, {color: 'red'}).addTo(map);
  // zoom the map to the polyline
  map.fitBounds(polyline.getBounds());
  const database = await fetch('http://127.0.0.1:1029/weathercard?nimi='+ name + '&icao=' + icao);
  setTimeout(budgetMain, 90)
  setTimeout(weatherMain, 120)
  setTimeout(budgetMainWin, 140)
}

Iflocal()


async function budget(nimi){
  const response = await fetch('http://127.0.0.1:1029/budget/'+ nimi);
  console.log('response', response)
  const dataC02 = await response.json()
  console.log('data', dataC02);
  return dataC02
}


function budgetC02(dataC02) {
    if (dataC02['co2consumed'] > dataC02['co2budget']){
      popup()
    } else {
      /*alert('Jatka')*/
    }
}


async function budgetMain(){
  let nimi = localStorage.getItem("textvalue");
  const data = await budget(nimi)
  budgetC02(data);
}

function popup(){
  var blur = document.getElementById('blur');
  blur.classList.toggle('active');
  var blur = document.getElementById('popup');
  blur.classList.toggle('active')
}


async function restart(){
  let name = localStorage.getItem("textvalue");
  const restart = await fetch('http://127.0.0.1:1029/restart/' + name);
  window.location.href="http://localhost:63342/ClearSkies_H-ryhm%C3%A4/HTML/dashboard.html#";
  localStorage.removeItem('thunderstrom')
  localStorage.removeItem('drizzle')
  localStorage.removeItem('rain')
  localStorage.removeItem('snow')
  localStorage.removeItem('clouds')
  localStorage.removeItem('haze')
  localStorage.removeItem('clear')

}

/*===================================================
                   Weather Card
===================================================*/
async function weather(nimi){
  const response = await fetch('http://127.0.0.1:1029/saa/'+ nimi);
  console.log('response', response)
  const weather = await response.json()
  console.log('data', weather);
  return weather
}


function weatherIF(weather) {
    if (weather['saa'] == 10){
      localStorage.setItem("thunderstrom", 10)
    } if (weather['saa'] == 19) {
        document.documentElement.style.setProperty('--color-drizzle', '#7380ec');
        localStorage.setItem("drizzle", 19)
    } if (weather['saa'] == 29) {
        document.documentElement.style.setProperty('--color-rain', '#7380ec');
        localStorage.setItem('rain', 29)
    } if (weather['saa'] == 40) {
        document.documentElement.style.setProperty('--color-snow', '#7380ec');
        localStorage.setItem('snow', 40)
    } if (weather['saa'] == 44) {
        document.documentElement.style.setProperty('--color-clouds', '#7380ec');
        localStorage.setItem('clouds', 44)
    } if (weather['saa'] == 48) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 46) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 47) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 49) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 50) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 51) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 52) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 54) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 55) {
        document.documentElement.style.setProperty('--color-haze', '#7380ec');
        localStorage.setItem('haze', 48)
    } if (weather['saa'] == 45) {
        document.documentElement.style.setProperty('--color-clear', '#7380ec');
        localStorage.setItem('clear', 45)
    }
}

async function weatherMain(){
  let nimi = localStorage.getItem("textvalue");
  const data = await weather(nimi)
  console.log(data)
  weatherIF(data);
}

function Iflocal(){
  if (localStorage.getItem('thunderstrom') == 10){
    document.documentElement.style.setProperty('--color-thunderstrom', '#7380ec');
  } if (localStorage.getItem('thunderstrom') == 19){
    document.documentElement.style.setProperty('--color-drizzle', '#7380ec');
  } if (localStorage.getItem('rain') == 29){
    document.documentElement.style.setProperty('--color-rain', '#7380ec');
  } if (localStorage.getItem('snow') == 40){
    document.documentElement.style.setProperty('--color-snow', '#7380ec');
  } if (localStorage.getItem('clouds') == 44){
    document.documentElement.style.setProperty('--color-clouds', '#7380ec');
  } if (localStorage.getItem('haze') == 46){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 47){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 48){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 49){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 50){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 51){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 52){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 53){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 54){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('haze') == 55){
    document.documentElement.style.setProperty('--color-haze', '#7380ec');
  } if (localStorage.getItem('clear') == 45){
    document.documentElement.style.setProperty('--color-clear', '#7380ec');
  }
}


function poista(){
  localStorage.removeItem('thunderstrom')
  localStorage.removeItem('drizzle')
  localStorage.removeItem('rain')
  localStorage.removeItem('snow')
  localStorage.removeItem('clouds')
  localStorage.removeItem('haze')
  localStorage.removeItem('clear')
}

async function saaWin(nimi){
  const response = await fetch('http://127.0.0.1:1029/winner/' + nimi);
  console.log('response', response)
  const saa = await response.json()
  console.log('data', saa);
  return saa
}

function budgetC02Win(saa) {
    if (saa['tila'] == 4){
      popupWin()
    } else {
      /alert('Hävisit')/
    }
}


async function budgetMainWin(){
  let nimi = localStorage.getItem("textvalue");
  const data = await saaWin(nimi)
  budgetC02Win(data);
}

function popupWin(){
  var blur = document.getElementById('blur');
  blur.classList.toggle('active');
  var blur = document.getElementById('popup-win');
  blur.classList.toggle('active')
}