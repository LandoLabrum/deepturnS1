// $(document).ready(function () {   alert('worked') });
document.addEventListener('DOMContentLoaded', function () {
  $('.modal').modal();
  var elems = document.querySelectorAll('.materialboxed');
  M.Materialbox.init(elems);
  var datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker);
  var timepicker = document.querySelectorAll('.timepicker', { 'vibrate': true });
  M.Timepicker.init(timepicker);

  $('.err').hide();

  const isNumericInput = (event) => {
    const key = event.keyCode;
    return ((key >= 48 && key <= 57) || // Allow number line
      (key >= 96 && key <= 105) // Allow number pad
    );
  };

  const isModifierKey = (event) => {
    const key = event.keyCode;
    return (event.shiftKey === true || key === 35 || key === 36) || // Allow Shift, Home, End
      (key === 8 || key === 9 || key === 13 || key === 46) || // Allow Backspace, Tab, Enter, Delete
      (key > 36 && key < 41) || // Allow left, up, right, down
      (
        // Allow Ctrl/Command + A,C,V,X,Z
        (event.ctrlKey === true || event.metaKey === true) &&
        (key === 65 || key === 67 || key === 86 || key === 88 || key === 90)
      )
  };

  const enforceFormat = (event) => {
    // Input must be of a valid number format or a modifier key, and not longer than ten digits
    if (!isNumericInput(event) && !isModifierKey(event)) {
      event.preventDefault();
    }
  };

  const formatToPhone = (event) => {
    if (isModifierKey(event)) { return; }

    const input = event.target.value.replace(/\D/g, '').substring(0, 10); // First ten digits of input only
    const areaCode = input.substring(0, 3);
    const middle = input.substring(3, 6);
    const last = input.substring(6, 10);

    if (input.length > 6) { event.target.value = `(${areaCode}) ${middle} - ${last}`; }
    else if (input.length > 3) { event.target.value = `(${areaCode}) ${middle}`; }
    else if (input.length > 0) { event.target.value = `(${areaCode}`; }
  };

  const inputElement = document.getElementById('phoneNumber');
  inputElement.addEventListener('keydown', enforceFormat);
  inputElement.addEventListener('keyup', formatToPhone);



  // var email = $('#email').val();
  // if(IsEmail(email)==false){
  //   $('#invalid_email').show();
  //   return false;
  // }
  // $('#email').on('change', function() {
  //   // alert( this.value );

  // });

});
$(".link").click(function () {
  window.location = $(this).find("a").attr("href");
  return false;
});
function confirm(str, title) {
  confirm = window.confirm(str);
  if (confirm == true) {
    document.getElementById(title).submit();
  }
}
function timeHandler(t) {
  var trig = $('#time-trigger')
  trig.removeClass('blue lighten-3');
  trig.addClass('grey lighten-2');
  trig.text(t);
  trig.append("<i class='material-icons left'>check</i>");
  $('#time-modal').modal('close');
}
function dateHandler(t) {
  var trig = $('#date-trigger')
  trig.removeClass('blue lighten-3');
  trig.addClass('grey lighten-2');
  trig.text(t);
  trig.append("<i class='material-icons left'>check</i>");
  $('#date-modal').modal('close');
}
function IsEmail(email) {
  var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if (!regex.test(email)) {
    return false;
  } else {
    return true;
  }
}
function IsTel(tel) {
  var regex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
  if (!regex.test(tel)) {
    return false;
  } else {
    return true;
  }
}

function emailHandler() {
  var email = $('#email').val();
  if (IsEmail(email) == false) {
    $('#invalid_email').show();
    return false;
  } else {
    $('#invalid_email').hide();
  }
}

