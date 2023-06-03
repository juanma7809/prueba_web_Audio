const btn = document.getElementById('btn--hamburguesa');
const menu = document.getElementById('menu');
const logout = document.getElementById('navbar--logout');



function abrirForm(idForm){
    localStorage.setItem("idForm", JSON.stringify(idForm));
    window.location.replace("pacientes-form.html");
}

function eliminarItem(idItem, activo){

    var parametros = new URLSearchParams(window.location.search);

    // Obtener el valor de un parámetro específico
    var id = parametros.get('id');
    var rol = parametros.get('rol');
    var url = "/habilitar-deshabilitar-paciente/?id=" + id + "&rol=" + rol + "&id_usu=" + idItem + "&activo=" + activo;
    window.location.href = url;
}

function volver() {
    var parametros = new URLSearchParams(window.location.search);

    // Obtener el valor de un parámetro específico
    var id = parametros.get('id');
    var rol = parametros.get('rol');
    var url = "/dashboard/?id=" + id + "&rol=" + rol;
    window.location.href = url;

}

function editarPerfil(idItem){

    var parametros = new URLSearchParams(window.location.search);

    // Obtener el valor de un parámetro específico
    var id = parametros.get('id');
    var rol = parametros.get('rol');
    var url = "/editar_perfil/?id=" + id + "&rol=" + rol + "&id_usu=" + idItem;
    window.location.href = url;
}

function diagnosticar(idItem) {
    var parametros = new URLSearchParams(window.location.search);

    // Obtener el valor de un parámetro específico
    var id = parametros.get('id');
    var rol = parametros.get('rol');
    var url = "/diagnostico_paciente/?id=" + id + "&rol=" + rol + "&id_usu=" + idItem;
    window.location.href = url;

}

function doSearch()

{


    const tableReg = document.getElementById('tablaPacientes');

    const searchText = document.getElementById('searchTerm').value.toLowerCase();

    let total = 0;



    // Recorremos todas las filas con contenido de la tabla

    for (let i = 1; i < tableReg.rows.length; i++) {

        // Si el td tiene la clase "noSearch" no se busca en su cntenido

        if (tableReg.rows[i].classList.contains("noSearch")) {

            continue;

        }



        let found = false;

        const cellsOfRow = tableReg.rows[i].getElementsByTagName('td');

        // Recorremos todas las celdas

        for (let j = 0; j < cellsOfRow.length && !found; j++) {

            const compareWith = cellsOfRow[j].innerHTML.toLowerCase();

            // Buscamos el texto en el contenido de la celda

            if (searchText.length == 0 || compareWith.indexOf(searchText) > -1) {

                found = true;

                total++;

            }

        }

        if (found) {

            tableReg.rows[i].style.display = '';

        } else {

            // si no ha encontrado ninguna coincidencia, esconde la

            // fila de la tabla

            tableReg.rows[i].style.display = 'none';

        }

    }



    // mostramos las coincidencias

    const lastTR=tableReg.rows[tableReg.rows.length-1];

    const td=lastTR.querySelector("td");

    lastTR.classList.remove("hide", "red");

    if (searchText == "") {

        lastTR.classList.add("hide");

    } else if (total) {

        

    } else {

        lastTR.classList.add("red");

       

    }

}