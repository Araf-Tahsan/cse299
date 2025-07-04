import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

def load_data(batch_size=64, img_size=28):
    transform = transforms.Compose([
        transforms.Resize(img_size),
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5])
    ])
    dataset = torchvision.datasets.MNIST(
        root='./DATA/cgan_dataset/training/data',
        train=True,
        download=True,
        transform=transform
    )
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=2 if torch.cuda.is_available() else 0
    )
    return dataloader