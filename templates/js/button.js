var GetCoordinates = d3.select("#button");

GetCoordinates.on("click", function() {

  // Select the input element and get the raw HTML node
    var inputElementO = d3.select("#Origin");
    var inputElementD = d3.select("#Destiny");
  // Get the value property of the input element
  var inputValueO = inputElementO.property("value");
  var inputValueD = inputElementD.property("value");

  console.log(inputValueO);
  console.log(inputValueD);

  d3.json("airports.json", function(error,data){
    for (var i=0; i<data.length; i++){
      
      if (data[i].city===inputValueO){
        console.log(data[i].city);
        console.log(data[i].lat_decimal);
      }
    }

    var line=[
      [origin_lat,orgin_lon],
      [destiny_lat,destiny_lon]
    ];

    L.pollyline(line,{ 
      color:"red"
    }).addTo(map);
    
    
  });
  // for (var index = 0; index < response.length; index++) {
    
  // if (inputValueD === coordinates.city){
  //   console.log(coordinates.lat_decimal);
  // };
  // d3.json("airports.json", function(error,data){
  //   for (var index = 0; index < data.length; index++){
  //   if(data.city === inputValueO){
  //     return data.lat_decimal
  //   }
  // };

  // //return

});
