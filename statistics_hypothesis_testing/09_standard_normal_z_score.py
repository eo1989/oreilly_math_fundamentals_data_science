def z_score(x, mean, std):
    return (x - mean) / std


def z_to_x(z, mean, std):
    return (z * std) + mean


mean = 6.0
std_dev = 1.0
x = 8.0

# Convert to Z-score and then back to X 
z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)

print(f"Z-Score: {z}")
print(f"Back to X: {back_to_x}")
