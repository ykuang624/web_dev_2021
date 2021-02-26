
// Listen to add to cart event
document.addEventListener("DOMContentLoaded", function() {
    var elements = document.getElementsByClassName("button");
    var quantities = document.getElementsByClassName("");
    
    // Generate shoppingcart Element
    var genCartElement = function(price, item_name){

        var cartSection = document.querySelector("#shopping_cart")
        var cartNode = document.createElement("div")
        cartItem = cartSection.appendChild(cartNode);
        cartItem.className = "cartItem";

        // Create Item Name
        var nameNode = document.createElement("p")
        nameNode.textContent = item_name;
        nameNode.className="redtext";
        cartItem.appendChild(nameNode)

        // Create Quantity and Price for one item in cart
        var quant_price = document.createElement("div");
        quant_price.className="row";

        var quant_text = document.createElement("p");
        quant_text.textContent = "Qty:";
        quant_text.className = "col-4"
        quant_price.appendChild(quant_text);
        
        var quant_form = document.createElement("input");
        quant_form.type ="number";
        quant_form.value = 1;
        quant_form.min = 0;
        quant_form.className = "quantity col-4";
        
        quant_price.appendChild(quant_form);

        var item_price = document.createElement("p");
        item_price.textContent = "$"+price.toString();
        item_price.className = "cart_price col-4";
        quant_price.appendChild(item_price);

        cartItem.appendChild(quant_price);
        // add eventlistener to change in the cart price of the item
        quant_form.addEventListener('change', function(){
            // Get the cart price element
            var cart = document.querySelector("#shopping_cart");
            var cartItems = cart.querySelectorAll(".cartItem");
            for (i = 0; i < cartItems.length; ++i) {
                var node = cartItems[i].querySelector(".redtext")
                if (node.textContent == item_name){
                    var parentNode = node.parentElement;
                    var cart_price = parentNode.querySelector(".row").querySelector(".cart_price");
                    var quantity = parentNode.querySelector(".row").querySelector("input");
                    cart_price.textContent = "$"+(parseFloat(quantity.value)*parseFloat(price)).toFixed(2).toString();
                };
            }
        });
};


    // Add Item to Cart
    var addToCart = function(e) {
        e.preventDefault();
        parent = e.currentTarget.parentNode.parentNode
        var price = parent.querySelector(".menu_price").innerHTML;
        var price = (parseFloat(price.toString().split("$")[1]).toFixed(2))
        var item_name = e.currentTarget.parentNode.querySelector(".redtext").innerHTML;
        
        //change button
        var buttonNode = e.currentTarget
        buttonNode.className = "col-4 button_after"
        buttonNode.textContent = "Added to Cart"
        e.currentTarget.removeEventListener('click',addToCart);
        genCartElement(price, item_name);
    };
    
    for (var i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', addToCart);
    };
});



// Change total price
document.addEventListener('click', function(e){
    cartprices = document.querySelectorAll(".cart_price")
    // document.querySelector("#total_price").addEventListener("")
    var total  = 0;
    for (var i = 0; i < cartprices.length; i++) {
        var cart_price = (parseFloat(cartprices[i].textContent.toString().split("$")[1]))
        total = (parseFloat(total) + parseFloat(cart_price)).toFixed(2)
    };
    var total_node = document.querySelector("#total_price")
    total_node.textContent= "$"+total.toString()
});
