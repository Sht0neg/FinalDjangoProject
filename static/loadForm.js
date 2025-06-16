async function loadSalaries(data) {
    const selectEl = document.querySelector("#price")
    const option = document.createElement("option")
    last_value = undefined
    if (selectEl.children.length > 0){
        last_value = selectEl.children[0].getAttribute("value")
    }
    option.textContent = "-"
    option.setAttribute("value", "")
    selectEl.appendChild(option)
    data.forEach(vacancy => {
        if (vacancy.price != last_value){
            const option = document.createElement("option")
            option.textContent = vacancy.price
            option.setAttribute("value", vacancy.price)
            selectEl.appendChild(option)    
        }
    });
}
async function loadDates(data) {
    const selectEl = document.querySelector("#date")
    last_value = undefined
    if (selectEl.children.length > 0){
        last_value = selectEl.children[0].getAttribute("value")
    }
    const option = document.createElement("option")
    option.textContent = "-"
    option.setAttribute("value", "")
    selectEl.appendChild(option)
    data.forEach(vacancy => {
        if (vacancy.publication_date != last_value){
            const option = document.createElement("option")
            option.textContent = vacancy.publication_date
            option.setAttribute("value", vacancy.publication_date)
            selectEl.appendChild(option)
        }
    });
}
async function loadTitles(data) {
    const selectEl = document.querySelector("#title")
    last_value = undefined
    if (selectEl.children.length > 0){
        last_value = selectEl.children[0].getAttribute("value")
    }
    const option = document.createElement("option")
    option.textContent = "-"
    option.setAttribute("value", "")
    selectEl.appendChild(option)
    data.forEach(vacancy => {
        if (vacancy.title != last_value){
            const option = document.createElement("option")
            option.textContent = vacancy.title
            option.setAttribute("value", vacancy.id)
            selectEl.appendChild(option)
        }
    });
}


async function dataLoad(){
    const res = await fetch("/vacancy/all-vacancies/")
    const data = await res.json()

    loadDates(data)
    loadTitles(data)
    loadSalaries(data)
}

dataLoad()