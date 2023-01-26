function resetSliders() {}

function updateDemographicTurnout() {}

const raceDropdown = document.getElementById("race");
const demographicsDropdown = document.getElementById("demographics");
const subdivisionDropdown = document.getElementById("subdivision");

async function initializeAndSortDropdownLabels() {
    const baseURL = new URL("/data/swingometer/", window.location.origin);

    const yearsArray = await fetch("/data/swingometer/years.json").then(
        (data) => data.json()
    );

    let raceOptions = [];
    let demographicsOptions = [];

    let promises = [];
    for (const dirName of yearsArray) {
        const folderURL = new URL(dirName + "/", baseURL);

        async function addDropdownOption(fileName, dropdown, dropdowns) {
            let data = await fetch(new URL(fileName, folderURL)).then(
                (response) => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        return null;
                    }
                }
            );

            if (data === null) {
                return;
            }

            let option = document.createElement("option");
            option.text = data.optionName;
            option.value = folderURL.href.split("/").reverse()[1];
            option.sourceCitations = data.sourceCitations;
            option.sourceURLs = data.sourceURLs;
            dropdowns.push(option);
        }

        promises.push(
            addDropdownOption(
                "electionResults.json",
                raceDropdown,
                raceOptions
            ),
            addDropdownOption(
                "demographics.json",
                demographicsDropdown,
                demographicsOptions
            )
        );
    }

    await Promise.all(promises);

    const comparator = (a, b) => a.value.localeCompare(b.value);

    for (const option of raceOptions.sort(comparator)) {
        raceDropdown.options.add(option);
    }
    for (const option of demographicsOptions.sort(comparator)) {
        demographicsDropdown.options.add(option);
    }
}

// hover and right click mouse effect
function addMouseEffects(dropdown) {
    let timer = null;
    let parentSpan = dropdown.parentElement;

    dropdown.onmouseover = () => {
        const selectedOption = dropdown.options[dropdown.selectedIndex];
        timer = setTimeout(() => {
            parentSpan.setAttribute(
                "hover-text",
                selectedOption.sourceCitations.toString()
            );
            parentSpan.style.setProperty("--hover-text-opacity", 1);
        }, 1000);
    };

    dropdown.onmouseout = () => {
        clearTimeout(timer);
        parentSpan?.style?.setProperty("--hover-text-opacity", 0);
    };

    dropdown.oncontextmenu = async () => {
        const selectedOption = dropdown.options[dropdown.selectedIndex];
        for (const url of selectedOption.sourceURLs) {
            window.open(url);
        }
    };
}

function coupleSlidersAndTextInputs() {
    for (let slider of document.getElementsByClassName("partisan-slider")) {
        let box =
            slider.parentElement.getElementsByClassName("partisan-text")[0];
        slider.oninput = () => {
            box.value = slider.value;
        };
        box.onchange = () => {
            slider.value = box.value;
        };
    }

    for (let slider of document.getElementsByClassName("turnout-slider")) {
        let box =
            slider.parentElement.getElementsByClassName("turnout-text")[0];
        slider.oninput = () => {
            box.value = slider.value;
            updateDemographicTurnout();
        };
        box.onchange = () => {
            slider.value = box.value;
            updateDemographicTurnout();
        };
    }
}

async function initializeData(raceYear, demographicsYear, subdivision) {
    await fetch(`/data/swingometer/${raceYear}/electionResults.json`)
        .then((response) => response.json())
        .then((data) => {
            resetSliders = () => {
                for (const [
                    group,
                    { gopVotePct, turnoutPct },
                ] of Object.entries(data.nationwideData)) {
                    const partisanSlider = document.querySelector(
                        `#${group} .partisan-slider`
                    );
                    const turnoutSlider = document.querySelector(
                        `#${group} .turnout-slider`
                    );

                    partisanSlider.value = gopVotePct;
                    turnoutSlider.value = turnoutPct;

                    partisanSlider.oninput();
                    turnoutSlider.oninput();
                }
            };
            resetSliders();
        });

    await fetch(`/data/swingometer/${demographicsYear}/demographics.json`)
        .then((response) => response.json())
        .then((data) => {
            const populationData = data.nationwidePopulation;

            updateDemographicTurnout = () => {
                let totalVotesCast = 0;
                for (const element of document.querySelectorAll(
                    "#sliders > div"
                )) {
                    let id = element.id;
                    let slider =
                        element.getElementsByClassName("turnout-slider")[0];

                    totalVotesCast +=
                        (parseFloat(slider.value) / 100) * populationData[id];
                }
                for (const [idx, element] of document
                    .querySelectorAll("#sliders > div")
                    .entries()) {
                    let id = element.id;
                    let turnoutDisplay = element.getElementsByClassName(
                        "demographic-turnout"
                    )[0];
                    let slider =
                        element.getElementsByClassName("turnout-slider")[0];

                    let votesCast =
                        (parseFloat(slider.value) / 100) * populationData[id];
                    let percentOfVotesCast = (
                        (votesCast / totalVotesCast) *
                        100
                    ).toFixed(2);
                    if (isNaN(percentOfVotesCast)) {
                        percentOfVotesCast = 0.0;
                    }

                    if (idx == 0) {
                        turnoutDisplay.innerHTML = `${percentOfVotesCast}% of all voters`;
                    } else {
                        turnoutDisplay.innerHTML = `${percentOfVotesCast}%`;
                    }
                }
            };
            updateDemographicTurnout();
        });
}

async function initializeDataFromInputs() {
    await initializeData(
        document.getElementById("race").value,
        document.getElementById("demographics").value,
        document.getElementById("subdivision").value
    );
}
