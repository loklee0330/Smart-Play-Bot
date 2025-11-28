# Competitive Booking Clicker (Agency Adjustable Edition)

_A precision mouse click automation tool for competitive online bookings, with a user-friendly GUI and pro-level accuracy controls._

---

## Overview

**Competitive Booking Clicker** is a Python utility that lets you schedule ultra-fast, ultra-precise mouse clicks at a specific screen location and exact time.  
Originally built for high-stakes booking battles (think: government or sports signups), this tool is agency-tested and adjustable to fit different queueing strategies.

**Features:**
- Schedule clicks down to the millisecond (HH:MM:SS:MMM).
- Burst multiple clicks with adjustable intervals (default: 5 clicks, 10ms apart).
- Add a safety delay for network/clock drift.
- Live display and quick-fill for your current mouse position.
- Keyboard shortcut: `Ctrl+C` to auto-fill X/Y with current cursor location.
- Built-in pro tips from agency experience!

---

## Getting Started

### Prerequisites

- **Python 3.x** (https://www.python.org)
- **pip** (comes with Python)
- Required packages: `tkinter`, `pyautogui`
    - `tkinter` is standard in most Python installs.  
    - Install `pyautogui` via pip (see below).

### Installation

1. **Clone this repo:**
    ```bash
    git clone https://github.com/loklee0330/Smart-Play-Bot.git
    cd Smart-Play-Bot
    ```

2. **Install dependencies:**
    ```bash
    pip install pyautogui
    ```
    (If you get errors about `tkinter`, install it via your package manager or use Python from python.org.)

---

## Usage

1. Run the app:
    ```bash
    python hack.py
    ```
2. Enter the **target time** (format: `HH:MM:SS:MMM`), mouse **X/Y coordinates**, **number of clicks**, **interval** between clicks (ms), and a **safety delay** (ms).
3. Use the **"Use Current Mouse Position"** button or `Ctrl+C` to quickly fill your mouse coordinates.
4. Click **Start**. The click burst will fire exactly at the scheduled moment.

**Pro Tip:**  
Sync your PC clock to an NTP server for maximum accuracy (critical for government or ticketing queues).

---

## Example

- **Time:** `07:00:00:000`
- **X:** `350`
- **Y:** `640`
- **Clicks:** `5`
- **Interval:** `10` (ms)
- **Safety Delay:** `8` (ms)

This will send 5 rapid-fire clicks at the exact location right after 7am, with an 8ms safety buffer.

---

## Contributing

Pull requests and suggestions are welcome!  
- Please open an issue first for major changes.
- Keep your code clean and well-commented (agency standard).
- Respect `.gitignore` and never commit personal data or credentials.

---

## License

[MIT](LICENSE) (or your chosen license)

---

## Author

Locke Lee  
loklee0330@gmail.com

---

*Agency Pro Tip: Never run automation tools on production systems without prior testing! Sync your clock, test with a dummy site, and stay ethical.*

---
