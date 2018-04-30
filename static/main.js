var currentMapData = null;

$(function(){
  var url = '/api/v1/disasters';
  
  map.on('load', function () {
    getData(url);
  });
  

  var $disasterTypeSector = $('#disasterType');
  var $disasterYearSector = $('#disasterYear');

  $('#disasterType, #disasterYear').on('change', function(e){
    var typeSelected = $disasterTypeSector.val();
    var yearSelected = $disasterYearSector.val();
    
    if(typeSelected !== 'All' && yearSelected !== "All") {
      // user selected both type and year.
      url += '/yeartype/' + yearSelected + '/' + typeSelected;
    } else if(typeSelected !== 'All') {
      // user selected just type.
      url += '/type/' + typeSelected;
    } else if(yearSelected !== 'All') {
      // user selected just year.
      url += '/year/' + yearSelected;
    }
    getData(url);
  });


  function getData(url) {
    // get the data from the API.
    $.ajax({
      method: 'GET',
      url: url,
      success: function(data){
        currentMapData = data;
        showData(data);
      },
      error: function(){
        // TODO: some UI to show that we hit an error.
        console.error(arguments);
      }
    });
  }

  // Update the map with the disaster information
  function showData(data) {  
    // TODO: Replace Object.values. Doens't work in IE
    var highestNum = getMaxOfArray(Object.values(data));
    
    var normalizedData = Object.assign({}, data);

    Object.keys(normalizedData).forEach(function(key) {
      var value = normalizedData[key];
      normalizedData[key] = (normalizedData[key] / highestNum) * 1000;
    });

    

    statesData.features.forEach(function(stateData){
      var longName = stateData.properties.name;
      var value = normalizedData[stateMapping[longName]];
      if (value) {
        stateData.properties.density = value;
      } else {
        stateData.properties.density = 0;
      }
    });
    renderLayer(statesData);

  };
});

function getMaxOfArray(numArray) {
  return Math.max.apply(null, numArray);
}

var stateMapping = {
  'Alabama': 'AL',
  'Alaska': 'AK',
  'Arizona': 'AZ',
  'Arkansas': 'AR',
  'California': 'CA',
  'Colorado': 'CO',
  'Connecticut': 'CT',
  'Delaware': 'DE',
  'District Of Columbia': 'DC',
  'Florida': 'FL',
  'Georgia': 'GA',
  'Hawaii': 'HI',
  'Idaho': 'ID',
  'Illinois': 'IL',
  'Indiana': 'IN',
  'Iowa': 'IA',
  'Kansas': 'KS',
  'Kentucky': 'KY',
  'Louisiana': 'LA',
  'Maine': 'ME',
  'Maryland': 'MD',
  'Massachusetts': 'MA',
  'Michigan': 'MI',
  'Minnesota': 'MN',
  'Mississippi': 'MS',
  'Missouri': 'MO',
  'Montana': 'MT',
  'Nebraska': 'NE',
  'Nevada': 'NV',
  'New Hampshire': 'NH',
  'New Jersey': 'NJ',
  'New Mexico': 'NM',
  'New York': 'NY',
  'North Carolina': 'NC',
  'North Dakota': 'ND',
  'Ohio': 'OH',
  'Oklahoma': 'OK',
  'Oregon': 'OR',
  'Pennsylvania': 'PA',
  'Rhode Island': 'RI',
  'South Carolina': 'SC',
  'South Dakota': 'SD',
  'Tennessee': 'TN',
  'Texas': 'TX',
  'Utah': 'UT',
  'Vermont': 'VT',
  'Virginia': 'VA',
  'Washington': 'WA',
  'West Virginia': 'WV',
  'Wisconsin': 'WI',
  'Wyoming': 'WY'
};
