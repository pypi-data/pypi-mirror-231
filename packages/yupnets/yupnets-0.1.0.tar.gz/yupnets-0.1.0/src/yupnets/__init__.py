from . import resnet
from . import utils

__all__ = [
    "load_net",
]


def load_net(
        net: str,
        **kwargs,
):
    if net in resnet.nets:
        model = resnet.resnet_loader(net=net, **kwargs)

    else:
        raise ValueError(f"Unsupported net: {net}")

    return model
