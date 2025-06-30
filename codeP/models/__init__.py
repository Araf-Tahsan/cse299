def get_model(name):
    if name == "dcgan":
        from .dcgan import DCGAN
        return DCGAN()
    elif name == "cgan":
        from .cgan import ConditionalGAN
        return ConditionalGAN(noise_dim=100,num_classes=10,img_channels=1,img_size=28)
    else:
        raise ValueError(f"Unknown model: {name}")
