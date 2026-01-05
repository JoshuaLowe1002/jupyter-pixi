# JupyterHub configuration file
#
# For full configuration options, run:
#   pixi run generate-config
#
# Or see: https://jupyterhub.readthedocs.io/en/stable/reference/config-reference.html

c = get_config()  # noqa: F821

# =============================================================================
# Application settings
# =============================================================================

# The public facing URL of the whole JupyterHub application
# c.JupyterHub.bind_url = 'http://:8000'

# The ip address for the Hub process to *bind* to
c.JupyterHub.hub_ip = '127.0.0.1'

# The port for the Hub process to *bind* to
c.JupyterHub.hub_port = 8081

# The public facing port of the proxy
c.JupyterHub.port = 8000

# =============================================================================
# Spawner settings
# =============================================================================

# SimpleLocalProcessSpawner runs all user servers as the current process user
# This works in containerized/deployed environments where system users don't exist
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'

# The command used for starting the single-user server
c.Spawner.cmd = ['jupyterhub-singleuser']

# Default URL to redirect users to after login
c.Spawner.default_url = '/lab'

# Timeout for starting a server (in seconds)
c.Spawner.start_timeout = 60

# Each user gets their own notebook directory
c.Spawner.notebook_dir = '~/notebooks'

# =============================================================================
# Authenticator settings
# =============================================================================

# For local development, use the PAM authenticator (system users)
# This authenticates against system user accounts
# c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

# For simple testing without system accounts, use DummyAuthenticator:
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "password"

# Allow all authenticated users to access the hub
c.Authenticator.allow_all = True

# Allowed users (to restrict to specific users instead of allow_all)
# c.Authenticator.allowed_users = {'user1', 'user2'}

# Admin users
# c.Authenticator.admin_users = {'admin'}

# =============================================================================
# Security settings
# =============================================================================

# Generate a secure cookie secret (recommended for production)
# c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

# Proxy authentication token
# c.ConfigurableHTTPProxy.auth_token = 'your-secure-token-here'

# =============================================================================
# Database settings
# =============================================================================

# URL for the database. SQLite is the default
c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

# =============================================================================
# Logging
# =============================================================================

# Set the log level
c.JupyterHub.log_level = 'INFO'

