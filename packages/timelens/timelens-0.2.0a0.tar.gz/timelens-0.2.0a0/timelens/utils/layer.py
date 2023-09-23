def get_cnn_layer(cnn, layer_name):
    """ Get the actual layer reference of a cnn layer

    Args:
        cnn (torch.nn.Module): Convolutional neural network
        layer_name (str): Name of the layer to get (example: 'conv_layers.conv0')

    Note:
        Make sure to use the complete name of a layer with all module dicts (Use cnn.named_modules to look them up)

    Returns:
        layer_ (torch.nn.Module): Requested CNN layer
    """
    layer_depth = layer_name.split('.')
    if len(layer_depth) == 1:
        return getattr(cnn, layer_name)
    else:
        layer_ = None
        for idx, layer in enumerate(layer_depth):
            layer_ = getattr(layer_, layer) if idx >= 1 else getattr(cnn, layer)
        return layer_
