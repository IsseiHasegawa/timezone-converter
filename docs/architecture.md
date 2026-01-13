Purpose

This document describes the overall architecture of a web-based timezone converter application.
The goal of the application is to allow users to convert multiple local times from one timezone to another accurately, with correct handling of daylight saving time (DST).

Overview

The application provides a simple web interface where users:
	•	Select an input timezone (source timezone)
	•	Select an output timezone (target timezone)
	•	Enter multiple local times at once
	•	Receive converted times in a consistent, human-readable format

All timezone conversion logic is handled by a Python-based API to ensure correctness and maintainability.

System Architecture

The system follows a client–server architecture:
[ Web Frontend ]
  - Timezone selection (dropdown)
  - Multiple time input (textarea)
  - Result display

        ↓ HTTP (JSON)

[ Python API ]
  - Input validation
  - Time parsing
  - Timezone conversion (DST-aware)
  - Output formatting

Design Principles
	•	Time conversion logic is centralized in the API
	•	The frontend is responsible only for input and presentation
	•	IANA timezone identifiers are used instead of fixed UTC offsets
	•	DST behavior is handled consistently on the server side

Web Interface Design

Input

Timezone Selection
	•	Users select:
	•	Input timezone (the timezone they know)
	•	Output timezone (the timezone they want to know)
	•	Timezones are selected via dropdown menus
	•	IANA timezone names are used (e.g., Asia/Tokyo, America/New_York)

Time Input
	•	Users can input multiple times at once
	•	Input is provided as a multiline text area
	•	Each line represents one local time

Input format (strict):MM/DD HH:MM

Example:
01/13 09:00
01/13 13:30
01/14 00:15

•	Empty lines are ignored
•	Invalid lines are reported as errors without stopping other conversions

Output

Each input time is converted and displayed in the following format:MM/DD (Day) HH:MM

Example:
01/12 (Mon) 19:00
01/12 (Mon) 23:30
01/13 (Tue) 00:15

Output Rules
	•	Day of the week is displayed using a three-letter English abbreviation (Mon, Tue, Wed, etc.)
	•	24-hour time format is used
	•	All values are zero-padded
	•	Output order matches the input order

