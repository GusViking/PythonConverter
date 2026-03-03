# PythonConverter

## Requirements

- Python 3.8+
- Free API key from [exchangerate-api.com](https://www.exchangerate-api.com/)

---

## Installation

### 1. Clone project

```bash
https://github.com/GusViking/PythonConverter.git
```

### 2. Create VE

```bash
python3 -m venv .venv
```

### 3. Activate VE

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependecies
**Via uv**
```bash
uv sync
```

**via pip**
```bash
pip install -r requirements.txt
```

---

## Use

### First time - insert your API key

```bash
python3 valuta.py --key YOUR_API_KEY
```

this saves the key in your `.env` file, so you don't have to write it a second time.

### After the first time

```bash
python3 valuta.py
```

The program guides you through the rest:

```
Write first currency: DKK
Write your second currency: EUR
Write how much you want to exchange: 100

Conversion rate: 0.134
Result: 13.4
```

---

## Deactivate your VM

When you are finished, you can deactivate the VM with

```bash
deactivate
```