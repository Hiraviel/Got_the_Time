# Got_the_Time

An Andon-style visual timer system for a production line, written in Python with Tkinter.

An operator enters a VIN and a model, a large on-screen stopwatch starts, and its color and status change as time passes: green while on pace, yellow when approaching the limit, red once the limit is exceeded. When the run ends, the system writes a `.txt` record with the date, VIN, model, start time, end time, elapsed time, and OK/NOK result, then loops back to ask for the next VIN.

## How it works

1. The script asks for a **VIN** (alphanumeric, no symbols) and a **MODEL** (6 alphanumeric characters) in the console.
2. A Tkinter stopwatch window opens and counts up in `h:m:s`.
3. The window background and status change with elapsed time:
   - **Green / OK** — within the time limit
   - **Yellow / OK** — approaching the limit
   - **Red / NOK** — over the limit
4. When the timer window is closed, the run is recorded to a `.txt` file and the script asks for the next VIN, running continuously.

## Versions

### v1 — `Timer.py` + `Tkinter_Timer.py`

- The timer logic lives in `Timer.py`; the stopwatch window is defined in `Tkinter_Timer.py`.
- Color thresholds in the v1 code: green under 5 minutes, yellow from 5 to 10 minutes, red at 10 minutes and over. (The documented production thresholds are 27 and 52 minutes — see v1.1.)
- The record file is named `<VIN>_<date>.txt`, e.g. `ESTEESUNCODIGOVIN_2019-05-19.txt`, and contains: date, VIN, model, start time, end time, elapsed time, OK/NOK — comma-separated.

### v1.1 — `Timer_v1.1.py` (recommended)

- Self-contained: the stopwatch is built into the script, so `Tkinter_Timer.py` is no longer needed.
- Runs the timer and the console input on separate threads, so the process keeps working continuously.
- Color thresholds match the documented limits: green 0–26 minutes, yellow 27–51 minutes, red at 52 minutes and over.
- The record filename now includes the start time (`<VIN>_<date>_<HHMM>.txt`), so reusing the same VIN no longer overwrites the previous record.
- The timer window can be closed from the console thread to end a run.

### Standalone stopwatch — `Tkinter_Timer.py`

- The stopwatch window on its own, with no VIN capture and no output file.
- Thresholds: green under 27 minutes, yellow 27–53 minutes, red at 54 minutes and over.
- Start/stop buttons exist in the code but are commented out; the timer starts automatically.

## Input rules

- **VIN**: alphanumeric characters only (`A-Z`, `0-9`), no symbols. The design calls for 17 characters; the v1 code currently checks for a length of 4, with a comment in the code marking it to be changed to 17.
- **MODEL**: exactly 6 alphanumeric characters.

## Requirements

- Python 3 with Tkinter (included with standard Python on Windows)
- No external libraries

## Usage

```bash
python Timer_v1.1.py
```

Or, for the original version:

```bash
python Timer.py
```

Type the VIN and model when prompted, then watch the stopwatch window. Close the window to end the run and generate the record file.

## Files

| File | Description |
| --- | --- |
| `Timer_v1.1.py` | Current version: self-contained, threaded, 27/52-minute thresholds |
| `Timer.py` | v1: console capture + timer (uses `Tkinter_Timer.py`) |
| `Tkinter_Timer.py` | v1 stopwatch window, also runnable as a standalone timer |
| `README.md` | This file |
