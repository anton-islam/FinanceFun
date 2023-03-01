function editExpense(expenseId) {
  // Make an AJAX call to the server to get the expense data
  $.ajax({
    url: '/expenses/' + expenseId + '/edit/',
    type: 'GET',
    success: function(response) {
      // Update the HTML form with the expense data
      $('#date').val(response.date);
      $('#item_name').val(response.item_name);
      $('#payment_method').val(response.payment_method);
      $('#amount').val(response.amount);
      $('#description').val(response.description);

      // Update the form action to submit the edited data
      $('form').attr('action', '/expenses/' + expenseId + '/edit/');

      // Change the submit button text
      $('button[type="submit"]').text('Save');
    }
  });
}

function removeExpense(expenseId) {
  // Make an AJAX call to the server to delete the expense data
  $.ajax({
    url: '/expenses/' + expenseId + '/delete/',
    type: 'POST',
    data: {
      csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    success: function() {
      // Remove the expense row from the HTML table
      $('tr[data-expense-id="' + expenseId + '"]').remove();
    }
  });
}