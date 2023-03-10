class PrepareResult {
    sheets = []
    init(resultsheet) {
        this.sheets.push(resultsheet)
    }

    thisSheet(index) {
        var sheet = this.sheets[index]
        var students = ''
        var subjects = ''
        console.log(sheet.result.results)




        sheet.result.results.forEach(element => {
            var marks = ''
            element.marks.forEach(mark=>{
                marks = marks +  `<div>${parseInt(mark.theory) + parseInt(mark.practical)}</div>`
            })
            students = students + `
            <div>
                <div class="subjects-area">
                    <div class="subjects-area-btn lg-sub">${element.student.name} (Roll No : ${element.student.rollno})</div>
                    <div class="subjects">
                       ${marks}
                    </div>
                </div>
            </div>`
        });



        sheet.result.subjects.forEach(sub=>{
            subjects = subjects + `<div>${sub.name}</div>`
        })




        var template = `<div class="result-sheet" id="${sheet.id}" style="height:90px">
                <div class="about-result">
                    <b>
                        ${sheet.name}
                    </b>

                    <div class="dateandpercent">
                        <b>Percentage:</b>&nbsp;
                        <input type="text" name="" id="" value="100">
                        <div class="subjects-area-btn p-5" onclick="openSheet(${sheet.id})"><span
                        class="material-symbols-outlined arrow-down">
                        keyboard_double_arrow_down
                    </span>
                </div>
                    </div>

                </div>
                <div class="subjects-area head-sub">
                    <div class="subjects-area-btn lg-sub">Subjects</div>
                    <div class="subjects ">
                       ${subjects}
                    </div>
                   
                </div>
                ${students}
            </div>`

        return template
    }
}

class Result_Model {
    init(percentage, name, result, id) {
        this.name = name
        this.result = result
        this.percentage = percentage
        this.id = id
    }
}

function openSheet(id) {
    var sheet = document.getElementById(id)
    if (sheet.style.height == '90px') {
        sheet.style.height = ''
    } else {
        sheet.style.height = '90px'
    }
}