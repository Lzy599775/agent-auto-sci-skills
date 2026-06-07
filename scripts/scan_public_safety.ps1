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
  'FLAG_TOKEN = "ARS_PASSPORT_RESET"',
  'PROTOCOL_TOKEN = "passport_as_reset_boundary"',
  'token = _annotation_match_token(literal)',
  'suite_version, invalid_suite_token = _parse_suite_version(claude_text)'
)
$files = Get-ChildItem -Path $Root -Recurse -File | Where-Object {
  $_.FullName -notmatch "\\.git\\" -and
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
