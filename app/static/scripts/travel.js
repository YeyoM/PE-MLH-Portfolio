// Loader to create SVG path for the orbs to travel along
window.onload = () => {
  const reductionRatio = 100;
  const map = $('#map');
  const mapHeight = map.height() - reductionRatio;
  const mapWidth = map.width() - reductionRatio;

  $('.orb').css('offsetPath', `path("M ${reductionRatio},${reductionRatio} L ${mapWidth}, ${reductionRatio} L ${mapWidth},${mapHeight} L ${reductionRatio},${mapHeight} Z")`);


  setTimeout(() => {
    $('.blue-orb').css('animationPlayState', 'running');
    $('.blue-orb').css('animationDelay', '-6s');
    $('.blue-orb.top-orb').css('animationPlayState', 'running');
    $('.blue-orb.top-orb').css('animationDelay', '-10s !important');
    $('.purple-orb').css('animationPlayState', 'running');
    $('.purple-orb').css('animationDelay', '-6s !important');
  }, 3000);
};

function loadMap() {
  // Edit this list according to the places you visited

  //20.700273069391454, -103.34686439076253
  const visitedPlaces = [
    {
      latitude: 33.813206842511214,
      longitude: -117.91900083374378,
      label: "School Trip 2015",
      tooltip: `I visited Los Angeles in 2015 for a school trip`
    },
    {
      latitude: 32.764278090368684,
      longitude: -117.22607178479097,
      label: "San Diego 2015",
      tooltip: `I visited San Diego in 2015 for a school trip`
    },
    {
      latitude: 20.631605818236892,
      longitude: -105.23049927911595,
      label: "Puerto Vallarta",
      tooltip: `Favorite place to spend vacations`
    },
    {
      latitude: 23.196239521549412,
      longitude: -106.42623537710914,
      label: "Mazatlan",
      tooltip: `I visited Mazatlan in 2019`
    },
    {
      latitude: 19.043465661470957,
      longitude: -98.19784667129454,
      label: "Puebla",
      tooltip: `I visited Puebla in 2017`
    },
    {
      latitude: 20.709350515038704,
      longitude: -100.44561623034305,
      label: "Queretaro",
      tooltip: `I went to a basketball tournament in Queretaro in 2020`
    },
    {
      latitude: 20.700273069391454,
      longitude: -103.34686439076253,
      label: "Guadalajara",
      tooltip: `I went to a basketball tournament in Guadalajara in 2020`
    }
  ]
  
  Mapkick.options = {
    style:'../static/mapStyles/dark_theme.json', 
    zoom: 3.6, 
    center: [-100, 28],
    tooltips: {html: true, hover: false},
    markers: {color: "#f84d4d"},
    label: {color: "#f84d4d"},
    textColor: "#f84d4d",
    controls: true
  };

  new Mapkick.Map("map", visitedPlaces);
}