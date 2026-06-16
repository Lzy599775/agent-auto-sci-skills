$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

$patterns = @(
  "(?i)(api[_-]?key|secret|token|password|cookie)\s*[:=]\s*['""]?[A-Za-z0-9_\-]{12,}",
  "BEGIN RSA PRIVATE KEY",
  "BEGIN OPENSSH PRIVATE KEY",
  "C:\\Users\\LI ZEYANG",
  "F:\\A_",
  "F:/A_",
  "manual_download_nonOA_pdfs"
)

$hits = @()
$allowedFalsePositiveText = @(
  'api_key="YOUR_API_KEY",',
  'api_key=YOUR_API_KEY',
  '&api_key=YOUR_API_KEY_HERE',
  'export NCBI_API_KEY="your_key_here"',
  'print("  export OPENROUTER_API_KEY=''your_api_key''")',
  "print(""  export OPENROUTER_API_KEY='your_api_key'"")",
  "export OPENROUTER_API_KEY='your_api_key_here'",
  'api_key="your_openrouter_key",',
  "export OPENROUTER_API_KEY='sk-or-v1-your_key_here'",
  'echo ''export OPENROUTER_API_KEY="sk-or-v1-your_key"'' >> ~/.bashrc  # or ~/.zshrc',
  "export OPENROUTER_API_KEY='your_api_key_here'",
  'api_key = check_env_file()',
  'print("OPENROUTER_API_KEY=your-api-key-here")',
  'print("export OPENROUTER_API_KEY=your-api-key-here")',
  'FLAG_TOKEN = "ARS_PASSPORT_RESET"',
  'PROTOCOL_TOKEN = "passport_as_reset_boundary"',
  'token = _annotation_match_token(literal)',
  'suite_version, invalid_suite_token = _parse_suite_version(claude_text)'
)
$gitFiles = git -C $Root -c core.quotePath=false ls-files --cached --others --exclude-standard 2>$null
if ($LASTEXITCODE -eq 0 -and $gitFiles) {
  $files = foreach ($relativePath in $gitFiles) {
    $fullPath = Join-Path $Root $relativePath
    if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
      Get-Item -LiteralPath $fullPath
    }
  }
}
else {
  $files = Get-ChildItem -Path $Root -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch "\\.git\\" -and
    $_.FullName -notmatch "\\_local\\" -and
    $_.FullName -notmatch "\\archives\\" -and
    $_.FullName -notmatch "\\external_repos\\" -and
    $_.FullName -notmatch "\\incoming\\" -and
    $_.FullName -notmatch "\\inventory\\" -and
    $_.FullName -notmatch "\\unpackaged\\"
  }
}

$files = $files | Where-Object {
  $_.FullName -ne $PSCommandPath -and
  $_.Extension -notin @(".png", ".jpg", ".jpeg", ".gif", ".ico")
}

foreach ($pattern in $patterns) {
  foreach ($file in $files) {
    $matches = Select-String -Path $file.FullName -Pattern $pattern -CaseSensitive:$false -ErrorAction SilentlyContinue
    foreach ($m in $matches) {
      if ($allowedFalsePositiveText -contains $m.Line.Trim()) {
        continue
      }
      $hits += [PSCustomObject]@{
        Pattern = $pattern
        Path = $m.Path
        Line = $m.LineNumber
        Text = $m.Line.Trim()
      }
    }
  }
}

if ($hits.Count -gt 0) {
  $hits | Format-Table -AutoSize
  throw "Potential public-safety issues found. Review the hits above."
}

Write-Host "No obvious public-safety issues found."
