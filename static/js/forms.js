
var school = FieldSelect('id_school','form')
school.remove()
var is_active = FieldSelect('id_is_active','form')
is_active.remove()

var user = FieldSelect('id_user','form')
user.remove()

var student_dob = FieldSelect('id_student_dob','form')
if(student_dob != null){
    student_dob.setAttribute('type', 'date')
}

var student_dob = FieldSelect('id_student_dob','form')
if(student_dob != null){
    student_dob.childNodes.forEach(ele=>{
        if(ele.nodeName == 'INPUT' && ele.getAttribute('type') != 'hidden'){
            ele.setAttribute('type', 'date')
        }
    })
}

var grade = document.getElementById('id_grade')
filterSection(grade)
grade.setAttribute('onchange', 'filterSection(this)')
if(grade != null){
    grade.childNodes.forEach(
        ele=>{
            if(ele.nodeName == 'OPTION'){
                ele.setAttribute('onclick', 'filterSection(this.value)')
            }
        }
    )
}

function FieldSelect(id, parent_id) {
    var form = document.getElementById(parent_id); 
    var ele;
    form.childNodes.forEach(elementParent => {
        elementParent.childNodes.forEach(element=>{
            if (element.id == id) {
                ele = elementParent;
            }
        })
       
    });
    return ele;
}


function filterSection(grade){
    var section = document.getElementById('id_section')
    var child = document.createElement('option');
    child.innerHTML = '---------';
    child.setAttribute('selected', '');
    section.replaceChildren();
    section.appendChild(child)
    fetch(`/sections/${grade.value}/`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
        
    }) .then((response) => response.json())
    .then((data) => {
      console.log(data)
        
        data.forEach(ele=>{
            var child = document.createElement('option');
            child.value = ele['id']
            child.innerHTML = ele['name']
            section.appendChild(child)
        })
    });
}