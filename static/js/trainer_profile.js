$(document).ready(function(){
  $.get('/api/trainer', function(data){
    $('#email').append(data['trainer_email']);
    $('#name').append(data['trainer_name']);
    $('#gym').append(data['gym']);
    $('#cert').append(data['certification']);
  });
});
