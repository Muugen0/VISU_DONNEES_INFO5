// set the dimensions and margins of the graph
const margin = {top: 40, right: 350, bottom: 60, left: 30},
    width = document.getElementById("bubble_plot").clientWidth - margin.left - margin.right,
    height = document.getElementById("bubble_plot").clientWidth / 2 - margin.top - margin.bottom - 50;

// append the svg object to the body of the page
const svg = d3.select("#bubble_plot")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

//Read the data
d3.csv("http://localhost:8000/TP1/dataset/MentalHealthDatasetMoyenne.csv").then(function(data) {

  // Add X axis
  const x = d3.scaleLinear()
    .domain([12, 18])
    .range([0, width]);
  svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x).ticks(15));

  // X axis label
  svg.append("text")
      .attr("text-anchor", "end")
      .attr("x", width)
      .attr("y", height + 50)
      .text("Depression level");

  // Add Y axis
  const y = d3.scaleLinear()
    .domain([8, 14])
    .range([height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Y axis label
  svg.append("text")
      .attr("x", 0)
      .attr("y", -20)
      .text("anxiety level")
      .attr("text-anchor", "start");

  // Scale for bubble size
  const z = d3.scaleLinear()
    .domain([0.8, 1.5])
    .range([2, 30]);

  // Scale for bubble color
  const myColor = d3.scaleLinear()
    .domain([5.0, 6.5])
    .range(["#fdc500","#780000"]);

  // Tooltip
  const tooltip = d3.select("#bubble_plot")
    .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "black")
      .style("border-radius", "5px")
      .style("padding", "10px")
      .style("color", "white");

  const showTooltip = function(event,d) {
    tooltip.transition().duration(200);
    tooltip.style("opacity", 1)
      .html("age: " + d.age + "--" + (parseInt(d.age)+3))
      .style("left", (event.x)/2 + "px")
      .style("top", (event.y)/2 - 50 + "px");
  }
  const moveTooltip = function(event,d) {
    tooltip.style("left", (event.x)/2 + "px")
           .style("top", (event.y)/2 - 50 + "px");
  }
  const hideTooltip = function(event,d) {
    tooltip.transition().duration(200).style("opacity", 0);
  }

  // Highlight group
  const highlight = function(event, d){
    d3.selectAll(".bubbles").style("opacity", .05);
    d3.selectAll("." + classSelector(d)).style("opacity", 1);
  }
  const noHighlight = function(event,d){
    d3.selectAll(".bubbles").style("opacity", 1);
  }

  function classSelector(value) {
    if (value < 5.15) return "type1";
    else if (value < 5.45) return "type2";
    else if (value < 5.75) return "type3";
    else if (value < 6.05) return "type4";
    else if (value < 6.35) return "type5";
    else return "type6";
  }

  // Add bubbles
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .join("circle")
      .attr("class", d => "bubbles " + classSelector(d.stress_level))
      .attr("id", d => d.gender)
      .attr("cx", d => x(d.depression_score))
      .attr("cy", d => y(d.anxiety_score))
      .attr("r", d => z(d.mental_health_risk))
      .style("fill", d => myColor(d.stress_level))
      .on("mouseover", showTooltip)
      .on("mousemove", moveTooltip)
      .on("mouseleave", hideTooltip);

  // ---------------------------//
  // Stress level legend (colors)
  const size = 20;
  const stressGroups = [5.0, 5.3, 5.6, 5.9, 6.3, 6.5];
  const legendX = width + 50;

  svg.selectAll("legendColor")
    .data(stressGroups)
    .join("circle")
      .attr("cx", legendX)
      .attr("cy", (d,i) => 20 + i*(size+5))
      .attr("r", 7)
      .style("fill", d => myColor(d))
      .on("mouseover", highlight)
      .on("mouseleave", noHighlight);

  svg.selectAll("legendColorLabels")
    .data(stressGroups)
    .enter()
    .append("text")
      .attr("x", legendX + size * 0.8)
      .attr("y", (d,i) => 10 + i * (size + 5) + (size/1.3))
      .style("fill", d => myColor(d))
      .text(d => d)
      .attr("text-anchor", "left")
      .style("alignment-baseline", "middle")
      .on("mouseover", highlight)
      .on("mouseleave", noHighlight);

  svg.append("text")
      .attr('x', legendX)
      .attr("y", 0)
      .text("Stress level")
      .attr("text-anchor", "left");

  // ---------------------------//
  // Mental health risk legend (sizes)
  const valuesToShow = [0.8, 1.15, 1.5];
  const legendSizeX = width + 50;
  const legendSizeY = height - 100;

  // Circles
  svg.selectAll("legendSizeCircles")
    .data(valuesToShow)
    .join("circle")
      .attr("cx", legendSizeX + 25)
      .attr("cy", d => legendSizeY - z(d) + 100)
      .attr("r", d => z(d))
      .style("fill", "none")
      .attr("stroke", "black");

  // Lines
  svg.selectAll("legendSizeLines")
    .data(valuesToShow)
    .join("line")
      .attr('x1', d => legendSizeX + z(d) + 25)
      .attr('x2', legendSizeX + 75)
      .attr('y1', d => legendSizeY - z(d) + 100)
      .attr('y2', d => legendSizeY - z(d) + 100)
      .attr('stroke', 'black')
      .style('stroke-dasharray', '2,2');

  // Labels
  function labelCirc(val) {
    if (val == 0.8) return "Low";
    else if (val == 1.15) return "Medium";
    return "High";
  }

  svg.selectAll("legendSizeLabels")
    .data(valuesToShow)
    .join("text")
      .attr('x', legendSizeX + 75)
      .attr('y', d => legendSizeY - z(d) + 100)
      .text(d => labelCirc(d))
      .style("font-size", 10)
      .attr('alignment-baseline', 'middle');

  // Legend title
  svg.append("text")
      .attr('x', legendSizeX + 50)
      .attr("y", legendSizeY + 120)
      .text("mental health risk")
      .attr("text-anchor", "middle");

});

// ---------------------------//
// Filter by gender radio buttons
function radioValueToGenre(val){
  switch (val) {
    case '0' : return "Male";
    case '1' : return "Female";
    case '2' : return "Non-binary";
    case '3' : return "PreferNotToSay";
    default : return "All";
  }
}

d3.selectAll("input[name='genre']").on("change", function() {
  const val = radioValueToGenre(this.value);
  d3.selectAll(".bubbles").style("display", "block");
  if (val != "All") {
    d3.selectAll(".bubbles").style("display", "none");
    d3.selectAll("#"+val).style("display", "block");
  }
});

