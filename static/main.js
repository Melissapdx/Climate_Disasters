
  $(function(){
    var $disasterTypeSector = $('#disasterType');
    var $disasterYearSector = $('#disasterYear');

    $('#disasterType, #disasterYear').on('change', function(e){
      var typeSelected = $disasterTypeSector.val();
      var yearSelected = $disasterYearSector.val();
      
      var url = '/api/v1/disasters';
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
          console.log(data);
        },
        error: function(){
          // TODO: some UI to show that we hit an error.
          console.error(arguments);
        }
      });
    }

    // function showData(data) {
    //   // Update the map with the disaster information
    //   var highestValue = max([0, 1, 34, 44])
    //   values.each(value => {
    //     value/highestValue // 34/44 = 0.7727272727. value would be 772.
    //   })

    // }
  });