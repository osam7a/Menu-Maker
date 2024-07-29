$(document).ready(() => {
    $("#menu-button").on('click', () => {
        $("#menu-button").toggleClass("open");
        // $("#info-modal").toggleClass("hidden");
        // animate info-modal to slide up
        $("#info-modal").slideToggle();
    });

    $("#searchbar").on('input', () => { // Use 'input' to capture real-time changes
        const query = $("#searchbar").val().toLowerCase(); // Get the search query and convert it to lowercase
        $("[id^='item-']").each(function() {
            const itemText = $(this).text().toLowerCase();
            
            if (itemText.includes(query)) {
                $(this).show();
            } else {
                $(this).hide()
            }
        });
    });
});