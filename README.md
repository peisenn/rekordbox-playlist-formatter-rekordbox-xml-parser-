# rekordbox-playlist-formatter 🎧

A lightweight Python script that parses Rekordbox exported XML databases (`rekordbox.xml`) and outputs a clean, plain-text summary of your DJ collection and playlists (BPM, Key, Track Name, Artist).

> **Acknowledgment**: Originally written by my late mentor and close friend, John (J.I.), to streamline DJ music library management. Shared here to preserve his pragmatic hacker spirit and keep his useful tools running.

---

## ✨ Features

- **Fast XML Parsing**: Uses `xmltodict` to extract track details directly from Rekordbox export databases.
- **Clean CLI Output**: Formats BPM, Tonality (Key), Track Name, and Artist into neat, scannable columns.
- **Zero Overhead**: Simple, single-file script without unnecessary dependencies.

---

## 🛠️ Prerequisites

Make sure you have Python installed, then install the required dependencies:

```bash
pip install lxml xmltodict
