#!/usr/bin/env python3
"""
🐙 MYSTERIOUS CYCLOPUS - Dependency & Requirements Checker
Verifies all required and optional dependencies are properly installed.
"""

import sys
import os
import subprocess
import importlib
import platform
import shutil
import argparse
from typing import Dict, List, Tuple

# ============================================================
# ANSI Colors
# ============================================================
class C:
    ORANGE = "\033[38;5;214m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @staticmethod
    def disable():
        for attr in ["ORANGE", "WHITE", "GREEN", "YELLOW", "RED", "CYAN", "BOLD", "RESET"]:
            setattr(C, attr, "")


if os.name == "nt" and not os.environ.get("WT_SESSION"):
    try:
        import colorama
        colorama.init()
    except ImportError:
        C.disable()

# ============================================================
# Dependency Definitions
# ============================================================
REQUIRED_PYTHON = (3, 7)

# (import_name, pip_name, description, is_required)
PYTHON_PACKAGES: List[Tuple[str, str, str, bool]] = [
    # Core
    ("psutil", "psutil", "System monitoring", True),
    ("colorama", "colorama", "Terminal colors", True),
    ("requests", "requests", "HTTP client", True),
    ("dotenv", "python-dotenv", "Environment config", False),

    # Security
    ("cryptography", "cryptography", "Cryptography primitives", True),
    ("paramiko", "paramiko", "SSH client", True),
    ("scapy", "scapy", "Packet manipulation", True),
    ("dns", "dnspython", "DNS resolution", True),
    ("whois", "python-whois", "WHOIS lookups", False),

    # Web
    ("flask", "flask", "Web framework", True),
    ("flask_socketio", "flask-socketio", "WebSocket support", True),
    ("flask_cors", "flask-cors", "CORS support", True),
    ("socketio", "python-socketio", "Socket.IO", False),
    ("eventlet", "eventlet", "Async networking", False),

    # Bots
    ("discord", "discord.py", "Discord bot", False),
    ("telethon", "telethon", "Telegram bot", False),
    ("slack_sdk", "slack-sdk", "Slack bot", False),
    ("selenium", "selenium", "WhatsApp automation", False),
    ("webdriver_manager", "webdriver-manager", "Chrome driver", False),
    ("google.oauth2", "google-auth", "Google auth", False),
    ("googleapiclient", "google-api-python-client", "Google Chat", False),

    # Keylogger
    ("pynput", "pynput", "Keyboard listener", False),
    ("pyperclip", "pyperclip", "Clipboard access", False),
    ("pyautogui", "pyautogui", "Screenshots/automation", False),

    # Data / Reports
    ("numpy", "numpy", "Numerical computing", False),
    ("matplotlib", "matplotlib", "Charts", False),
    ("seaborn", "seaborn", "Statistical charts", False),
    ("bs4", "beautifulsoup4", "HTML parsing", False),
    ("pandas", "pandas", "Data analysis", False),
    ("reportlab", "reportlab", "PDF generation", False),
    ("PIL", "Pillow", "Image processing", False),
    ("qrcode", "qrcode", "QR codes", False),
    ("pyshorteners", "pyshorteners", "URL shortening", False),

    # Utils
    ("tabulate", "tabulate", "Table formatting", False),
    ("tqdm", "tqdm", "Progress bars", False),
    ("dateutil", "python-dateutil", "Date utilities", False),
    ("sqlalchemy", "sqlalchemy", "ORM", False),
    ("netaddr", "netaddr", "Network address manipulation", False),
]

# External system binaries: (binary, description, is_required)
SYSTEM_TOOLS: List[Tuple[str, str, bool]] = [
    ("ping", "ICMP ping utility", True),
    ("nmap", "Network mapper", True),
    ("curl", "HTTP client", True),
    ("wget", "File downloader", True),
    ("dig", "DNS lookup", False),
    ("nslookup", "DNS lookup (Windows)", False),
    ("host", "DNS lookup", False),
    ("traceroute", "Path tracing", False),
    ("tracert", "Path tracing (Windows)", False),
    ("nc", "Netcat", False),
    ("ncat", "Ncat", False),
    ("ssh", "SSH client", True),
    ("nikto", "Web vulnerability scanner", False),
    ("hashcat", "Password cracker", False),
    ("signal-cli", "Signal CLI", False),
    ("docker", "Docker engine", False),
]

# Optional Python builtins
OPTIONAL_MODULES: List[Tuple[str, str]] = [
    ("sqlite3", "SQLite3 database"),
    ("ssl", "SSL/TLS support"),
    ("socket", "Socket support"),
    ("threading", "Threading support"),
    ("subprocess", "Subprocess support"),
]


# ============================================================
# Checker Class
# ============================================================
class RequirementsChecker:
    def __init__(self, verbose: bool = False, json_out: bool = False):
        self.verbose = verbose
        self.json_out = json_out
        self.results = {
            "python": {},
            "packages": {"ok": [], "missing": [], "broken": []},
            "tools": {"ok": [], "missing": []},
            "modules": {"ok": [], "missing": []},
            "summary": {},
        }

    # ---------- Python version ----------
    def check_python(self) -> bool:
        v = sys.version_info
        ok = v >= REQUIRED_PYTHON
        self.results["python"] = {
            "version": f"{v.major}.{v.minor}.{v.micro}",
            "required": f"{REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+",
            "ok": ok,
            "executable": sys.executable,
            "platform": f"{platform.system()} {platform.release()}",
        }

        if not self.json_out:
            print(f"\n{C.ORANGE}{'='*64}{C.RESET}")
            print(f"{C.BOLD}🐙 MYSTERIOUS CYCLOPUS - REQUIREMENTS CHECKER{C.RESET}")
            print(f"{C.ORANGE}{'='*64}{C.RESET}")
            print(f"\n{C.CYAN}🐍 Python Environment{C.RESET}")
            print(f"  Version : {v.major}.{v.minor}.{v.micro} "
                  f"{C.GREEN + '✓ OK' + C.RESET if ok else C.RED + '✗ FAIL' + C.RESET}")
            print(f"  Required: {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+")
            print(f"  Executable: {sys.executable}")
            print(f"  Platform  : {platform.system()} {platform.release()}")
        return ok

    # ---------- Python packages ----------
    def check_package(self, import_name: str, pip_name: str) -> Tuple[bool, str]:
        try:
            mod = importlib.import_module(import_name)
            version = getattr(mod, "__version__", None)
            if version is None:
                try:
                    from importlib.metadata import version as md_version
                    version = md_version(pip_name)
                except Exception:
                    version = "installed"
            return True, str(version)
        except ImportError:
            return False, ""
        except Exception as e:
            return False, f"error: {e}"

    def check_packages(self) -> bool:
        if not self.json_out:
            print(f"\n{C.CYAN}📦 Python Packages{C.RESET}")

        all_required_ok = True
        for import_name, pip_name, desc, is_required in PYTHON_PACKAGES:
            ok, version = self.check_package(import_name, pip_name)

            if ok:
                self.results["packages"]["ok"].append({
                    "import": import_name, "pip": pip_name, "version": version,
                })
                if not self.json_out and (self.verbose or is_required):
                    print(f"  {C.GREEN}✓{C.RESET} {pip_name:<28} {version:<12} {desc}")
            else:
                entry = {
                    "import": import_name, "pip": pip_name,
                    "description": desc, "required": is_required,
                }
                if is_required:
                    all_required_ok = False
                    self.results["packages"]["missing"].append(entry)
                    if not self.json_out:
                        print(f"  {C.RED}✗{C.RESET} {pip_name:<28} {C.RED}MISSING (required){C.RESET}")
                else:
                    self.results["packages"]["broken"].append(entry)
                    if not self.json_out and self.verbose:
                        print(f"  {C.YELLOW}○{C.RESET} {pip_name:<28} {C.YELLOW}missing (optional){C.RESET}")

        return all_required_ok

    # ---------- System binaries ----------
    def check_tools(self) -> bool:
        if not self.json_out:
            print(f"\n{C.CYAN}🛠️  System Tools{C.RESET}")

        all_required_ok = True
        for binary, desc, is_required in SYSTEM_TOOLS:
            path = shutil.which(binary)
            if path:
                self.results["tools"]["ok"].append({"binary": binary, "path": path})
                if not self.json_out and (self.verbose or is_required):
                    print(f"  {C.GREEN}✓{C.RESET} {binary:<14} {desc}")
            else:
                self.results["tools"]["missing"].append({
                    "binary": binary, "description": desc, "required": is_required,
                })
                if is_required:
                    all_required_ok = False
                    if not self.json_out:
                        print(f"  {C.RED}✗{C.RESET} {binary:<14} {C.RED}MISSING (required){C.RESET}")
                else:
                    if not self.json_out and self.verbose:
                        print(f"  {C.YELLOW}○{C.RESET} {binary:<14} {C.YELLOW}not found (optional){C.RESET}")

        return all_required_ok

    # ---------- Builtin modules ----------
    def check_builtin_modules(self) -> bool:
        if not self.json_out:
            print(f"\n{C.CYAN}🧩 Builtin Modules{C.RESET}")

        ok = True
        for module, desc in OPTIONAL_MODULES:
            try:
                importlib.import_module(module)
                self.results["modules"]["ok"].append(module)
                if not self.json_out and self.verbose:
                    print(f"  {C.GREEN}✓{C.RESET} {module:<14} {desc}")
            except ImportError:
                ok = False
                self.results["modules"]["missing"].append(module)
                if not self.json_out:
                    print(f"  {C.RED}✗{C.RESET} {module:<14} {C.RED}MISSING{C.RESET}")
        return ok

    # ---------- Summary ----------
    def summary(self) -> Dict:
        total_pkgs = len(PYTHON_PACKAGES)
        ok_pkgs = len(self.results["packages"]["ok"])
        missing_required = len(self.results["packages"]["missing"])
        missing_optional = len(self.results["packages"]["broken"])

        total_tools = len(SYSTEM_TOOLS)
        ok_tools = len(self.results["tools"]["ok"])
        missing_tools = len(self.results["tools"]["missing"])

        self.results["summary"] = {
            "python_ok": self.results["python"].get("ok", False),
            "packages_total": total_pkgs,
            "packages_ok": ok_pkgs,
            "packages_missing_required": missing_required,
            "packages_missing_optional": missing_optional,
            "tools_total": total_tools,
            "tools_ok": ok_tools,
            "tools_missing": missing_tools,
            "ready": missing_required == 0 and self.results["python"].get("ok", False),
        }
        return self.results["summary"]

    def print_summary(self):
        s = self.results["summary"]
        print(f"\n{C.ORANGE}{'='*64}{C.RESET}")
        print(f"{C.BOLD}📊 SUMMARY{C.RESET}")
        print(f"{C.ORANGE}{'='*64}{C.RESET}")

        py_status = f"{C.GREEN}OK{C.RESET}" if s["python_ok"] else f"{C.RED}FAIL{C.RESET}"
        print(f"  Python        : {py_status} ({self.results['python']['version']})")

        print(f"  Packages      : {s['packages_ok']}/{s['packages_total']} installed "
              f"({C.RED}{s['packages_missing_required']} required missing{C.RESET}, "
              f"{C.YELLOW}{s['packages_missing_optional']} optional missing{C.RESET})")

        print(f"  System tools  : {s['tools_ok']}/{s['tools_total']} available")

        if s["packages_missing_required"]:
            print(f"\n{C.RED}❌ Missing REQUIRED packages:{C.RESET}")
            for p in self.results["packages"]["missing"]:
                print(f"   • {p['pip']:<28} ({p['description']})")

        if self.results["tools"]["missing"]:
            required_missing = [t for t in self.results["tools"]["missing"] if t["required"]]
            optional_missing = [t for t in self.results["tools"]["missing"] if not t["required"]]
            if required_missing:
                print(f"\n{C.RED}❌ Missing REQUIRED tools:{C.RESET}")
                for t in required_missing:
                    print(f"   • {t['binary']:<14} ({t['description']})")
            if optional_missing and self.verbose:
                print(f"\n{C.YELLOW}⚠️  Missing optional tools:{C.RESET}")
                for t in optional_missing:
                    print(f"   • {t['binary']:<14} ({t['description']})")

        print(f"\n{C.ORANGE}{'='*64}{C.RESET}")
        if s["ready"]:
            print(f"{C.GREEN}{C.BOLD}✅ SYSTEM READY{C.RESET} - All required dependencies satisfied.")
        else:
            print(f"{C.RED}{C.BOLD}❌ SYSTEM NOT READY{C.RESET} - Install missing required dependencies.")
            print(f"{C.WHITE}   Run: pip install -r requirements.txt{C.RESET}")
        print(f"{C.ORANGE}{'='*64}{C.RESET}\n")

    # ---------- Run ----------
    def run(self) -> bool:
        self.check_python()
        self.check_packages()
        self.check_tools()
        self.check_builtin_modules()
        s = self.summary()

        if self.json_out:
            import json
            print(json.dumps(self.results, indent=2, default=str))
        else:
            self.print_summary()

        return s["ready"]


# ============================================================
# CLI
# ============================================================
def install_packages(pip_names: List[str]) -> bool:
    if not pip_names:
        return True
    cmd = [sys.executable, "-m", "pip", "install", *pip_names]
    print(f"\n{C.CYAN}📥 Installing: {' '.join(pip_names)}{C.RESET}")
    try:
        subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{C.RED}Installation failed: {e}{C.RESET}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="🐙 Mysterious Cyclopus Requirements Checker"
    )
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show all packages/tools including optional")
    parser.add_argument("-j", "--json", action="store_true",
                        help="Output results as JSON")
    parser.add_argument("--install-required", action="store_true",
                        help="Attempt to pip install missing required packages")
    parser.add_argument("--install-all", action="store_true",
                        help="Attempt to pip install ALL missing packages")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable colored output")
    args = parser.parse_args()

    if args.no_color:
        C.disable()

    checker = RequirementsChecker(verbose=args.verbose, json_out=args.json)
    ready = checker.run()

    if args.install_required or args.install_all:
        missing = []
        if args.install_all:
            missing = [p["pip"] for p in checker.results["packages"]["missing"]] + \
                      [p["pip"] for p in checker.results["packages"]["broken"]]
        else:
            missing = [p["pip"] for p in checker.results["packages"]["missing"]]
        if missing:
            install_packages(missing)

    sys.exit(0 if ready else 1)


if __name__ == "__main__":
    main()