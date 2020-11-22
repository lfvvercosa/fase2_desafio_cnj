$(document).ready(function () {

    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover({trigger: 'hover'});
    $('#cboTribunal').select2({placeholder: 'Selecione o tribunal'});
    $('.select-assuntos').select2({placeholder: 'Justiça'});
    $('.select-grau').select2({placeholder: 'Grau'});
    $('.select-classe').select2({placeholder: 'Classe processual',multiple: true});
    $('.select-grupo').select2({placeholder: 'Grupo'});
});