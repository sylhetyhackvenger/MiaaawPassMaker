#!/usr/bin/env python3
"""
Password Maker Pro - Terminal Dashboard Edition
Fiber optic style UI with professional password generation
"""

import random
import string
import os
import sys
import time
from datetime import datetime
from typing import List, Dict, Optional

class TerminalColors:
    """Terminal color codes for fiber optic effect"""
    # Fiber optic colors
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

    # Fiber optic effects
    FIBER1 = '\033[38;5;51m'    # Bright cyan
    FIBER2 = '\033[38;5;45m'    # Light blue
    FIBER3 = '\033[38;5;39m'    # Soft blue
    FIBER4 = '\033[38;5;33m'    # Deep blue
    FIBER5 = '\033[38;5;27m'    # Dark blue

    # Glow effects
    GLOW = '\033[38;5;123m'
    PULSE = '\033[38;5;159m'

class Dashboard:
    """Fiber optic dashboard UI"""

    BANNER = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⡸⣞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣧⢿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣼⣞⡿⣞⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⣰⣟⢾⣽⢫⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⢤⣶⡻⣞⣿⣺⢯⣽⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⣀⣠⣤⣿⣽⣻⢾⣽⣷⣾⣽⣻⣞⣷⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣶⣄⡀⠀⠀⠀⣉⣲⣴⢶⣞⡿⣽⣞⡷⣯⢿⡽⣞⣿⠟⠋⠁⠉⠈⠳⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⢶⣾⣿⡽⣯⣟⡾⣽⡷⣯⣟⡽⡾⣽⡯⠁⠀⠀⠀⠀⠀⠀⢮⣭⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢞⣿⣿⢯⡿⣿⣯⣟⣷⣯⢿⣳⣟⡷⣽⣼⣻⣽⠀⠀⠀⠀⠀⠀⠀⢀⣼⡯⡗⠋⠤⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣯⣽⣾⣿⣾⣗⡿⣯⡷⣯⣟⡷⣞⣼⣿⣀⠀⠀⠀⠀⢀⣠⡿⣏⡗⠈⠐⠈⠅⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠛⠏⠉⠉⠽⢟⢿⣿⣿⣿⣿⣷⣻⢾⡽⣞⡷⠄⡹⣶⢿⣻⢿⣻⡽⢯⣼⢦⠶⠁⠈⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣯⠇⠀⠀⠀⠀⠀⠁⣽⣿⣿⣿⣷⣯⣿⣽⣛⡦⠀⠀⢩⣿⣹⢯⣷⢻⣟⠺⢣⡖⣘⠤⠓⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡃⠁⠀⠀⠀⢀⣤⣾⣟⢿⣻⣿⣿⣟⡾⣽⡳⠄⠎⢳⣯⢯⣟⡾⢯⣞⣯⣓⠉⢀⠀⠀⡄⢢⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣷⣶⣳⣶⣺⣿⣿⣳⢯⣟⣿⣿⣳⢯⠛⠅⠃⠀⠀⣴⣿⡿⣬⢶⠾⠙⣊⣥⠾⡒⠊⢁⢠⠣⣌⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡽⣾⡽⣯⣟⣿⡿⣯⣿⣿⣾⢿⣿⠳⢏⣈⢠⠀⠀⣰⢿⡿⣽⣉⡶⠌⠋⠉⣀⡀⠁⠀⠀⠀⣘⡐⣂⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣽⣳⣟⣳⣟⣾⣽⣿⣿⣿⣿⣿⣦⣜⡻⡽⠆⠧⣴⡟⣯⢟⡳⣭⠲⠄⠐⠀⠀⠀⠈⠁⠉⠑⢊⡕⢃⠄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣾⣿⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⢧⠀⠹⠾⡵⡞⡽⢢⣃⠐⠀⠀⠄⡐⠀⠀⠀⡘⢦⠘⣌⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠒⡈⠀⡀⠄⡑⠢⣉⠴⣈⣆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣏⡴⣶⣵⣢⢤⢠⡀⡄⢠⠐⡰⢌⡱⠀⡁⡀⠆⡥⠆⡥⣛⡽⣾
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠔⠉⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣻⢷⣯⡽⣞⣷⣻⡼⣡⢋⡔⠣⠜⡐⢐⠠⡓⣤⣙⣲⣽⣻⢷
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣽⣞⣷⣻⡴⣣⢜⡱⣊⡕⣊⠠⡙⡰⣭⢷⣯⣿⢿
                        Miaaaaaaawwwww Ehehehehe
    """

    def __init__(self):
        self.passwords: List[Dict] = []
        self.passwords_file = "passave.txt"
        self.secret_password = "SYLHETYHACKVENGER2024"
        self.load_history()

    def load_history(self):
        """Load password history from file"""
        if os.path.exists(self.passwords_file):
            try:
                with open(self.passwords_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if 'Serial:' in line and 'Password:' in line:
                            parts = line.strip().split('|')
                            entry = {}
                            for part in parts:
                                if 'Serial:' in part:
                                    entry['serial'] = part.split('Serial:')[1].strip()
                                elif 'Password:' in part:
                                    entry['password'] = part.split('Password:')[1].strip()
                                elif 'Length:' in part:
                                    entry['length'] = part.split('Length:')[1].strip()
                                elif 'Custom:' in part:
                                    entry['custom'] = part.split('Custom:')[1].strip()
                            if entry:
                                self.passwords.append(entry)
            except:
                pass

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_fiber_line(self, text: str, color1: str, color2: str, width: int = 60):
        """Print a fiber optic line with gradient effect"""
        for i, char in enumerate(text):
            if i % 2 == 0:
                print(f"{color1}{char}", end='')
            else:
                print(f"{color2}{char}", end='')
        print(TerminalColors.RESET)

    def print_header(self):
        """Print the main header with fiber optic effect"""
        print(TerminalColors.FIBER1 + "="*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "█"*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "█" + " "*78 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER4 + "█" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.WHITE +
              "            TOOL: PASSWORD MAKER PRO v2.0          " +
              TerminalColors.RESET + TerminalColors.FIBER4 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "█" + TerminalColors.RESET +
              TerminalColors.DIM + TerminalColors.CYAN +
              "            AUTHOR: SYLHETYHACKVENGER              " +
              TerminalColors.RESET + TerminalColors.FIBER3 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER4 + "█" + TerminalColors.RESET +
              TerminalColors.DIM + TerminalColors.CYAN +
              "            STATUS: ⚡ ONLINE | FIBER OPTIC MODE   " +
              TerminalColors.RESET + TerminalColors.FIBER4 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "█" + " "*78 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "█"*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "="*80 + TerminalColors.RESET)

    def print_banner(self):
        """Print the ASCII banner"""
        print(TerminalColors.FIBER1 + self.BANNER + TerminalColors.RESET)
        print()
        print(TerminalColors.FIBER3 + "█"*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "█" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.WHITE +
              "  ⚡ PASSWORD MAKER  •  Miaaawwww DASHBOARD  ⚡".center(78) +
              TerminalColors.RESET + TerminalColors.FIBER2 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "█"*80 + TerminalColors.RESET)
        print()

    def print_dashboard(self):
        """Print the main dashboard"""
        self.clear_screen()
        self.print_banner()

        # Stats
        print(TerminalColors.FIBER1 + "╔" + "═"*78 + "╗" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.WHITE +
              "  SYSTEM STATUS".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  🟢 GENERATED: {len(self.passwords)} passwords" .ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  📁 SAVED TO: {self.passwords_file}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  🔐 SECRET KEY: {self.secret_password[:8]}...".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  ⏰ CURRENT TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "╚" + "═"*78 + "╝" + TerminalColors.RESET)
        print()

        # History table
        if self.passwords:
            self.print_history_table()

    def print_history_table(self):
        """Print password history as a table"""
        print(TerminalColors.FIBER2 + "┌" + "─"*78 + "┐" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "│" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.WHITE +
              "  PASSWORD HISTORY".center(78) +
              TerminalColors.RESET + TerminalColors.FIBER2 + "│" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "├" + "─"*78 + "┤" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "│" + TerminalColors.RESET +
              TerminalColors.CYAN +
              "  #  │  PASSWORD".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER2 + "│" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "├" + "─"*78 + "┤" + TerminalColors.RESET)

        # Show last 10 passwords
        start = max(0, len(self.passwords) - 10)
        for i in range(start, len(self.passwords)):
            entry = self.passwords[i]
            serial = entry.get('serial', 'N/A')
            password = entry.get('password', '')
            display_pwd = password[:25] + "..." if len(password) > 25 else password

            color = TerminalColors.FIBER3 if i % 2 == 0 else TerminalColors.FIBER4
            print(color + "│" + TerminalColors.RESET +
                  TerminalColors.WHITE + f"  {serial[:3]} │ {display_pwd}".ljust(78) +
                  TerminalColors.RESET + color + "│" + TerminalColors.RESET)

        print(TerminalColors.FIBER2 + "└" + "─"*78 + "┘" + TerminalColors.RESET)
        print()

    def generate_password(self, length: int, include_custom: bool = False, custom_secret: str = None) -> str:
        """Generate a password with optional custom integration"""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*^!?+-="
        password = ''.join(random.choice(chars) for _ in range(length))

        if include_custom and custom_secret:
            # Insert custom secret
            pos = random.randint(0, len(password))
            password = password[:pos] + custom_secret + password[pos:]

            # Pad to desired length
            target_len = length + len(custom_secret)
            while len(password) < target_len:
                password += random.choice(chars)
            if len(password) > target_len:
                password = password[:target_len]

        return password

    def save_password(self, password: str, custom: bool = False):
        """Save password to file with serial number"""
        serial = len(self.passwords) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = {
            'serial': str(serial).zfill(4),
            'password': password,
            'length': str(len(password)),
            'custom': str(custom),
            'time': timestamp
        }

        self.passwords.append(entry)

        with open(self.passwords_file, 'a') as f:
            f.write(f"Serial: {entry['serial']} | Password: {password} | Length: {len(password)} | Custom: {custom} | Time: {timestamp}\n")

        return entry

    def display_result(self, entry: Dict):
        """Display generated password in a fiber optic box"""
        print(TerminalColors.FIBER1 + "╔" + "═"*78 + "╗" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.GREEN +
              "  ✅ PASSWORD GENERATED SUCCESSFULLY".center(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "╠" + "═"*78 + "╣" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  📌 SERIAL #: {entry['serial']}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.YELLOW + f"  🔑 PASSWORD : {entry['password']}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  📏 LENGTH  : {entry['length']} characters".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  🎯 CUSTOM  : {entry['custom']}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  💾 SAVED TO: {self.passwords_file}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER1 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "╚" + "═"*78 + "╝" + TerminalColors.RESET)
        print()

    def get_user_input(self):
        """Get user input with fiber optic styling"""
        print(TerminalColors.FIBER3 + "╔" + "═"*78 + "╗" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.WHITE +
              "  📝 PASSWORD GENERATION OPTIONS".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "╠" + "═"*78 + "╣" + TerminalColors.RESET)

        # Length input
        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + "  Enter password length: ".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET + "  " +
              TerminalColors.WHITE, end='')

        try:
            length_input = input().strip()
            if not length_input:
                length = 12
            else:
                length = int(length_input)
                if length < 4:
                    print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
                          TerminalColors.RED + "  ⚠️ Minimum length is 4".ljust(78) +
                          TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
                    length = 4
        except ValueError:
            length = 12

        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + f"  ✅ Length set to: {length}".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)

        # Custom secret option
        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
              TerminalColors.CYAN + "  Include custom secret? (y/n): ".ljust(78) +
              TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET + "  " +
              TerminalColors.WHITE, end='')

        include_custom = input().strip().lower() == 'y'

        custom_secret = None
        if include_custom:
            print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
                  TerminalColors.CYAN + "  Enter custom secret: ".ljust(78) +
                  TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
            print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET + "  " +
                  TerminalColors.WHITE, end='')
            custom_secret = input().strip()
            if not custom_secret:
                custom_secret = self.secret_password

        print(TerminalColors.FIBER3 + "╚" + "═"*78 + "╝" + TerminalColors.RESET)
        print()

        return length, include_custom, custom_secret

    def run(self):
        """Main execution loop"""
        while True:
            self.print_dashboard()

            # Get user input
            length, include_custom, custom_secret = self.get_user_input()

            # Generate password
            print(TerminalColors.FIBER2 + "█"*80 + TerminalColors.RESET)
            print(TerminalColors.CYAN + "  ⏳ Generating password..." + TerminalColors.RESET)
            time.sleep(0.5)

            password = self.generate_password(length, include_custom, custom_secret)

            # Save and display
            entry = self.save_password(password, include_custom)

            # Show result
            self.clear_screen()
            self.print_banner()
            self.display_result(entry)

            # Ask to continue
            print(TerminalColors.FIBER3 + "╔" + "═"*78 + "╗" + TerminalColors.RESET)
            print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET +
                  TerminalColors.CYAN + "  Generate another password? (y/n): ".ljust(78) +
                  TerminalColors.RESET + TerminalColors.FIBER3 + "║" + TerminalColors.RESET)
            print(TerminalColors.FIBER3 + "║" + TerminalColors.RESET + "  " +
                  TerminalColors.WHITE, end='')

            if input().strip().lower() != 'y':
                break

        # Exit gracefully
        self.clear_screen()
        print(TerminalColors.FIBER1 + "="*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "█"*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER3 + "█" + TerminalColors.RESET +
              TerminalColors.BOLD + TerminalColors.GREEN +
              "  ✅ THANK YOU FOR USING PASSWORD MAKER PRO".center(78) +
              TerminalColors.RESET + TerminalColors.FIBER3 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER4 + "█" + TerminalColors.RESET +
              TerminalColors.CYAN +
              "  🌐 STAY CONNECTED • SYLHETYHACKVENGER".center(78) +
              TerminalColors.RESET + TerminalColors.FIBER4 + "█" + TerminalColors.RESET)
        print(TerminalColors.FIBER2 + "█"*80 + TerminalColors.RESET)
        print(TerminalColors.FIBER1 + "="*80 + TerminalColors.RESET)
        print()

def main():
    dashboard = Dashboard()
    try:
        dashboard.run()
    except KeyboardInterrupt:
        print("\n\n" + TerminalColors.RED + "  ⚠️ Operation cancelled" + TerminalColors.RESET)
    except Exception as e:
        print(f"\n\n{TerminalColors.RED}  ❌ Error: {e}{TerminalColors.RESET}")

if __name__ == "__main__":
    main()
