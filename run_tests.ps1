# Activate the virtual environment
& ".\.venv\Scripts\Activate.ps1"

# Run pytest
pytest

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ All tests passed!"
    exit 0
} else {
    Write-Host "❌ Some tests failed!"
    exit 1
}
