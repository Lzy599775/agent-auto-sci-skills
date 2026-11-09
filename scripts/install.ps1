param(
  [string]$Target = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$SkillDir = Join-Path $Root "skills"

if (!(Test-Path $SkillDir)) {
  throw "skills directory not found: $SkillDir"
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null
Get-ChildItem -LiteralPath $SkillDir -Directory | Where-Object {
  Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md")
} | ForEach-Object {
  Copy-Item -LiteralPath $_.FullName -Destination $Target -Recurse -Force
}

Write-Host "Installed skills to $Target"
Write-Host "Restart Codex to refresh the skill list."
