$.when($.ready).then(() => {
  $('#add_list').on('click', () => {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    $('.my_list li').last().remove();
  });
  $('#clear_list').on('click', () => {
    $('.my_list li').remove();
  });
});
