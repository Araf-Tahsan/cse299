def get_dataset(name):
    if name == "CIFAR10":
        from .dcgan_dataset import load_data
        return load_data()
    elif name == "mnist":
        from .cgan_dataset import load_data
        return load_data()
    else:
        raise ValueError(f"Unknown dataset: {name}")
