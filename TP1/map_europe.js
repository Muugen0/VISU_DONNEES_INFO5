// Base config (shared constants)
const baseConfig = {
  title: 'Self-reported consultation of mental healthcare for 15-24 year olds',
  width: 1080,
  legend: { x: 10, y: 200, title: 'Percentage of consultations, %', boxOpacity: 0 },
  numberOfClasses: 8,
  colors: ['#FFEBE6','#FFD0C2','#FFB39A','#FF8A6E','#F25A3F','#D93B2A','#B72117','#8B0001'],
  nutsLevel: 0,
  eurostatDatasetCode: 'hlth_ehis_am6e',
  unitText: '%',
  isco08: 'OC2634_2212PSY',
  age: 'Y15-24',
  isced11: 'TOTAL'
};

// Function to (re)build the map given filter parameters
function buildMap(filters) {
  const svg = document.getElementById('map');
  // Clear old contents (so you don't overlay maps)
  while (svg.firstChild) {
    svg.removeChild(svg.firstChild);
  }

  const subtitle = filters.TIME || '';

  eurostatmap
    .map('choropleth')
    .title(baseConfig.title)
    .width(baseConfig.width)
    .subtitle(subtitle)
    .stat({
      eurostatDatasetCode: baseConfig.eurostatDatasetCode,
      unitText: baseConfig.unitText,
      filters: {
        TIME: filters.TIME,
        sex: filters.sex,
        isco08: baseConfig.isco08,
        isced11: filters.isced11,
        age: baseConfig.age
      }
    })
    .legend(baseConfig.legend)
    .numberOfClasses(baseConfig.numberOfClasses)
    .colors(baseConfig.colors)
    .nutsLevel(baseConfig.nutsLevel)
    .build();
}

// When DOM is ready, wire up UI and initial map
document.addEventListener('DOMContentLoaded', function () {
  const yearSelect = document.getElementById('yearSelect');
  const sexSelect = document.getElementById('sexSelect');
  const eduSelect = document.getElementById('eduSelect');
  const updateBtn = document.getElementById('updateBtn');

  // Initial build
  buildMap({
    TIME: yearSelect.value,
    sex: sexSelect.value,
    isced11: eduSelect.value
  });

  // Update on button click
  updateBtn.addEventListener('click', function() {
    buildMap({
      TIME: yearSelect.value,
      sex: sexSelect.value,
      isced11: eduSelect.value
    });
  });


});
