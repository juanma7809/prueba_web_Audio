// Nope. This is a concept design, so no menu or filter toggles work. But it looks good, doesn't it?
function modificarCuenta() {
    document.getElementById('modificar').addEventListener('click', function() {
        var parametros = new URLSearchParams(window.location.search);

    // Obtener el valor de un parámetro específico
        var id = parametros.get('id');
        var rol = parametros.get('rol');
        var url = "{% url '/profile/' %}?id=" + id + "&rol=" + rol;
        window.location.href = url;
    });
}