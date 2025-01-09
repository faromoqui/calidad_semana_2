# Ruta al directorio de tests
$TEST_DIR = "test"

# Ejecuta los tests con unittest
Write-Host "Ejecutando tests en la carpeta '$TEST_DIR'..."
python -m unittest discover -s $TEST_DIR

# Verifica si los tests pasaron
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Tests fallaron. Cancela el commit."
    exit 1
} else {
    Write-Host "✅ Todos los tests pasaron. Procediendo con el commit."
}