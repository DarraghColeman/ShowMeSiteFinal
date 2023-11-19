/**
 * main.js
 * The glue logic hacks responsible for making this website interactive.
 *
 * @author Nathan Campos <nathan@innoveworkshop.com>
 */

// Ensure we are up to 2010's standard.
"use strict";

/**
 * Shows a cheerful and intrusive toast message at the top of the page.
 *
 * @param type    {string} Type of the toast.
 * @param message {string} Message to be displayed in the toast.
 */
const show_toast = function (type, message) {
    const placeholder = document.getElementById("top-toast-placeholder");
    const wrapper = document.createElement("div");

    // Build up the toast alert.
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join("\n");

    placeholder.append(wrapper);
};

/**
 * Casts a vote and notifies the user.
 *
 * @param name   {string}      Name of the poll to vote on.
 * @param option {string}      Value of the option to vote on.
 * @param elem   {HTMLElement} Element that called this function.
 */
const vote = function (name, option, elem) {
    const req_url = `/api/vote/${name}`;

    console.log(elem);

    // Prepare the request.
    const xhr = new XMLHttpRequest();
    xhr.open("POST", req_url, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Set up the response callback.
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                show_toast("success", "Your vote was successfully cast!");
                elem.classList.add("voted");
            } else {
                show_toast("danger", "An error occurred while trying to cast a vote");
            }
        }
    };

    // Perform the request.
    xhr.send(`option=${option}`);
};
