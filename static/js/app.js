$(document).foundation();

$(document).ready(function (){
    hideNewImport();

    $('#btnNewCompo').click(function() {
        hideNewImport();
        $('#newCompo').show();
        $(this).addClass('disabled');
    });

    $('#btnImportCompo').click(function() {
        hideNewImport();
        $('#importCompo').show();
        $(this).addClass('disabled');
    });

    $('#btnHideNewCompo').click(function() {
        $('#formNewCompo')[0].reset();
        hideNewImport();
    })

    $('#btnHideImportCompo').click(function() {
        $('#formImportCompo')[0].reset();
        hideNewImport();
    })
});

function hideNewImport() {
    $('#newCompo').hide();
    $('#importCompo').hide();
    $('#btnImportCompo').removeClass('disabled');
    $('#btnNewCompo').removeClass('disabled');
}