<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imprimir Nombre</title>
    <script>
        // Función que imprime el nombre en el elemento con id "nombreCompleto"
        function imprimirNombre() {
            document.getElementById("nombreCompleto").innerText = "Juan Milliano";
        }
    </script>
</head>
<body onload="imprimirNombre()">
    <h1>Nombre y Apellido:</h1>
    <p id="nombreCompleto"></p> <!-- Aquí se imprimirá el nombre -->
</body>
</html>
