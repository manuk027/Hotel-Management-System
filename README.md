# 🏨 Hotel Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)
> A simple CLI-based hotel management system using Python and CSV for basic room and customer operations.

---

## 📌 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🚀 Features](#-features)
- [🗂️ Data Storage](#️-data-storage)
- [▶️ How to Run](#️-how-to-run)
- [📎 Dependencies](#-dependencies)
- [👨‍💻 Author](#-author)
- [📫 Contact](#-contact)

---

## 📌 Project Overview

This **Hotel Management System** is a basic command-line interface application written in Python. It allows the hotel staff to manage:

- 🛏️ Room details
- 👤 Customer records
- 🔁 Room assignment and return

No external databases or frameworks are required. All data is stored in local CSV files for ease of access and modification.

---

## 🚀 Features

### 🛏️ Room Management
- Add new rooms
- Edit room details
- Delete room entries
- View all available rooms

### 👤 Customer Management
- Add customer records
- Update customer details
- Delete customer records
- View all customers

### 🔁 Room Allocation
- Issue a room to a customer
- Mark a room as vacated

---

## 🗂️ Data Storage

The application uses the following CSV files:

| File Name        | Description                          |
|------------------|--------------------------------------|
| `rooms.csv`      | Stores room details                  |
| `customers.csv`  | Stores customer information          |
| `room_issue.csv` | Tracks room issue history            |
| `members.csv`    | Used to verify customer numbers      |

---

## ▶️ How to Run

1. ✅ Ensure Python 3.x is installed on your system.
2. 📁 Place all `.py` and `.csv` files in the same folder.
3. 💻 Run the script from your terminal or command line:

```bash
python hotel_management.py

## 👨‍💻 Author
