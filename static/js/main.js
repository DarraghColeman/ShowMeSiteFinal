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
    // Prepare the request.
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `/api/vote/${name}`, true);
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

/**
 * Populates the results into the page.
 *
 * @param container {HTMLElement} Element that will contain the results.
 */
const populate_results = function (container) {
    // Prepare the request.
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `/api/polls`, true);

    // Set up the response callback.
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const polls = JSON.parse(xhr.responseText)["polls"];
                polls.forEach(function (poll) {
                    // Build up the chart wrapper.
                    const wrapper = document.createElement("div");
                    wrapper.innerHTML = `<canvas id="chart-${poll["name"]}"></canvas>`;
                    container.append(wrapper);

                    // Set up the chart.
                    new Chart(document.getElementById(`chart-${poll["name"]}`), {
                        type: "bar",
                        options: {
                            indexAxis: "y"
                        },
                        data: {
                            labels: poll["options"].map(function (opt) {
                                return opt["label"];
                            }),
                            datasets: [
                                {
                                    label: poll["title"],
                                    data: poll["options"].map(function (opt) {
                                        return opt["votes"];
                                    }),
                                    fill: false,
                                    backgroundColor: [
                                        'rgba(54, 162, 235, 0.2)',
                                        'rgba(255, 205, 86, 0.2)',
                                        'rgba(75, 192, 192, 0.2)',
                                        'rgba(255, 159, 64, 0.2)',
                                        'rgba(153, 102, 255, 0.2)',
                                        'rgba(201, 203, 207, 0.2)'
                                    ],
                                    borderColor: [
                                        'rgb(54, 162, 235)',
                                        'rgb(255, 205, 86)',
                                        'rgb(75, 192, 192)',
                                        'rgb(255, 159, 64)',
                                        'rgb(153, 102, 255)',
                                        'rgb(201, 203, 207)'
                                    ],
                                    borderWidth: 1
                                }
                            ]
                        }
                    });
                });
            } else {
                show_toast("danger", "An error occurred while trying to fetch results");
            }
        }
    };

    // Perform the request.
    xhr.send();
}
