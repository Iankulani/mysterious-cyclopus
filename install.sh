#!/usr/bin/env bash
# ============================================================
# 🐙 MYSTERIOUS CYCLOPUS - Linux / macOS Installer
# ============================================================
set -e

CYAN='\033[96m'; ORANGE='\033[38;5;214m'; GREEN='\033[92m'
YELLOW='\033[93m'; RED='\033[91m'; BOLD='\033[1m'; RESET='\033[0m'

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${PROJECT_DIR}/.venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

banner() {
    echo -e "${ORANGE}"
    cat <<'EOF'
   __  ___               __                        __
  /  |/  /_  _____  ___ / /____ ___   ___  ___ ___/ /  __ __ ___
 / /|_/ / / / / _ \/ _ / __/ -_) _ \ / _ \/ -_) _  /  / // /(_-<
/_/  /_/_/ /_/\___/_/ /_/\__/\___/ /_//_/\__/\_,_/   \_,_//___/

        🐙 MYSTERIOUS CYCLOPUS v1.0.0 - Installer 🐙
EOF
    echo -e "${RESET}"
}

log()  { echo -e "${CYAN}[*]${RESET} $*"; }
ok()   { echo -e "${GREEN}[✓]${RESET} $*"; }
warn() { echo -e "${YELLOW}[!]${RESET} $*"; }
err()  { echo -e "${RED}[✗]${RESET} $*"; }

require_root_or_sudo() {
    if [[ "$EUID" -ne 0 ]]; then
        if command -v sudo &>/dev/null; then
            SUDO="sudo"
        else
            warn "No sudo available — system packages may fail."
            SUDO=""
        fi
    else
        SUDO=""
    fi
}

detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG_MANAGER="brew"
    elif [[ -f /etc/debian_version ]]; then
        OS="debian"
        PKG_MANAGER="apt-get"
    elif [[ -f /etc/redhat-release ]]; then
        OS="redhat"
        PKG_MANAGER="yum"
    elif [[ -f /etc/arch-release ]]; then
        OS="arch"
        PKG_MANAGER="pacman"
    else
        OS="unknown"
        PKG_MANAGER=""
    fi
    ok "Detected OS: ${BOLD}${OS}${RESET} (pkg: ${PKG_MANAGER:-none})"
}

check_python() {
    log "Checking Python..."
    if ! command -v "$PYTHON_BIN" &>/dev/null; then
        err "Python 3 not found. Please install Python 3.7+."
        exit 1
    fi
    PYVER=$("$PYTHON_BIN" -c 'import sys;print("%d.%d"%sys.version_info[:2])')
    ok "Python ${PYVER} found at $(command -v $PYTHON_BIN)"
    "$PYTHON_BIN" - <<'PY' || { err "Python 3.7+ required"; exit 1; }
import sys
sys.exit(0 if sys.version_info >= (3, 7) else 1)
PY
}

install_system_packages() {
    log "Installing system packages (may require sudo)..."
    require_root_or_sudo
    case "$OS" in
        debian)
            $SUDO apt-get update -qq
            $SUDO apt-get install -y \
                python3 python3-pip python3-venv python3-dev \
                build-essential libssl-dev libffi-dev \
                nmap curl wget dnsutils traceroute netcat-openbsd \
                openssh-client git tcpdump docker.io docker-compose-plugin || true
            ;;
        redhat)
            $SUDO yum install -y \
                python3 python3-pip python3-devel \
                gcc openssl-devel libffi-devel \
                nmap curl wget bind-utils traceroute nc \
                openssh-clients git tcpdump docker || true
            ;;
        arch)
            $SUDO pacman -Sy --noconfirm \
                python python-pip python-virtualenv \
                base-devel openssl libffi \
                nmap curl wget bind-tools traceroute openbsd-netcat \
                openssh git tcpdump docker docker-compose || true
            ;;
        macos)
            if ! command -v brew &>/dev/null; then
                err "Homebrew not found. Install from https://brew.sh"
                return
            fi
            brew update
            brew install python3 nmap curl wget bind traceroute netcat \
                         openssh git tcpdump docker docker-compose || true
            ;;
        *)
            warn "Unknown OS — skipping system package installation."
            ;;
    esac
    ok "System packages installed (or already present)."
}

create_venv() {
    log "Creating Python virtual environment..."
    if [[ ! -d "$VENV_DIR" ]]; then
        "$PYTHON_BIN" -m venv "$VENV_DIR"
        ok "Virtual environment created at $VENV_DIR"
    else
        warn "Virtual environment already exists."
    fi
    # shellcheck source=/dev/null
    source "$VENV_DIR/bin/activate"
    python -m pip install --upgrade pip setuptools wheel -q
    ok "pip/setuptools/wheel upgraded."
}

install_python_requirements() {
    log "Installing Python requirements..."
    if [[ ! -f "${PROJECT_DIR}/requirements.txt" ]]; then
        err "requirements.txt not found in ${PROJECT_DIR}"
        exit 1
    fi
    pip install -r "${PROJECT_DIR}/requirements.txt" || {
        warn "Some packages failed — continuing anyway."
    }
    ok "Python requirements installed."
}

run_self_check() {
    log "Running requirements check..."
    if [[ -f "${PROJECT_DIR}/requirements-check.py" ]]; then
        python "${PROJECT_DIR}/requirements-check.py" -v || true
    else
        warn "requirements-check.py not found."
    fi
}

create_launchers() {
    log "Creating launcher scripts..."
    cat > "${PROJECT_DIR}/run.sh" <<EOF
#!/usr/bin/env bash
cd "\$(dirname "\$0")"
source "${VENV_DIR}/bin/activate"
exec python "${PROJECT_DIR}/mysterious_cyclopus.py" "\$@"
EOF
    chmod +x "${PROJECT_DIR}/run.sh"

    # Optional: system-wide symlink
    if [[ -w /usr/local/bin ]]; then
        ln -sf "${PROJECT_DIR}/run.sh" /usr/local/bin/cyclopus 2>/dev/null || true
        ok "Installed 'cyclopus' to /usr/local/bin (run: cyclopus)"
    fi
    ok "Launcher created: ${PROJECT_DIR}/run.sh"
}

main() {
    banner
    detect_os
    check_python
    install_system_packages
    create_venv
    install_python_requirements
    run_self_check
    create_launchers

    echo -e "\n${GREEN}${BOLD}✅ Installation complete!${RESET}"
    echo -e "${WHITE}To run:${RESET}"
    echo -e "  ${ORANGE}source ${VENV_DIR}/bin/activate${RESET}"
    echo -e "  ${ORANGE}python mysterious_cyclopus.py${RESET}"
    echo -e "  or simply: ${ORANGE}./run.sh${RESET}\n"
}

main "$@"