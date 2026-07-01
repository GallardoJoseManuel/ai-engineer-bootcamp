# Virtual Environments

## What is a virtual environment?

A virtual environment (venv) is an isolated Python environment that contains its own interpreter and installed packages.

Each project can have its own dependencies without affecting the global Python installation or other projects.

---

## Why do we use it?

Without virtual environments:

- Different projects may require different package versions.
- Installing packages globally can create dependency conflicts.
- Reproducing projects becomes much harder.

Using a virtual environment ensures that every project runs with exactly the packages it needs.

---

## Create a virtual environment

```bash
python -m venv .venv
```

This creates a folder called `.venv` containing a separate Python installation.

---

## Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

When activated, the terminal shows:

```text
(.venv)
```

which means Python and pip now refer to the virtual environment.

---

## Verify the environment

Check the Python executable:

```bash
where python
```

Check pip:

```bash
where pip
```

Both should point inside:

```
.venv/
```

---

## Install packages

Example:

```bash
pip install numpy
pip install pandas
pip install jupyter
```

Packages installed inside the virtual environment do not affect the global Python installation.

---

## Deactivate

```bash
deactivate
```

This returns the terminal to the global Python installation.

---

## Packages currently used in this bootcamp

- NumPy
- Pandas
- Jupyter Notebook

---

## Key Takeaways

- Every project should have its own virtual environment.
- Never install project dependencies globally.
- The `.venv` folder should not be uploaded to GitHub.
- Use `.gitignore` to exclude it.