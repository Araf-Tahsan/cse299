def get_dataset(name):
    if name == "gan_dataset":
        from .gan_dataset import load_data
        return load_data()
    # other datasets...
    raise ValueError(f"Unknown dataset: {name}")
