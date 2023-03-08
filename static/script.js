$(document).ready(function() {
        $('#search-button').click(function() {
          var stock_name = $('#search-box').val();
          $.post('/', { stock_name: stock_name }, function(data) {
            $('#stock-name').text(stock_name);
            $('#current-price').text(data.current_price);
            $('#week-high').text(data.week_high);
            $('#week-low').text(data.week_low);
            $('#stock-details').show();
          });
        });
      });