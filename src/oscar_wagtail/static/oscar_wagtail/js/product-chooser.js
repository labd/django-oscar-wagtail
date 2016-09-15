function createProductChooser(id, contentType) {
    var chooserElement = $('#' + id + '-chooser');
    var docTitle = chooserElement.find('.title');
    var input = $('#' + id);
    var editLink = chooserElement.find('.edit-link');

    $('.action-choose', chooserElement).click(function() {
        ModalWorkflow({
            url: window.chooserUrls.productChooser,
            responses: {
                productChosen: function(productData) {
                    input.val(productData.id);
                    docTitle.text(productData.string);
                    chooserElement.removeClass('blank');
                    editLink.attr('href', productData.edit_link);
                }
            }
        });
    });

    $('.action-clear', chooserElement).click(function() {
        input.val('');
        chooserElement.addClass('blank');
    });
}
