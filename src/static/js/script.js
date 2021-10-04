function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Use csrf token while doing post request, this will prevent 500 Server Error
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
}); 

//All Products API
$.ajax({
    url : "http://localhost:8000/api/products/",
    dataType: "json",
    success : function (response) {
        var trHTML = '';
        $.each(response, function (i, item) {
           trHTML += "<tr><th>" + item.id + "</th><td>" + item.name + "</td><td>" + item.category + "</td><td>" + item.quantity + "</td><td>" + item.price +  "</td><td> <button class='btn btn-success update btn-sm' id ="+ item.id +" data-toggle='modal' data-target='#editProduct'>Update</button> <button class='btn btn-danger delete btn-sm' id ="+ item.id +" data-toggle='modal' data-target='#deleteProduct'>Delete</button>"
           "</td></tr>";
        });
        $('#Product-Records').append(trHTML);
    }
});

//Edit Products API
$('#Product-Records').on('click', '.update', function(){
    var id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    var myurl = 'http://localhost:8000/api/products/'+id+'/';

    $( "#p-name" ).change(function() {
        $('input[name=name]').val($(this).val());
    });
    $( "#p-category" ).change(function() {
        $('select[name=category]').val($(this).val());
    });
    $( "#p-quantity" ).change(function() {
        $('input[name=quantity]').val($(this).val());
    });
    $( "#p-price" ).change(function() {
        $('input[name=price]').val($(this).val());
    });

    $.ajax({
        async: true,
        url:myurl,
        method:'GET',
        success: function(result){
            $('input[name="name"]').val(result.name);
            $('select[name="category"]').val(result.category);
            $('input[name="quantity"]').val(result.quantity);
            $('input[name="price"]').val(result.price);
        }
    });

});

//Delete Products API
$('#Product-Records').on('click', '.delete', function(){
    var id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    var myurl = 'http://localhost:8000/api/products/delete/'+id+'/';

    $.ajax({
        async: true,
        url:myurl,
        method:'DELETE',
        success: function(result){
            location.reload();
        }
    });

});

$('#create').click(function(){ 
    $("#add-Product").trigger('reset');
});

//Save New Product Button
$('#p-create').click(function(){
    $.ajax({
        type : 'POST',
        url : "http://localhost:8000/api/products/add/",
        data : {
            '_token':$('input[name=_token]').val(),
            'name':$('input[name=name]').val(),
            'category':$('select[name=category]').val(),
            'quantity':$('input[name=quantity]').val(),
            'price':$('input[name=price]').val()
        },
        success: function(data){
           location.reload(); 
        }
    })
});

//Save Edited Product Button
$('#p-edit').click(function(){
    var id = $("#Myid").attr("value");
    console.log(id);
    var myurl = "http://localhost:8000/api/products/edit/"+id+"/";

    $.ajax({
        type : 'PUT',
        url : myurl,
        data : {
            '_token':$('input[name=_token]').val(),
            'name':$('input[name=name]').val(),
            'category':$('select[name=category]').val(),
            'quantity':$('input[name=quantity]').val(),
            'price':$('input[name=price]').val()
        },
        success: function(data){
           location.reload();
        },
    })
});