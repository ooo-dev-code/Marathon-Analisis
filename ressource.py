import kagglehub

# Download latest version
path = kagglehub.dataset_download("aiaiaidavid/the-big-dataset-of-ultra-marathon-running")

print("Path to dataset files:", path)