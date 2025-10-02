// set the dimensions and margins of the graph
const margin = {top: 40, right: 200, bottom: 60, left: 30},
    width = document.getElementById("bubble_plot").clientWidth - margin.left - margin.right,
    height = document.getElementById("bubble_plot").clientWidth/2 - margin.top - margin.bottom - 50;

//console.log(width, height);

// append the svg object to the body of the page
const svg = d3.select("#bubble_plot")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

//Read the data
d3.csv("http://localhost:8000/TP1/dataset/MentalHealthDatasetMoyenne.csv").then( function(data) {

  // Add X axis
  const x = d3.scaleLinear()
    .domain([12, 18])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x).ticks(15));

  // Add X axis label:
  svg.append("text")
      .attr("text-anchor", "end")
      .attr("x", width)
      .attr("y", height+50 )
      .text("Depression level");

  // Add Y axis
  const y = d3.scaleLinear()
    .domain([8, 14])
    .range([ height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Add Y axis label:
  svg.append("text")
      .attr("text-anchor", "end")
      .attr("x", 0)
      .attr("y", -20 )
      .text("anxiety level")
      .attr("text-anchor", "start")

  // Add a scale for bubble size
  const z = d3.scaleLinear()
    .domain([0.8, 1.5])
    .range([2, 30]);

  // Add a scale for bubble color
  //const myColor = console.log;
  const myColor = d3.scaleLinear()
    .domain([5.0, 6.5])
    .range(["#fdc500","#780000"]);
	  
	


  // -1- Create a tooltip div that is hidden by default:
  const tooltip = d3.select("#bubble_plot")
    .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "black")
      .style("border-radius", "5px")
      .style("padding", "10px")
      .style("color", "white")

  // -2- Create 3 functions to show / update (when mouse move but stay on same circle) / hide the tooltip
  const showTooltip = function(event,d) {
    tooltip
      .transition()
      .duration(200)
    tooltip
      .style("opacity", 1)
      .html("age: " + d.age + "--" + String(parseInt(d.age)+3))
      .style("left", (event.x)/2 + "px")
      .style("top", (event.y)/2-50 + "px")
  }
  const moveTooltip = function(event, d) {
    tooltip
      .style("left", (event.x)/2 + "px")
      .style("top", (event.y)/2-50 + "px")
  }
  const hideTooltip = function(event, d) {
    tooltip
      .transition()
      .duration(200)
      .style("opacity", 0)
  }


  // ---------------------------//
  //       HIGHLIGHT GROUP      //
  // ---------------------------//

  // What to do when one group is hovered
  const highlight = function(event, d){
    // reduce opacity of all groups
    d3.selectAll(".bubbles").style("opacity", .05)
    // expect the one that is hovered
    d3.selectAll("."+classSelector(d)).style("opacity", 1)
  }

  // And when it is not hovered anymore
  const noHighlight = function(event, d){
    d3.selectAll(".bubbles").style("opacity", 1)
  }


  // ---------------------------//
  //       CIRCLES              //
  // ---------------------------//

  function classSelector(value) {
    if (value < 5.15)
      return "type1";
    else if (value < 5.45)
      return "type2";
    else if (value < 5.75)
      return "type3";
    else if (value < 6.05)
      return "type4";
    else if (value < 6.35)
      return "type5";
    else 
      return "type6";
  }

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .join("circle")
      .attr("class", function(d) { return "bubbles " + classSelector(d.stress_level)})
      .attr("id", function(d) {return d.gender})
      .attr("cx", function (d) { return x(d.depression_score); } )
      .attr("cy", function (d) { return y(d.anxiety_score); } )
      .attr("r", function (d) { return z(d.mental_health_risk); } )
      .style("fill", function (d) { return myColor(d.stress_level); }) 
    // -3- Trigger the functions for hover
    .on("mouseover", showTooltip )
    .on("mousemove", moveTooltip )
    .on("mouseleave", hideTooltip )



    // ---------------------------//
    //       LEGEND              //
    // ---------------------------//

    // Add legend: circles
    const valuesToShow = [0.8,1.15,1.5]
    function labelCirc(val) {
      if (val == 0.8){
        return "Low";
      } else if (val == 1.15) {
        return "Medium";
      }
      return "High";
    }
    const xCircle = width
    const xLabel = width +50
    yCircle = height - 100
    svg
      .selectAll("legend")
      .data(valuesToShow)
      .join("circle")
        .attr("cx", xCircle)
        .attr("cy", d => yCircle - z(d))
        .attr("r", d => z(d))
        .style("fill", "none")
        .attr("stroke", "black")

    // Add legend: segments
    svg
      .selectAll("legend")
      .data(valuesToShow)
      .join("line")
        .attr('x1', d => xCircle + z(d))
        .attr('x2', xLabel)
        .attr('y1', d => yCircle - z(d))
        .attr('y2', d => yCircle - z(d))
        .attr('stroke', 'black')
        .style('stroke-dasharray', ('2,2'))

    // Add legend: labels
    svg
      .selectAll("legend")
      .data(valuesToShow)
      .join("text")
        .attr('x', xLabel)
        .attr('y', d => yCircle - z(d))
        .text( d => labelCirc(d))
        .style("font-size", 10)
        .attr('alignment-baseline', 'middle')

    // Legend title
    svg.append("text")
      .attr('x', xCircle)
      .attr("y", yCircle +30)
      .text("mental health risk")
      .attr("text-anchor", "middle")

    // Add one dot in the legend for each name.
    const size = 20
    const allgroups = [5.0, 5.3, 5.6, 5.9, 6.3, 6.5]
    svg.selectAll("myrect")
      .data(allgroups)
      .join("circle")
        .attr("cx", width)
        .attr("cy", (d,i) => 10 + i*(size+5)) // 100 is where the first dot appears. 25 is the distance between dots
        .attr("r", 7)
        .style("fill", d =>  myColor(d))
        .on("mouseover", highlight)
        .on("mouseleave", noHighlight)

    // Add labels beside legend dots
    svg.selectAll("mylabels")
      .data(allgroups)
      .enter()
      .append("text")
        .attr("x", width + size*.8)
        .attr("y", (d,i) =>  i * (size + 5) + (size/1.3)) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", d => myColor(d))
        .text(d => d)
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle")
        .on("mouseover", highlight)
        .on("mouseleave", noHighlight)

    svg.append("text")
      .attr('x', width)
      .attr("y", 0)
      .text("Stress level")
      .attr("text-anchor", "left")
  })

function radioValueToGenre(val){
  switch (val) {
    case '0' : 
      return "Male"
      break;
    case '1' :
      return "Female"
      break;
    case '2' :
      return "Non-binary"
      break;
    case '3' :
      return "PreferNotToSay"
      break;
    default :
      return "All"
      break;
  }
}

// Event listener to the radio button
d3.selectAll("input[name='genre']").on("change", function() {
  const val = radioValueToGenre(this.value);
  d3.selectAll(".bubbles").style("display", "block");
  if (val != "All"){
    d3.selectAll(".bubbles").style("display", "none");
    d3.selectAll("#"+val).style("display", "block");
  } else {
    d3.selectAll(".bubbles").style("display", "block");
  }
});
