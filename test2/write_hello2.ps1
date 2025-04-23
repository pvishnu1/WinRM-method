# write_hello2.ps1

$path = "C:\deploy\hello.txt"
$content = "Hello from Github2!"
New-Item -ItemType File -Path $path -Force | Out-Null
Set-Content -Path $path -Value $content
Write-Host "File written to $path"
