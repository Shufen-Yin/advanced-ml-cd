import torch
import torch.nn as nn

# Define a minimalist neural network model for the assignment
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        # Define a linear layer (assuming 10 input features and 1 output)
        self.layer = nn.Linear(10, 1)

    def forward(self, x):
        return self.layer(x)

# Initialize the model
model = SimpleModel()

# Create dummy input data to define the input shape (Batch Size 1, 10 Features)
dummy_input = torch.randn(1, 10)

# Export the model to ONNX format as required by Part 2
# This generates the 'sentiment_model.onnx' file needed for the CI/CD pipeline
torch.onnx.export(
    model,
    dummy_input,
    "sentiment_model.onnx",
    export_params=True,
    opset_version=10,
    do_constant_folding=True,
    input_names=['input'],
    output_names=['output']
)

print("Successfully created sentiment_model.onnx!")
