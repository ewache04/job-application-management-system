// mystaticfiles/js_files/myglobal_scripts.js

// Function to update background looks
function updateBackgroundColor(user_id) {
    $.ajax({
        url: `/user/${user_id}/get_background_color/`,
        type: "GET",
        dataType: "json",
        success: function(data) {
            if (data.background_color) {
                $('body').css('background-color', data.background_color);
            } else {
                console.error("No background color found in response.");
            }
        },
        error: function(xhr, status, error) {
            console.error("AJAX Error: ", status, error);
        }
    });
}

// Function to show the loading indicator
function showLoadingIndicator() {
    $('#loadingSpinner').fadeIn('slow');
}

// Function to hide the loading indicator
function hideLoadingIndicator() {
    $('#loadingSpinner').fadeOut('slow');
}

// Function to hide alert message and reset session after a specified timeout
function hideAlertAndResetSession(resetMessageID, resetUrl, csrfToken, timeout) {
    setTimeout(function () {
        var resetMessageElement = document.getElementById(resetMessageID);
        if (resetMessageElement) {
            resetMessageElement.style.display = 'none';

            // AJAX request to delete the session key after hiding the message
            var xhr = new XMLHttpRequest();
            xhr.open('GET', resetUrl, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);
            xhr.send();
        }
    }, timeout);
}

// Function to filter table rows based on input
function filterTableRows() {
    var input = document.getElementById("myInput");
    var filter = input.value.toUpperCase();
    var table = document.getElementById("myTable");
    var tr = table.getElementsByTagName("tr");
    var found = false;

    for (var i = 0; i < tr.length; i++) {
        var cells = tr[i].getElementsByTagName("td");
        var cellFound = false;

        for (var j = 0; j < cells.length; j++) {
            var td = cells[j];
            if (td) {
                var txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    cellFound = true;
                    break; // Exit the inner loop if match is found
                }
            }
        }

        tr[i].style.display = cellFound ? "" : "none";
        found = found || cellFound;
    }

    document.getElementById("notFound").style.display = found ? "none" : "block";
}

// Function for smooth scrolling
function smoothScrolling() {
    $(".navbar a, footer a[href='#myPage']").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 900, function () {
                window.location.hash = hash;
            });
        }
    });

    $(window).scroll(function () {
        $(".slideanim").each(function () {
            var pos = $(this).offset().top;
            var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
                $(this).addClass("slide");
            }
        });
    });
}

// Function to initialize event listeners and page functionality
function initializePage(userId) {
    updateBackgroundColor(userId);

    // Show loading indicator on page load
    showLoadingIndicator();

    // Hide loading indicator once the document is fully loaded
    $(window).on('load', function() {
        hideLoadingIndicator();
    });

    // Call the hideAlertAndResetSession function
    hideAlertAndResetSession('alertMessage', '/reset_alert_message_session_value', csrfToken, 3000);
    hideAlertAndResetSession('greetingMessage', '/reset_greeting_message_session_value', csrfToken, 7000);

    // Add event listener for filtering table rows
    document.getElementById("myInput").addEventListener("input", filterTableRows);

    // Call the smoothScrolling function
    smoothScrolling();
}

// Show loading indicator on AJAX request start
$(document).ajaxStart(function() {
    showLoadingIndicator();
});

// Hide loading indicator on AJAX request complete
$(document).ajaxStop(function() {
    hideLoadingIndicator();
});