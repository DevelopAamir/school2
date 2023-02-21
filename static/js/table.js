function filter(id, table, col) {
    var tableElement = document.getElementById(table)
    var btn = document.getElementById(id)
    tableElement.childNodes.forEach((elem) => {

        if (elem.nodeName == 'TR') {
            elem.childNodes.forEach(element => {

                if (element.id == col) {
                  
                    if (element.innerHTML.toString().trim() != btn.innerHTML.toString().trim()) {
                       
                        elem.style.display = 'none';
                    } else {
                        elem.style.display = '';
                    }
                }
            });
        }
    })
}

function search(query, table){
    var tableElement = document.getElementById(table)

    tableElement.childNodes.forEach((elem) => {

        if (elem.nodeName == 'TR') {
            torv = true;
            elem.childNodes.forEach(element => {

                if (element.nodeName == 'TD') {
                  
                    if (element.innerHTML.toString().trim().toLowerCase().includes(query.toLowerCase().trim())) {
                       torv = false;
                       
                    } 
                }
            });
            if(torv){
                elem.style.display = 'none';
            }else{
                elem.style.display = '';
            }
        }
    })
}