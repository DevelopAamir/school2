function swithsetting() {
    var settingspart = document.getElementById('settings-part')
    if (settingspart.style.height != "500px") {
        settingspart.style.height = "500px"

    } else {
        settingspart.style.height = "0px"
    }
}



function getSubjects(resultSheet) {
    var tablesub = document.getElementById('subjects')
    tablesub.replaceChildren()
    resultSheet.subjects.forEach((element, index) => {
 
        var sub = `
        <tr subject-id="${element.id}">
            <td>
                ${index + 1}
            </td>
            <td>
                <input type="text" value="${element.name}" field_name="name" onchange="updateSubjects(${element.id}, 'name', this.value)">
            </td>
    
            <td>
                <input type="number" value="${element.full_marks}" field_name="full_marks" onchange="updateSubjects(${element.id}, 'full_marks', this.value)">
            </td>
            <td>
                <input type="number" value="${element.pass_marks}" field_name="pass_marks" onchange="updateSubjects(${element.id}, 'pass_marks', this.value)">
            </td>
            <td>
                <input type="number" value="${element.theory_marks}" field_name="theory_marks" onchange="updateSubjects(${element.id}, 'theory_marks', this.value)">
            </td>
            <td>
                <input type="number" value="${element.theory_pass_marks}" field_name="theory_pass_marks" onchange="updateSubjects(${element.id}, 'theory_pass_marks', this.value)">
            </td>
            <td>
                <input type="number" value="${element.practical_marks}" field_name="practical_marks" onchange="updateSubjects(${element.id}, 'practical_marks', this.value)">
            </td>
            <td>
                <input type="number" value="${element.practical_pass_marks}" field_name="practical_pass_marks" onchange="updateSubjects(${element.id}, 'practical_pass_marks', this.value)">
            </td>
            <td>
                <span class="material-symbols-outlined"onclick="upSubject(${index})">
                    fitbit_arrow_upward
                </span>
                <span class="material-symbols-outlined"onclick="downSubject(${index})">
                    fitbit_arrow_downward
                </span>
                <span class="material-symbols-outlined" onclick="deleteSubject(${element.id})">
                    delete
                </span>
            </td>

        </tr>`
        tablesub.innerHTML = tablesub.innerHTML + sub
    });

}

