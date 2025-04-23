# write_hello.ps1

$path = "C:\deploy\hello.txt"
$content = "Hello from Github!"
New-Item -ItemType File -Path $path -Force | Out-Null
Set-Content -Path $path -Value $content
Write-Host "File written to $path"
