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
    let monthes = []
    data.forEach(vacancy=>{
        if (!monthes.includes(vacancy.publication_date)){
            monthes.push(vacancy.publication_date)
        }
    })
    let monthes_to_strings = {
        "1": "Январь",
        "2": "Февраль",
        "3": "Март",
        "4": "Апрель",
        "5": "Май",
        "6": "Июнь",
        "7": "Июль",
        "8": "Август",
        "9": "Сентябрь",
        "10": "Октябрь",
        "11": "Ноябрь",
        "12": "Декабрь"
    }
    console.log(monthes)
    monthes.forEach(month => {
        if (month!= last_value){
            const option = document.createElement("option")
            option.textContent = monthes_to_strings[month]
            option.setAttribute("value", month)
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
}

dataLoad()