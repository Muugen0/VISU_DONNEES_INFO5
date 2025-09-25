function parseCGPA(str) {
  if(!str) return null;
  const raw = str.replace(/\s/g,''); // supprime tous les espaces
  const mapping = { "0-1.99":0, "2.00-2.49":2, "2.50-2.99":2.5, "3.00-3.49":3, "3.50-4.00":4 };
  return mapping[raw] ?? null;
}

// Update radar chart
function updateChart() {
  const filtered = filterData();
  const noData = filtered.length === 0;
  d3.select("#noDataMsg").style("display", noData ? "block" : "none");
  d3.select("#chart").selectAll("*").remove();
  //if(noData) return;

  const averages = [
    d3.mean(filtered, d => d.depression),
    d3.mean(filtered, d => d.anxiety),
    d3.mean(filtered, d => d.panic)
  ];

  const width = document.getElementById("chart").clientWidth;
  const height = document.getElementById("chart").clientHeight;
  let radius = Math.min(width, height)/2 - 50;
  radius = Math.max(radius, 100);
  const angleSlice = (2*Math.PI)/radarAxes.length;

  const svg = d3.select("#chart").append("svg")
    .attr("width", width).attr("height", height)
    .append("g").attr("transform", `translate(${width/2},${height/2})`);

  const rScale = d3.scaleLinear().domain([0,1]).range([0,radius]);

  // Grid
  for(let level=1; level<=5; level++){
    svg.append("circle").attr("r", radius/5*level).attr("fill","none").attr("stroke","#CDCDCD").attr("stroke-dasharray","2,2");
  }

  // Axes
  radarAxes.forEach((axis,i)=>{
    const angle = i*angleSlice - Math.PI/2;
    const x = rScale(1)*Math.cos(angle);
    const y = rScale(1)*Math.sin(angle);
    svg.append("line").attr("x1",0).attr("y1",0).attr("x2",x).attr("y2",y).attr("stroke","#888");
    svg.append("text").attr("x",x*1.1).attr("y",y*1.1).attr("text-anchor","middle").attr("alignment-baseline","middle").text(axis);
  });

  // Polygon
  const line = d3.lineRadial().radius(d=>rScale(d)).angle((d,i)=>i*angleSlice).curve(d3.curveLinearClosed);
  svg.append("path").datum(averages).attr("d",line).attr("fill","rgba(0,123,255,0.3)").attr("stroke","#007bff").attr("stroke-width",2);

  // Points + tooltip
  const tooltip = d3.select("body").append("div").attr("class","tooltip");
  svg.selectAll(".point").data(averages).enter().append("circle")
    .attr("cx",(d,i)=>rScale(d)*Math.cos(i*angleSlice - Math.PI/2))
    .attr("cy",(d,i)=>rScale(d)*Math.sin(i*angleSlice - Math.PI/2))
    .attr("r",5).attr("fill","#007bff")
    .on("mouseover", (event,d,i)=>{ tooltip.style("opacity",1).html(`${radarAxes[i]}: ${d.toFixed(2)}`); })
    .on("mousemove", event=>{ tooltip.style("left",(event.pageX+10)+"px").style("top",(event.pageY-10)+"px"); })
    .on("mouseout", ()=>{ tooltip.style("opacity",0); });
}

// Radar chart axes
const radarAxes = ["Dépression", "Anxiété", "Crise de panique"];
let dataGlobal = [];

// Load CSV
d3.csv("http://localhost:8000/VISU_DONNEES_INFO5/TP1/dataset/Student_Mental_health.csv").then(data => {
  dataGlobal = data.map(d => ({
    gender: d["Choose your gender"]?.toLowerCase(),
    year: d["Your current year of Study"]?.toLowerCase(),
    marital: d["Marital status"]?.toLowerCase(),
    age: d.Age ? +d.Age : null,
    cgpa: parseCGPA(d["What is your CGPA?"]),
    depression: d["Do you have Depression?"]?.toLowerCase() === "yes" ? 1 : 0,
    anxiety: d["Do you have Anxiety?"]?.toLowerCase() === "yes" ? 1 : 0,
    panic: d["Do you have Panic attack?"]?.toLowerCase() === "yes" ? 1 : 0
  }));

  initSliders();
  setTimeout(updateChart, 0);

}).catch(err => {
  console.error("Failed to load CSV:", err);
  d3.select("#noDataMsg").text("Failed to load data").style("display", "block");
});

// Initialize dual-handle sliders
function initSliders(){
  // Age slider
  noUiSlider.create(document.getElementById('ageSlider'), {
    start: [18, 24],
    connect: true,
    step: 1,
    range: { min: 18, max: 24 },
    tooltips: [true,true],
    format: { to: v => parseInt(v), from: v => parseInt(v) }
  });

  const ageSlider = document.getElementById('ageSlider').noUiSlider;

  ageSlider.on('update', function(values){
    document.getElementById('ageMinVal').textContent = values[0];
    document.getElementById('ageMaxVal').textContent = values[1];
    updateChart();
  });

  // CGPA slider
  noUiSlider.create(document.getElementById('cgpaSlider'), {
    start: [0, 4],
    connect: true,
    step: 0.5,
    range: { min: 0, max: 4 },
    tooltips: [true,true],
    pips: { mode: 'values', values: [0,2,2.5,3,4], density: 100 },
    format: { to: v => parseFloat(v), from: v => parseFloat(v) }
  });

  const cgpaSlider = document.getElementById('cgpaSlider').noUiSlider;

  cgpaSlider.on('update', function(values){
    document.getElementById('cgpaMinVal').textContent = values[0];
    document.getElementById('cgpaMaxVal').textContent = values[1];
    updateChart();
  });

  // Checkbox events
  document.querySelectorAll(".gender, .year, .marital").forEach(el => el.addEventListener("change", updateChart));
}

// Get filter values
function getFilters() {
  const genders = Array.from(document.querySelectorAll(".gender:checked")).map(d => d.value);
  const years = Array.from(document.querySelectorAll(".year:checked")).map(d => d.value);
  const marital = Array.from(document.querySelectorAll(".marital:checked")).map(d => d.value);

  const ageSliderEl = document.getElementById('ageSlider');
  const cgpaSliderEl = document.getElementById('cgpaSlider');

  const ageSlider = ageSliderEl?.noUiSlider?.get().map(Number) ?? [18,24];
  const cgpaSlider = cgpaSliderEl?.noUiSlider?.get().map(Number) ?? [0,4];

  return {
    genders, years, marital,
    ageMin: ageSlider[0], ageMax: ageSlider[1],
    cgpaMin: cgpaSlider[0], cgpaMax: cgpaSlider[1]
  };
}

// Filter data
function filterData() {
  const f = getFilters();
  return dataGlobal.filter(d => {
    if(d.age === null || d.cgpa === null) return false;
    const genderMatch = f.genders.length ? f.genders.includes(d.gender) : true;
    const yearMatch = f.years.length ? f.years.includes(d.year) : true;
    const maritalMatch = f.marital.length ? f.marital.includes(d.marital) : true;
    const ageMatch = d.age >= f.ageMin && d.age <= f.ageMax;
    const cgpaMatch = d.cgpa >= f.cgpaMin && d.cgpa <= f.cgpaMax;
    return genderMatch && yearMatch && maritalMatch && ageMatch && cgpaMatch;
  });
}
