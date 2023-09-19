import importlib
import os
from pipeless_ai.lib.logger import logger
from pipeless_ai.lib.app.app import PipelessApp

def load_plugin_module(path):
    spec = importlib.util.spec_from_file_location('plugin', path)
    plugin_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plugin_module)
    Plugin = getattr(plugin_module, 'PipelessPlugin')
    plugin_instance = Plugin()
    return plugin_instance

def inject_plugins(user_app: PipelessApp, plugins_dir : str, plugins_order: list[str]):
    '''
    Creates the tuple with the plugins sorted in execution order
    '''
    # TODO: since plugins are PipelessApps, we should allow a plugin with other plugins as dependencies and execute them recursively. The main plugin would need to specify dependencies as well on its metadata.
    exec_graph = () # A tuple of plugins IDs representing the plugins execution order
    for plugin_id in plugins_order:
        plugin_file_path = os.path.join(plugins_dir, plugin_id, 'plugin.py')
        if os.path.exists(plugin_file_path):
            plugin_instance = load_plugin_module(plugin_file_path)
            exec_graph += (plugin_id,)
            # Insert plugin into the user app so the user have access to plugin defined methods
            setattr(user_app.plugins, plugin_id, plugin_instance)
            # TODO: inject the plugin version under plugin_id.version. To have the plugin version on the
            #  plugin directory we have to create the metadata file when installing the plugin and add it
            #  to the plugin dir. This avoids the developer duplicating metadata in their repo and in the registry
            logger.info(f'Loaded plugin with id: {plugin_id}')
        else:
            logger.warning(f"[red]The plugin with ID '{plugin_id}' is not in the plugins directory: '{plugins_dir}'. Ignoring plugin.[/red]")

    user_app._PipelessApp__plugins_exec_graph = exec_graph

def exec_hook_with_plugins(user_app, hook_name, frame=None):
    '''
    Execute a Pipeless hook chaining all the plugins hooks in the order of the exec graph
    '''
    method_name = f'_PipelessApp__{hook_name}'
    for plugin_id in user_app._PipelessApp__plugins_exec_graph:
        plugin_instance = getattr(user_app.plugins, plugin_id)
        callable_method = getattr(plugin_instance, method_name)
        frame = callable_method(frame) if frame is not None else callable_method()

    callable_method = getattr(user_app, method_name)
    frame = callable_method(frame) if frame is not None else callable_method()
    return frame # Will return None when the frame is not passed. The hooks that do not return frames do no have return values