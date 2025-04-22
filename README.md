# Event Scheduler

The **Event Scheduler** is a Python-based application designed to help users manage and schedule events.

---

## Features

- **Add Events:** Create new events with details such as name, date, and description.
- **Edit Events:** Modify existing event information.
- **Delete Events:** Remove events you no longer need.
- **View Events:** List all scheduled events in a readable format.
- **Persistent Storage:** Save your events to a file and load them on startup.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/event_scheduler.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd event_scheduler
   ```
3. **Install dependencies:**
   ```bash
   poetry install
   ```
   > If you don't have [Poetry](https://python-poetry.org/docs/#installation) installed, follow the official instructions to set it up.

---

## Usage

1. **Run the application:**
   ```bash
   poetry run python src/event_scheduler/main.py
   ```
2. **Follow the on-screen instructions** to add, edit, delete, or view your events.

---

## Project Structure

```
event_scheduler/
├── src/
│   └── event_scheduler/
│       ├── main.py          # Entry point of the 
│       ├── event.py         # Event Class
│       └── scheduler.py     # Scheduler Class
│       └── errors.py        # Error types
├── test/                    # Testing directory
├── pyproject.toml           # Poetry configuration
└── README.md                # Project documentation
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.


