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
Copy-Item -Path (Join-Path $SkillDir "*") -Destination $Target -Recurse -Force

Write-Host "Installed skills to $Target"
Write-Host "Restart Codex to refresh the skill list."
