// Create Django Ajax Call
$("form#addProduct").submit(function() {
    var nameInput = $('input[name="name"]').val().trim();
    var categoryInput = $('input[name="category"]').val().trim();
    var quantityInput = $('input[name="quantity"]').val().trim();
    var priceInput = $('input[name="price"]').val().trim();
    if (nameInput && categoryInput && quantityInput && priceInput) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "AddProducts" %}',
            data: {
                'name': nameInput,
                'category': categoryInput,
                'quantity': quantityInput,
                'price': priceInput
            },
            dataType: 'json',
            success: function (data) {
                if (data.product) {
                  appendToProductTable(data.product);
                }
            }
        });
      } else {
        alert("All fields must have a valid value.");
    }
    $('form#addProduct').trigger("reset");
    return false;
});
function appendToProductTable(product) {
  $("#ProductTable > tbody:last-child").append(`
        <tr id="product-${product.id}">
        <td class="productName" name="name">${product.name}</td>
        '<td class="productCategory" name="category">${product.category}</td>
        '<td class="productQuantity" name="quantity">${product.quantity}</td>
        '<td class="productPrice" name="price">${product.price}</td>
        '<td align="center">
                <button class="btn btn-success form-control" onClick="editProduct(${product.id})" data-toggle="modal" data-target="#EditProductModal")">EDIT</button>
            </td>
            <td align="center">
                <button class="btn btn-danger form-control" onClick="deleteProduct(${product.id})" data-toggle="modal" data-target="#DeleteProductModal">DELETE</button>
            </td>
        </tr>
    `);
}