# 🏨 Hotel Management System

## 📌 Project Overview

This **Hotel Management System** is a Python-based CLI (Command Line Interface) program that helps manage the operations of a hotel including:

- Room management
- Customer details
- Room issuing and leaving

Data is handled using **CSV files**, making it lightweight and easy to understand for beginners.

---

## 👨‍💻 Author

**Manu Krishna**  
📅 Date Started: 01-02-2022

---

## ⚙️ Features

### 🛏️ Room Management
- Add a new room
- Edit existing room details
- Delete a room
- View all rooms

### 👤 Customer Management
- Add a new customer
- Update existing customer details
- Remove a customer
- View all customers

### 🔁 Room Assignment
- Issue a room to a customer
- Leave/return a room

---

## 🗃️ Data Storage

All data is stored in simple **CSV files**:
- `rooms.csv`
- `customers.csv`
- `room_issue.csv`
- `members.csv` (used to check valid customers while issuing rooms)

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Place this script in a folder.
3. Ensure the required CSV files are present or will be created when running:
    - If the files do not exist, they will be created automatically.
4. Open a terminal/command prompt.
5. Run the program using:
   ```bash
   python hotel_management.py
