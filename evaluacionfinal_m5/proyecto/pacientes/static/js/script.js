function validar_sesion() {

    var correo = document.getElementById("persona_correo").value;
    var pass = document.getElementById("persona_pass").value;
    if ((correo == "jccabellog@gmail.com") && (pass == "123456")) {
        window.location.href = "../templates/pacientes.html";
    } else if ((correo == "acarvajalh1@gmail.com") && (pass == "123456")) {
        window.location.href = "../templates/pacientes.html";
    } else if ((correo == "javiera@gmail.com") && (pass == "123456")) {
        window.location.href = "../templates/pacientes.html";
    } else {
        alert("Usuario o contraseña no válidos, favor reintentar");
    }
}

function agregar() {

    var fecha = document.getElementById("fecha").value;
    var diagnostico = document.getElementById("diagnostico").value;
    var tratamiento = document.getElementById("tratamiento").value;
    var control = document.getElementById("control").value;
    var comentario = document.getElementById("comentario").value;

    $('#tabla1').append('<tr><th scope=row>' + fecha + '</th><td scope=row>' + diagnostico + '</td><td scope=row>' + tratamiento + '</td><td scope=row>' + control + '</td><td scope=row>' + comentario + '</td></tr>');
    alert("Gracias, su tratamiento se ha agregado correctamente");
}

function agregar_consulta() {

    var fecha_consulta = document.getElementById("fecha_consulta").value;
    var especialidad = document.getElementById("especialidad").value;
    var medico = document.getElementById("medico").value;
    var prevision = document.getElementById("prevision").value;
    var consulta = document.getElementById("consulta").value;

    $('#tabla1').append('<tr><th scope=row>' + fecha_consulta + '</th><td scope=row>' + especialidad + '</td><td scope=row>' + medico + '</td><td scope=row>' + prevision + '</td><td scope=row>' + consulta + '</td></tr>');
    alert("Gracias, su hora se ha agendado correctamente");
}

function agregar_examen() {
    var fecha_examen = document.getElementById("fecha_examen").value;
    var tipo = document.getElementById("tipo").value;
    var nombre_examen = document.getElementById("nombre_examen").value;
    var resultado = document.getElementById("resultado").value;
    var normal = document.getElementById("normal").value;

    $('#tabla1').append('<tr><th scope=row>' + fecha_examen + '</th><td scope=row>' + tipo + '</td><td scope=row>' + nombre_examen + '</td><td scope=row>' + resultado + '</td><td scope=row>' + normal + '</td></tr>');
    alert("Gracias, su examen se ha agregado correctamente");
}

function registrar() {
    alert("Usuario registrado correctamente.");
}

function ver_historial() {
    window.location.href = "paciente_tratamiento.html";
}