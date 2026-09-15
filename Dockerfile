# ============================================================
# 🐙 MYSTERIOUS CYCLOPUS - Multi-stage Docker Image
# ============================================================
# Base: Debian slim (smaller, has apt)
FROM python:3.11-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        libffi-dev \
        libssl-dev \
        libpcap-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Create virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python deps first (cache-friendly)
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# ============================================================
# Runtime stage
# ============================================================
FROM python:3.11-slim-bookworm AS runtime

LABEL org.opencontainers.image.title="Mysterious Cyclopus" \
      org.opencontainers.image.description="Cybersecurity Command & Control Platform" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.authors="Security Team" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH" \
    CYCLOPUS_HOME=/opt/cyclopus

# Runtime system tools
RUN apt-get update && apt-get install -y --no-install-recommends \
        nmap \
        curl \
        wget \
        dnsutils \
        traceroute \
        netcat-openbsd \
        openssh-client \
        iputils-ping \
        iproute2 \
        tcpdump \
        libpcap0.8 \
        tini \
        ca-certificates \
        procps \
        vim-tiny \
    && rm -rf /var/lib/apt/lists/*

# Copy venv from builder
COPY --from=builder /opt/venv /opt/venv

WORKDIR ${CYCLOPUS_HOME}

# Copy application
COPY mysterious_cyclopus.py       ./
COPY requirements.txt             ./
COPY requirements-check.py        ./
COPY config.example.json          ./

# Create non-root user (but allow override for raw socket features)
RUN groupadd -r cyclopus && useradd -r -g cyclopus -d ${CYCLOPUS_HOME} -s /bin/bash cyclopus \
    && mkdir -p ${CYCLOPUS_HOME}/.mysterious_cyclopus \
    && chown -R cyclopus:cyclopus ${CYCLOPUS_HOME}

# Persistent volumes
VOLUME ["/opt/cyclopus/.mysterious_cyclopus", "/opt/cyclopus/cyclopus_reports"]

# Default port for web dashboard
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests,sys; sys.exit(0 if requests.get('http://127.0.0.1:5000/api/stats', timeout=5).status_code==200 else 1)" \
    || exit 1

# Use tini for proper signal handling
ENTRYPOINT ["/usr/bin/tini", "--"]

# Default command: run the platform in non-interactive mode
CMD ["python", "mysterious_cyclopus.py"]