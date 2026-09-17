$ErrorActionPreference = "Stop"

chcp 65001 > $null
$utf8_encoding = New-Object System.Text.UTF8Encoding($false)
[Console]::InputEncoding = [Console]::OutputEncoding = $OutputEncoding = $utf8_encoding

$base_path = Get-Location

$escape = [char]27
$bold = "$escape[1m"
${/bold} = "$escape[22m"
$italic = "$escape[3m"
${/italic} = "$escape[23m"
$reset_style = "$escape[0m"

function separator {
    $width = $Host.UI.RawUI.WindowSize.Width
    if ($null -eq $width) { $width = 125 }
    $separator = "${bold}/" + ("-" * ($width - 3)) + "/${reset_style}"
    Write-Host $separator -ForegroundColor White
}

function main {
    $total_start_time = Get-Date
    Write-Host "${bold}${italic}Comenzando proceso de publicación y actualización...${reset_style}" -ForegroundColor White
    separator
    clean_pycache_folders
    build_package
    upload_library_to_pypi
    delete_temporary_files
    update_library
    finish $total_start_time
}

function clean_pycache_folders {
    Write-Host "${bold}${italic}[1/5]${/italic} Eliminando carpetas temporales...${reset_style}" -ForegroundColor White
    $current_step_start_time = Get-Date
    $folders_to_delete = @()
    Get-ChildItem -Path $base_path -Filter "__pycache__" -Directory -Recurse | ForEach-Object { $folders_to_delete += $_.FullName }
    Get-ChildItem -Path $base_path -Filter ".pytest_cache" -Directory -Recurse | ForEach-Object { $folders_to_delete += $_.FullName }
    $folders_to_delete | ForEach-Object { if (Test-Path $_) { Remove-Item -Path $_ -Recurse -Force -ErrorAction SilentlyContinue } }
    $duration = (Get-Date) - $current_step_start_time
    Write-Host "${bold}Carpetas temporales eliminadas en:${/bold} $($duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
    separator
}

function build_package {
    Write-Host "${bold}${italic}[2/5]${/italic} Construyendo paquete...${reset_style}" -ForegroundColor White
    $current_step_start_time = Get-Date
    python -m build
    $duration = (Get-Date) - $current_step_start_time
    Write-Host "${bold}Paquete construido en:${/bold} $($duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
    separator
}

function upload_library_to_pypi {
    Write-Host "${bold}${italic}[3/5]${/italic} Subiendo la librería a PyPI...${reset_style}" -ForegroundColor White
    $current_step_start_time = Get-Date
    twine upload dist/*
    $duration = (Get-Date) - $current_step_start_time
    Write-Host "${bold}Librería subida a PyPI en:${/bold} $($duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
    separator
}

function delete_temporary_files {
    Write-Host "${bold}${italic}[4/5]${/italic} Eliminando archivos residuales...${reset_style}" -ForegroundColor White
    $current_step_start_time = Get-Date
    $folders_to_delete = @("dist", "build")
    Get-ChildItem -Path $base_path -Filter "*.egg-info" -Directory | ForEach-Object { $folders_to_delete += $_.FullName }
    $folders_to_delete | ForEach-Object { if (Test-Path $_) { Remove-Item -Path $_ -Recurse -Force -ErrorAction SilentlyContinue } }
    $duration = (Get-Date) - $current_step_start_time
    Write-Host "${bold}Archivos residuales eliminados en:${/bold} $($duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
    separator
}

function update_library {
    Write-Host "${bold}${italic}[5/5]${/italic} Actualizando librería localmente...${reset_style}" -ForegroundColor White
    $current_step_start_time = Get-Date
    pip install -U advanced_automation_utilities
    pip install -U advanced_automation_utilities
    $duration = (Get-Date) - $current_step_start_time
    Write-Host "${bold}Librería actualizada en:${/bold} $($duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
    separator
}

function finish($total_start_time) {
    $total_duration = (Get-Date) - $total_start_time
    Write-Host "${bold}Proceso de publicación y actualización completado con éxito en:${/bold} $($total_duration.TotalMilliseconds.ToString("N0", [cultureinfo]::GetCultureInfo("es-ES")))ms${reset_style}" -ForegroundColor Green
}

main