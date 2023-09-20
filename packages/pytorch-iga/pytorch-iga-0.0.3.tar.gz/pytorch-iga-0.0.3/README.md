This is a PyTorch implementation of the Inter-environmental Gradient Alignment algorithm proposed by Koyama and Yamaguchi in their paper [Out-of-Distribution Generalization
with Maximal Invariant Predictor](https://arxiv.org/pdf/2008.01883v1.pdf)

## Quick start
Install pytorch-iga in the terminal:
```bash
pip install pytorch-iga
```

Import IGA in python:

```python
from iga import IGA
```

IGA is defined with the following parameters:

```python
IGA(model, optimizer, criterion, data, num_epochs, batch_size, lamda, verbose=10, device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),
)
```

Parameters:
>    model (torch.nn.Module): neural network model to be trained/tuned
    optimizer (torch.optim): pytorch optimizer object such as torch.optim.SGD
    criterion (function): loss function for model evaluation
    data (list(torch.utils.Dataset)): a list of Datasets for each environment
    num_epochs (int): number of training epochs
    batch_size (int): number of data points per batch
    lamda (float): importance weight of inter-environmental variance
    verbose (int): number of iterations in each progress log
    device (torch.device): optional, torch.device object, defaults to 'cuda' or 'cpu'

Returns:
>    model (torch.nn.Module): updated torch model
    IGA_loss (float): ending loss value
    
## Example
to be continued...