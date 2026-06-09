# Food Delivery

Simple, modular Food Delivery example demonstrating SOLID principles.

## Overview

This project implements a small, console-based food delivery system with a clear separation of concerns across controllers, services, repositories, and a lightweight CLI.

## Features

- Customer, Restaurant and Order management
- SQLite persistence (`food_delivery.db` included)
- Pluggable strategies for delivery and discounts

## Quickstart

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

2. Run the app:

```powershell
python main.py
```

The CLI will present a menu to interact with customers, restaurants and orders.

## Project Structure

- `main.py` — application entrypoint
- `app.py` — small App wrapper that runs the CLI
- `cli/` — command-line interface
- `controllers/`, `services/`, `repositories/` — core layered architecture
- `database/` — SQLite database adapter
- `models/`, `factories/`, `strategies/`, `utils/` — supporting modules

## Notes

- The project uses a local SQLite file `food_delivery.db` in the project root.
- There is no external dependency manifest; add requirements as needed.

## License

Open for educational use.
