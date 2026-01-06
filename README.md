# JupyterHub with Pixi

A JupyterHub server managed with [pixi](https://pixi.sh/).

## Prerequisites

- [pixi](https://pixi.sh/) installed on your system
- For PAM authentication (default): a system user account

## Quick Start

1. **Install dependencies:**

   ```bash
   pixi install
   ```

2. **Run JupyterHub:**

   ```bash
   pixi run hub
   ```

3. **Open your browser** and navigate to http://localhost:8000

4. **Login** with your system username and password

## Available Tasks

| Task | Description |
|------|-------------|
| `pixi run hub` | Start JupyterHub |
| `pixi run hub-dev` | Start JupyterHub in debug mode |
| `pixi run generate-config` | Generate a full config file with all options |

## Configuration

Edit `jupyterhub_config.py` to customize your setup. Common configurations:

### Use DummyAuthenticator for Testing

For quick testing without system accounts, uncomment these lines in `jupyterhub_config.py`:

```python
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "password"
```

Then any username with password "password" will work.

### Change the Port

```python
c.JupyterHub.port = 8888
```

### Restrict Allowed Users

```python
c.Authenticator.allowed_users = {'alice', 'bob'}
c.Authenticator.admin_users = {'alice'}
```

## Project Structure

```
jupyter-pixi/
├── pixi.toml              # Pixi project configuration
├── jupyterhub_config.py   # JupyterHub configuration
└── README.md              # This file
```

## Generated Files

When running JupyterHub, these files may be created:

- `jupyterhub.sqlite` - User database
- `jupyterhub_cookie_secret` - Cookie secret file
- `jupyterhub-proxy.pid` - Proxy process ID

These are gitignored and safe to delete if you want to reset state.

## Resources

- [JupyterHub Documentation](https://jupyterhub.readthedocs.io/)
- [Pixi Documentation](https://pixi.sh/latest/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)



