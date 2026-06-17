# Timezone Converter

A web application for converting multiple local times from one timezone to another. The backend handles all conversion logic using IANA timezone identifiers and daylight saving time (DST) rules, so results stay accurate across regions and seasons.

## Features

- Convert multiple date/time values in a single request
- DST-aware conversion via Python's `zoneinfo`
- IANA timezone support (e.g. `Asia/Tokyo`, `America/New_York`)
- Simple web UI with timezone dropdowns and datetime pickers
- Copy individual results or all results at once
- Per-item error handling — invalid inputs do not block other conversions

## Tech Stack

- **Backend:** Python, FastAPI, Pydantic
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Timezone data:** `zoneinfo` (stdlib)

## Project Structure

```
timezone-converter/
├── app/
│   ├── main.py              # FastAPI application and routes
│   ├── schemas.py           # Request/response models
│   └── services/
│       └── converter.py     # Timezone conversion logic
├── static/
│   └── index.html           # Web UI
└── docs/
    └── architecture.md      # Design and format specifications
```

## Requirements

- Python 3.9 or later

## Setup

1. Clone the repository and enter the project directory:

```bash
cd timezone-converter
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

## Running the Application

1. Start the API server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

2. Open the web UI:

Open `static/index.html` in your browser. The frontend sends requests to `http://127.0.0.1:8000/convert`.

You can also explore the API interactively at `http://127.0.0.1:8000/docs`.

## Usage

1. Select a **From Timezone** (source) and **To Timezone** (target).
2. Pick one or more date/time values.
3. Click **Convert** to see the results.
4. Use **Copy** or **Copy All** to copy converted times to the clipboard.

### Input Format

Times are sent to the API in this format:

```
MM/DD HH:MM
```

Example:

```
01/13 09:00
01/13 13:30
01/14 00:15
```

### Output Format

Converted times are returned as:

```
MM/DD (Day) HH:MM
```

Example:

```
01/12 (Mon) 19:00
01/12 (Mon) 23:30
01/13 (Tue) 00:15
```

## API Reference

### `GET /`

Health check endpoint.

**Response:**

```json
{
  "message": "API is running"
}
```

### `POST /convert`

Convert one or more local times between timezones.

**Request body:**

```json
{
  "from_timezone": "Asia/Tokyo",
  "to_timezone": "America/New_York",
  "times": ["01/13 09:00", "01/13 13:30"]
}
```

**Response:**

```json
{
  "results": [
    {
      "input": "01/13 09:00",
      "output": "01/12 (Mon) 19:00",
      "status": "ok"
    },
    {
      "input": "invalid",
      "output": null,
      "status": "error",
      "error": "time data 'invalid' does not match format '%m/%d %H:%M'"
    }
  ]
}
```

| Field | Description |
|-------|-------------|
| `from_timezone` | IANA timezone name for the input times |
| `to_timezone` | IANA timezone name for the output times |
| `times` | List of local times in `MM/DD HH:MM` format |
| `status` | `"ok"` on success, `"error"` on failure |
| `output` | Converted time string (present when `status` is `"ok"`) |
| `error` | Error message (present when `status` is `"error"`) |

## Architecture

For design principles, input/output rules, and system overview, see [docs/architecture.md](docs/architecture.md).
