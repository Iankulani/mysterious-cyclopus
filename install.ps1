<#
.SYNOPSIS
    🐙 Mysterious Cyclopus - PowerShell Installer
.DESCRIPTION
    Installs Python, dependencies, and sets up the Cyclopus environment.
.PARAMETER SkipSystemTools
    Skip installing system tools via winget.
.PARAMETER Verbose
    Print extra output.
#>
[CmdletBinding()]
param(
    [switch]$SkipSystemTools,
    [switch]$ForceRecreate
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

# ---------- Helpers ----------
function Write-Banner {
    Write-Host ""
    Write-Host "   __  ___               __                        __"       -ForegroundColor DarkYellow
    Write-Host "  /  |/  /_  _____  ___ / /____ ___   ___  ___ ___/ /  __ __ ___" -ForegroundColor DarkYellow
    Write-Host " / /|_/ / / / / _ \/ _ / __/ -_) _ \ / _ \/ -_) _  /  / // /(_-<" -ForegroundColor DarkYellow
    Write-Host "/_/  /_/_/ /_/\___/_/ /_/\__/\___/ /_//_/\__/\_,_/   \_,_//___/" -ForegroundColor DarkYellow
    Write-Host ""
    Write-Host "        🐙 MYSTERIOUS CYCLOPUS v1.0.0 - Installer 🐙" -ForegroundColor Yellow
    Write-Host ""
}

function Write-Step  ($m) { Write-Host "[*] $m" -ForegroundColor Cyan }
function Write-Ok    ($m) { Write-Host "[✓] $m" -ForegroundColor Green }
function Write-Warn  ($m) { Write-Host "[!] $m" -ForegroundColor Yellow }
function Write-Fail  ($m) { Write-Host "[✗] $m" -ForegroundColor Red }

# ---------- Paths ----------
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VenvDir    = Join-Path $ProjectDir ".venv"
$PyExe      = Join-Path $VenvDir "Scripts\python.exe"
$PipExe     = Join-Path $VenvDir "Scripts\pip.exe"

# ---------- Elevate if admin needed ----------
$IsAdmin = ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# ---------- Check Python ----------
function Find-Python {
    Write-Step "Locating Python 3..."
    foreach ($c in @("python", "python3", "py")) {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if ($cmd) {
            try {
                $ver = & $c --version 2>&1
                if ($ver -match "Python 3\.(\d+)" -and [int]$Matches[1] -ge 7) {
                    Write-Ok "Found $ver at $($cmd.Source)"
                    return $cmd.Source
                }
            } catch { }
        }
    }

    Write-Warn "Python 3.7+ not found."
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        $ans = Read-Host "Install Python via winget now? (y/n)"
        if ($ans -eq "y") {
            winget install -e --id Python.Python.3.12 `
                --accept-source-agreements --accept-package-agreements
            $env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
                        [Environment]::GetEnvironmentVariable("Path","User")
            return (Get-Command python -ErrorAction Stop).Source
        }
    }
    throw "Python 3.7+ is required."
}

# ---------- Install system tools ----------
function Install-SystemTools {
    if ($SkipSystemTools) { Write-Warn "Skipping system tools."; return }
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        Write-Warn "winget not available — install Nmap/Wireshark manually."
        return
    }

    Write-Step "Installing system tools (Nmap, Wireshark, Git) via winget..."
    $packages = @(
        @{ Id = "Insecure.Nmap";       Name = "Nmap" },
        @{ Id = "Wireshark.Wireshark"; Name = "Wireshark" },
        @{ Id = "Git.Git";             Name = "Git" }
    )
    foreach ($p in $packages) {
        Write-Host "  -> $($p.Name)" -ForegroundColor DarkGray
        try {
            winget install -e --id $p.Id --silent `
                --accept-source-agreements --accept-package-agreements
            Write-Ok "$($p.Name) installed."
        } catch {
            Write-Warn "$($p.Name) failed: $_"
        }
    }
}

# ---------- Create venv ----------
function New-Venv ($py) {
    if ((Test-Path $VenvDir) -and $ForceRecreate) {
        Write-Warn "Removing existing venv (ForceRecreate)..."
        Remove-Item -Recurse -Force $VenvDir
    }
    if (-not (Test-Path $VenvDir)) {
        Write-Step "Creating virtual environment..."
        & $py -m venv $VenvDir
        Write-Ok "Virtual environment created at $VenvDir"
    } else {
        Write-Warn "Virtual environment already exists."
    }
}

# ---------- Install Python deps ----------
function Install-PythonDeps {
    Write-Step "Upgrading pip..."
    & $PyExe -m pip install --upgrade pip setuptools wheel | Out-Null

    $req = Join-Path $ProjectDir "requirements.txt"
    if (-not (Test-Path $req)) { throw "requirements.txt not found." }

    Write-Step "Installing Python requirements (this may take a while)..."
    & $PyExe -m pip install -r $req
    Write-Ok "Python requirements installed."
}

# ---------- Self check ----------
function Invoke-SelfCheck {
    $chk = Join-Path $ProjectDir "requirements-check.py"
    if (Test-Path $chk) {
        Write-Step "Running requirements self-check..."
        & $PyExe $chk -v
    }
}

# ---------- Create launcher ----------
function New-Launcher {
    $launcher = Join-Path $ProjectDir "run.ps1"
    @"
# Auto-generated launcher
Set-Location "$ProjectDir"
& "$PyExe" "$ProjectDir\mysterious_cyclopus.py" @args
"@ | Out-File -Encoding UTF8 $launcher

    $bat = Join-Path $ProjectDir "run.bat"
    @"
@echo off
cd /d "$ProjectDir"
"$PyExe" "$ProjectDir\mysterious_cyclopus.py" %*
"@ | Out-File -Encoding ASCII $bat

    Write-Ok "Launchers: run.ps1, run.bat"
}

# ---------- Firewall hint ----------
function Show-FirewallHint {
    if (-not $IsAdmin) {
        Write-Warn "Run as Administrator to enable firewall rules for blocking IPs."
    }
}

# ---------- Main ----------
try {
    Write-Banner
    $py = Find-Python
    Install-SystemTools
    New-Venv $py
    Install-PythonDeps
    Invoke-SelfCheck
    New-Launcher
    Show-FirewallHint

    Write-Host ""
    Write-Host "============================================================" -ForegroundColor DarkYellow
    Write-Host " ✅ Installation complete!" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor DarkYellow
    Write-Host " To run:" -ForegroundColor White
    Write-Host "   .\run.ps1" -ForegroundColor DarkYellow
    Write-Host " or:" -ForegroundColor White
    Write-Host "   .\.venv\Scripts\Activate.ps1" -ForegroundColor DarkYellow
    Write-Host "   python mysterious_cyclopus.py" -ForegroundColor DarkYellow
    Write-Host ""
} catch {
    Write-Fail "Installation failed: $_"
    exit 1
}