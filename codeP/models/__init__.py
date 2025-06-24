def get_model(name):
    if name == "resnet":
        from .resnet import ResNet
        return ResNet()
    elif name == "gan":
        from .gan import GAN
        return GAN()
    # ... Add others here
    raise ValueError(f"Unknown model: {name}")
