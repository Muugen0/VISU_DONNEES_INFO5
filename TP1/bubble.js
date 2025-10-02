// set the dimensions and margins of the graph
const margin = {top: 40, right: 150, bottom: 60, left: 30},
    width = document.getElementById("bubble_plot").clientWidth - margin.left - margin.right,
    height = document.getElementById("bubble_plot").clientWidth/2 - margin.top - margin.bottom;

//console.log(width, height);

// append the svg object to the body of the page
const svg = d3.select("#bubble_plot")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

//Read the data
d3.csv("http://localhost:8000/TP1/dataset/mental_health_dataset.csv").then( function(data) {

  // Add X axis
  const x = d3.scaleLinear()
    .domain([0, 30])
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
    .domain([0, 22])
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
  const z = d3.scaleOrdinal()
    .domain(["Low", "Medium", "High"])
    .range([ 5, 10, 20]);

  // Add a scale for bubble color
  //const myColor = console.log;
  const myColor = d3.scaleLinear()
    .domain([ 1, 5])
	.range([d3.schemeOrRd[8][2],d3.schemeOrRd[8][7]]);
    //.range(["#fdc500","#780000"]);
	
	


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
      .html("age: " + d.age)
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
    d3.selectAll("."+d).style("opacity", 1)
  }

  // And when it is not hovered anymore
  const noHighlight = function(event, d){
    d3.selectAll(".bubbles").style("opacity", 1)
  }


  // ---------------------------//
  //       CIRCLES              //
  // ---------------------------//

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .join("circle")
      .attr("class", function(d) { return "bubbles " + (d.stress_level%2 == 0 ? d.stress_level/2 : d.stress_level/2 + 0.5) })
      .attr("cx", d => x(d.depression_score))
      .attr("cy", d => y(d.anxiety_score))
      .attr("r", d => z(d.mental_health_risk))
      .style("fill", d => myColor(d.stress_level%2 == 0 ? d.stress_level/2 : d.stress_level/2 + 0.5))
    // -3- Trigger the functions for hover
    .on("mouseover", showTooltip )
    .on("mousemove", moveTooltip )
    .on("mouseleave", hideTooltip )



    // ---------------------------//
    //       LEGEND              //
    // ---------------------------//

    // Add legend: circles
    const valuesToShow = ["Low", "Medium", "High"]
    const xCircle = width
    const xLabel = width +50
    svg
      .selectAll("legend")
      .data(valuesToShow)
      .join("circle")
        .attr("cx", xCircle)
        .attr("cy", d => height)
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
        .attr('y1', d => height - 100 - z(d))
        .attr('y2', d => height - 100 - z(d))
        .attr('stroke', 'black')
        .style('stroke-dasharray', ('2,2'))

    // Add legend: labels
    svg
      .selectAll("legend")
      .data(valuesToShow)
      .join("text")
        .attr('x', xLabel)
        .attr('y', d => height - 100 - z(d))
        .text( d => d)
        .style("font-size", 10)
        .attr('alignment-baseline', 'middle')

    // Legend title
    svg.append("text")
      .attr('x', xCircle)
      .attr("y", height - 100 +30)
      .text("mental health risk")
      .attr("text-anchor", "middle")

    // Add one dot in the legend for each name.
    const size = 20
    const allgroups = [1,2,3,4,5]
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
        .attr("x", 390 + size*.8)
        .attr("y", (d,i) =>  i * (size + 5) + (size/2)) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", d => myColor(d))
        .text(d => d)
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle")
        .on("mouseover", highlight)
        .on("mouseleave", noHighlight)
  })