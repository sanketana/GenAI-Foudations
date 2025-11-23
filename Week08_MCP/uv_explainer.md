# 🚀 `uv` — Modern Python Toolchain (Quick Guide)

`uv` is a fast, single tool that replaces multiple traditional Python utilities:

| `uv` Feature | Replaces |
|-------------|----------|
| `uv run` | python + virtualenv for temporary runs |
| `uv venv` | virtualenv / venv |
| `uv pip` | pip |
| `uvx` | pipx / npx |

---

## 🧪 Workflow A — Experimental / Temporary Use

Use **`uv run`** to execute Python scripts with an isolated environment automatically.

```bash
uv run script.py
uv run --with mcp server.py
uv run -m module_name
```

✔ No setup  
✔ Auto-installs needed packages  
✔ Keeps your project folder clean  
❌ Environment is temporary — deleted after execution

Best for: examples, demos, quick testing

---

## 🏗 Workflow B — Real Project Development

Use **`uv venv`** + **`uv pip`** for persistent environments inside project.

```bash
uv venv
source .venv/bin/activate
uv pip install mcp fastapi
```

✔ Persistent venv in your project  
✔ IDE & team-friendly  
✔ Reproducible builds  
✔ Best for production or collaborative work

---

## ⚙️ Running Python CLI Tools

Use **`uvx`** to run third-party tools without installing them globally.

```bash
uvx ruff check .
uvx black .
uvx pytest
uvx mcp-cli
```

✔ No global install  
✔ Caches package wheels  
✔ Perfect for linters, formatters, test runners

> `uv run` = run **your code**  
> `uvx` = run **someone else’s CLI tool**

---

## 📍 Caching & Storage

| Location | Purpose | Persistent? |
|---------|---------|-------------|
| `~/.cache/uv` | Cached wheels + metadata | ✔ Yes |
| OS temp directory | Env used by `uv run` / `uvx` | ❌ No |

Automatic updates?  
- ✔ If version not pinned  
- ✔ If within allowed version range  
- ❌ If version explicitly pinned (e.g., `==1.0.0`)

---

## 🔥 Comparison Table

| Feature | `uv run` | `uv venv` | `uvx` |
|--------|----------|-----------|------|
| Runs your local script | ✔ | ✔ | ❌ |
| Runs CLI tools | ❌ | ✔ | ✔ |
| Temporary environment | ✔ | ❌ | ✔ |
| Persistent dependencies | ❌ | ✔ | ❌ |
| Good for production | ❌ | ✔ | ❌ |

---

## 📝 TL;DR

> **Use `uv run` when experimenting**  
> **Use `uv venv` + `uv pip` for real projects**  
> **Use `uvx` to run CLI tools without installing them**
