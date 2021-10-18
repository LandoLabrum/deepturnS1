$(document).ready(function () {
    $('#nav-right').sidenav({ edge: "right" });
    $('#nav-left').sidenav();
    $('.dateinput').datepicker({ format: "mm/dd/yyyy" });
    $('select').formSelect();
    $('.dropdown-trigger').dropdown({ alignment: "right" });
    $('.modal').modal();
});