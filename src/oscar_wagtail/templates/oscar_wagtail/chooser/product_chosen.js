function(modal) {
    modal.respond('productChosen', {{ product_json|safe }});
    modal.close();
}
