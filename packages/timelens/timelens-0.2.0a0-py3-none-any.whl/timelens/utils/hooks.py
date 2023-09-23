from .layer import get_cnn_layer


def layer_hook(act_dict, layer_name):
    """Add a hook to a specific layer of a CNN and save the activations to the given dictionary

    Args:
        act_dict (dict): Used to save the activations at the key `layer_name`
        layer_name (str): Specifies to layer where the hook is being attached
    Returns:
        callable: function that adds a hook to the given module
    """

    def hook(module, input, output):
        act_dict[layer_name] = output

    return hook


def attach_hooks_to_layer(cnn, act_dict, layer_name):
    """
    Args:
        cnn (torch.nn.Module): Convolutional neural network used for the process
        act_dict (dict): Used to save activations at the key `layer_name`
        layer_name (str): Layer where the hook should be attached

    Returns:
        None
    """
    layer = get_cnn_layer(cnn, layer_name)
    layer.register_forward_hook(layer_hook(act_dict, layer_name))


def attach_hooks_to_all_layers(cnn, act_dict, modules):
    """
    Args:
        cnn (torch.nn.Module): Convolutional neural network used for the process
        act_dict (dict): Used to save activations at the key `layer_name`
        modules (list[torch.nn.Module]):

    Returns:
        None
    """
    for name, layer in cnn.named_modules():
        attach_hook = False
        for module in modules:
            if isinstance(layer, module):
                attach_hook = True
                break
        if attach_hook:
            layer.register_forward_hook(layer_hook(act_dict, name))
