# Running tests

```
# Install Python dependencies

$ python -m venv .venv 
# or
$ python3 -m venv .venv
$ source .venv/bin/activate
# or (from cmd.exe, not PowerShell)
$ .venv\Scripts\activate.bat
$ pip install -r requirements.txt

# Install browser
$ playwright install chromium

# Run the tests
# TODO: fix the URL
$ pytest -vs --browser=chromium --slowmo=1000 --headed --base-url=https://g.se1.hr.dmerej.info/
```

## Using `ipdb` as debugger

* Set the env var `PYTHONBREAKPOINT`  to `ipdb.set_trace`
* Call the breakpoint() function where you want to start the interactive debugging