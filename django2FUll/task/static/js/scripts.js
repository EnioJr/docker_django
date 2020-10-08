// Usado para chamar uma janela de aletar para confirmar que deseja deletar tal tarefa
// Encontrado em templates.list.html chamado no delete-btn 
//  ' < delete/{{task.id}}" class="delete-btn" > '

$(document).ready(function () {

    var baseUrl = 'http://0.0.0.0:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if (result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

    $(filter).change(function () {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });


});