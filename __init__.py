"""Set version and register the plugin."""
__version__ = "0.0.1"

# ============================================================================
# The following statements are required to register this 3rd party plugin:
# ============================================================================
from .blackplugin import Black as PLUGIN_CLASS  # noqa
