class ResultsSheet {
    subjects = []
    results = []
    init(subjects, students) {
        this.subjects = subjects
        students.forEach((element) => {
            var result = new Result()
            result.init(element, subjects)
            this.results.push(result)
        })
    }
    addSubject(subject) {
        subjects.push(subject)
    }
    widget() {
        var child = document.createElement('div')
        this.results.forEach((element) => {
            var elementsfiled = ''
            element.marks.forEach(field => {
                elementsfiled = elementsfiled + field.widget()
            })
            child.innerHTML = child.innerHTML + element.widget()


        })

        return child
    }

    update(student_id, subject_id, value, type) {
        this.results.filter(function (element) {
            return element.student.id == student_id
        }).forEach(selected_student => {
            selected_student.marks.filter(subject => {
                return subject.subject.id == subject_id;
            }).forEach(item => {

                if (type == 'th') {
                    item.theory = value
                } else {
                    item.practical = value
                }
            })

        })

    }

    initinstance(data) {
   
        var subjects = data['subjects']
        var results = data['results']

        subjects.forEach(subject => {
            var subject_new = new Subject()
            subject_new.init(subject['name'], subject['full_marks'], subject['pass_marks'], subject['practical_marks'], subject["practical_pass_marks"], subject['theory_marks'], subject["theory_pass_marks"], subject['id'])
            this.subjects.push(subject_new)
        })

        results.forEach(result => {
            var result_new = new Result()
            result_new.initinstance(result)
            this.results.push(result_new)
        })
    }

    updateSubject(subject_id, field_name, value) {
        this.subjects.forEach(subject => {
            if (subject.id == subject_id) {
                if (field_name == 'name') {
                    subject.name = value
                } else if (field_name == 'full_marks') {
                    subject.full_marks = value
                } else if (field_name == 'pass_marks') {
                    subject.pass_marks = value
                }
                else if (field_name == 'theory_marks') {
                    subject.theory_marks = value
                } else if (field_name == 'theory_pass_marks') {
                    subject.theory_pass_marks = value
                } else if (field_name == 'practical_marks') {
                    subject.practical_marks = value
                } else if (field_name == 'practical_pass_marks') {
                    subject.practical_pass_marks = value
                }
            }
        });
        this.results.forEach(result => {
            result.marks.forEach(mark => {
                if (mark.subject.id == subject_id) {
                    if (field_name == 'name') {
                        mark.subject.name = value
                    } else if (field_name == 'full_marks') {
                        mark.subject.full_marks = value
                    } else if (field_name == 'pass_marks') {
                        mark.subject.pass_marks = value
                    }
                    else if (field_name == 'theory_marks') {
                        mark.subject.theory_marks = value
                    } else if (field_name == 'theory_pass_marks') {
                        mark.subject.theory_pass_marks = value
                    } else if (field_name == 'practical_marks') {
                        mark.subject.practical_marks = value
                    } else if (field_name == 'practical_pass_marks') {
                        mark.subject.practical_pass_marks = value
                    }
                }
            })
        })


    }


    addSubject(name, full_marks, pass_marks, practical_marks, practical_pass_marks, theory_marks, theory_pass_marks) {
        var id = 0;
        var alreadyExist = false;
        this.subjects.forEach(subject => {
            if (parseInt(subject.id) >= id) {
                id = parseInt(subject.id) + 1;
            }
        
            if (subject.name.toString() != name) {

            } else {
                alreadyExist = true;
            }

        });
        var subject_new = new Subject()
        subject_new.init(name, full_marks, pass_marks, practical_marks, practical_pass_marks, theory_marks, theory_pass_marks, id)
        if (!alreadyExist) {
            this.subjects.push(subject_new)
            this.results.forEach(result => {
                result.addMarks(subject_new)

            })
        } else {
            alert(`${name} Already Exist !`)
        }


    }

    deleteSubject(id) {

        this.subjects.forEach(sub => {
            if (sub.id == id) {
                this.subjects = arrayRemove(this.subjects, sub)
            }

        })
        this.results.forEach(result => {
            result.deleteMarks(id)

        })

    }

    subjectmove(id, new_index) {
        this.subjects = array_move(this.subjects, id, new_index)
        this.results.forEach(result => {
            result.marks = array_move(result.marks, id, new_index)
        })
    }

    deleteStudent(id, token) {
        document.getElementById('body').innerHTML = document.getElementById('body').innerHTML + `
            <div class="dialogue-place" style="display:none" id="dialogue">
            <div class="dialogue-box" >
                <b class="dialogue-title">You are about to delete this Student?</b>
                <p>All the records will be permenently removed and you won't be able to see them again.</p>
                <div class="dialogue-actions">
                    <button class="cancel-button" id="cancel-btn-dialogue">cancel</button>
                    <button class="delete-btn"  id="delete-btn-dialogue">Delete</button>
                </div>
            </div>
        </div>
        `
        var dialogue = document.getElementById('dialogue')
        var yessbtn = document.getElementById('delete-btn-dialogue')
        var cancelbtn = document.getElementById('cancel-btn-dialogue')
        dialogue.style.display = '';
        yessbtn.addEventListener('click', () => {
            this.results.forEach(ele => {
                if (ele.student.id == id) {
                    console.log(ele.student.id == id)
                    console.log(ele.student.id , id)
                    this.results = arrayRemove(this.results, ele)
                }
            })
            dialogue.remove()
                uiInit(resultsheet)
                getSubjects(resultsheet)
                sendUpdate(resultsheet, token)
                
        })
        cancelbtn.addEventListener('click', () => {
            dialogue.remove()
        })

    }
    updateStudent(id, token) {
        document.getElementById('body').innerHTML = document.getElementById('body').innerHTML + `
        <div class="dialogue-place" style="display:none" id="update-dialogue">
        <div class="dialogue-box d-update" >
            <b class="dialogue-title">Update Student Information</b>
            <p class="m-0-c">This Update will only affect {{result_info.name}}.</p>
            <input type="text" placeholder="Update Name" id="student-name-update">
            <div class="dialogue-actions">
                <button class="cancel-button" id="cancel-update-btn-dialogue">cancel</button>
                <button class="update-btn"  id="update-btn-dialogue">Update</button>
            </div>
        </div>
</div>
        `
        var dialogue = document.getElementById('update-dialogue')
        var yessbtn = document.getElementById('update-btn-dialogue')
        var cancelbtn = document.getElementById('cancel-update-btn-dialogue')
        var text = document.getElementById('student-name-update')
        this.results.forEach(ele => {
            if (ele.student.id == id) {
                text.value = ele.student.name
            }
        })
        dialogue.style.display = '';
        yessbtn.addEventListener('click', () => {
            this.results.forEach(ele => {
                if (ele.student.id == id) {
                    ele.student.name = text.value

                }
                dialogue.remove()
                uiInit(this)
                getSubjects(this)
                sendUpdate(this, token)

            })
        })
        cancelbtn.addEventListener('click', () => {
            dialogue.remove()
        })

    }

    addStudent(students, token) {
        
        document.getElementById('body').innerHTML = document.getElementById('body').innerHTML + `
        <div class="dialogue-place" style="display:none" id="add-student-dialogue">
        <div class="dialogue-box d-update" >
            <b class="dialogue-title">Add Student</b>
            <p class="m-0-c">Register a new student from <a style="color:#56fc09" href="/register/student/">here</a> And then select</p>
            <select id="student-add-select"></select>
            <div class="dialogue-actions">
                <button class="cancel-button" id="cancel-add-btn-dialogue">cancel</button>
                <button class="update-btn"  id="add-btn-dialogue">Add</button>
            </div>
        </div>
     </div>
        `
        var listofst = []
        students.forEach(student => {
            var should = true;
            this.results.forEach(result => {
                if (student.id.toString() == result.student.id.toString()) {

                    should = false;
                }
            })
            if (should) {
                listofst.push(student)
            }
           
        })

        var dialogue = document.getElementById('add-student-dialogue')
        var yessbtn = document.getElementById('add-btn-dialogue')
        var cancelbtn = document.getElementById('cancel-add-btn-dialogue')
        var docs = document.getElementById('student-add-select')

        dialogue.style.display = '';
        var def = document.createElement('option')
        def.innerText = "Select Student";
        docs.appendChild(def)
        listofst.forEach(st => {
            var option = document.createElement('option')
            option.value = st.id
            option.innerText = st.name + ' (Roll No: ' + st.rollno+')'
            docs.appendChild(option)
        })

        yessbtn.addEventListener('click', () => {
            var selectedst = null;
            listofst.forEach(st => {
                if (st.id.toString() == docs.value.toString()) {
                    selectedst = st;
                }

                
            })
            
            if (selectedst) {
                var result = new Result()
                result.init(selectedst, this.subjects)
                this.results.push(result)
                uiInit(this)
                getSubjects(this)
                sendUpdate(this, token)

                dialogue.remove()
            }


        })
        cancelbtn.addEventListener('click', () => {
            dialogue.style.display = 'none';
            docs.innerHTML = ''
            dialogue.remove()
        })






    }


}



class Result {
    student = new Student()
    marks = []
    init(student, subjects) {
        this.student = student;
        subjects.forEach(element => {
            this.addMarks(element)
        });
    }

    initinstance(data) {
        var student = new Student()
        student.init(data['student']['name'], data['student']['rollno'], data['student']['id'], data['student']['section'])
        console.log(typeof data['student']['id'])
        this.student = student
        data['marks'].forEach(mark => {
            var mark_new = new Marks()
            var subject = new Subject()
            subject.init(mark['subject']['name'], mark['subject']['full_marks'], mark['subject']['pass_marks'], mark['subject']['practical_marks'], mark['subject']['practical_pass_marks'], mark['subject']['theory_marks'], mark['subject']['theory_pass_marks'], mark['subject']['id'])
            mark_new.init(subject, mark['theory'], mark['practical'], mark['student'])
            this.marks.push(mark_new)
        })
    }
    addMarks(subject) {
        var mark = new Marks()
        mark.init(subject, '', '', this.student)
        this.marks.push(mark)
    }

    deleteMarks(id) {
        this.marks.forEach(ele => {
            if (ele.subject.id == id) {
                this.marks = arrayRemove(this.marks, ele)
            }
        })
    }


    widget() {
        var elementsfiled = ''
        this.marks.forEach(field => {
            elementsfiled = elementsfiled + field.widget()
        })
        return `
        <div class="result-card" section="${this.student.section}" search-helper-name="${this.student.name}" search-helper-rollno="${this.student.rollno}">
                <div class="student-info">
                    <b>Obtained</b>
                    <span>${this.student.name}</span>
                    <span>Roll no: ${this.student.rollno}</span>
                </div>
                <div class="marks-type">
                    <b>TH</b>
                    <b>PR</b>
                </div>
                <div class="marks-entry" id="marks-entry">
                    ${elementsfiled}
                </div>
                <div class="totalsubjects updateDate">
                    <button onclick="updateStudent(${this.student.id})">Update Student</button>
                    <button onclick="deleteStudent(${this.student.id})">Delete Student</button>
                </div>
        </div>
        `
    }


}

class Student {
    init(name, rollno, id, section) {
        this.name = name;
        this.rollno = rollno;
        this.id = id;
        this.section = section
    }
}

class Subject {
    init(name, full_marks, pass_marks, practical_marks, practical_pass_marks, theory_marks, theory_pass_marks, id) {
        this.name = name;
        this.full_marks = full_marks;
        this.pass_marks = pass_marks;
        this.practical_marks = practical_marks;
        this.theory_marks = theory_marks;
        this.id = id;
        this.practical_pass_marks = practical_pass_marks;
        this.theory_pass_marks = theory_pass_marks;
    }

    widget() {
        return `
            <div class="subject-card">
                <b>${this.name}</b>
                <span>TH: ${this.theory_marks}</span>
                <span>PR: ${this.practical_marks}</span>
            </div>
        
        
        `
    }
}

class Marks {
    subject = new Subject()
    init(subject, theory, practical, student) {
        this.subject = subject;
        this.theory = theory;
        this.practical = practical
        this.student = student
    }

    widget() {
        var theory_border_color =  this.theory == '' ? '2px solid white' : this.subject.theory_pass_marks > this.theory ? '2px solid red' : this.subject.theory_marks == this.theory ? '2px solid #90EE90' : '2px solid white'
        var practical_border_color = this.practical == '' ? '2px solid white':this.subject.practical_pass_marks > this.practical ? '2px solid red' : this.subject.practical_marks == this.practical ? '2px solid #90EE90' : '2px solid white'
        return `
        <div class="number-chip">
            <input type="number" placeholder="TH" max="${this.subject.theory_marks}" pass-marks-should="${this.subject.theory_pass_marks}" style="border:${theory_border_color}"  onchange="checknubervalidity(this); onupdate(${this.student.id}, ${this.subject.id}, this.value, 'th');" value=${this.theory}>
            <input type="number" placeholder="PR" max="${this.subject.practical_marks}" pass-marks-should="${this.subject.practical_pass_marks}" style="border:${practical_border_color}"   onchange="checknubervalidity(this); onupdate(${this.student.id}, ${this.subject.id}, this.value, 'pr');" value=${this.practical}>
        </div>
        `
    }
}

function arrayRemove(arr, value) {

    return arr.filter(function (ele) {
        return ele != value;
    });
}

function array_move(arr, old_index, new_index) {
    if (new_index >= arr.length) {
        var k = new_index - arr.length + 1;
        while (k--) {
            arr.push(undefined);
        }
    }
    arr.splice(new_index, 0, arr.splice(old_index, 1)[0]);
    return arr; // for testing
};
