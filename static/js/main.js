// $(document).ready(function () {   alert('worked') });
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.materialboxed');
  var instances = M.Materialbox.init(elems, options);
});
$(".link").click(function () {
  window.location = $(this).find("a").attr("href");
  return false;
});
function confirm(str, title){
  confirm = window.confirm(str);
  if (confirm == true){
      document.getElementById(title).submit();
  }
}