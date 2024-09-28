import numpy as np
from pprint import pprint

def calculate(input_list):
    if len(input_list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(input_list).reshape(3, 3)

    # Calculate the statistics
    calculations = {
        "mean": [[np.mean(arr[i]) for i in range(arr.shape[0])], 
                 [np.mean(arr[:, j]) for j in range(arr.shape[1])], 
                 np.mean(arr)],
        "variance": [[np.var(arr[i]) for i in range(arr.shape[0])], 
                     [np.var(arr[:, j]) for j in range(arr.shape[1])], 
                     np.var(arr)],
        "standard deviation": [[np.std(arr[i]) for i in range(arr.shape[0])], 
                               [np.std(arr[:, j]) for j in range(arr.shape[1])], 
                               np.std(arr)],
        "max": [[np.max(arr[i]) for i in range(arr.shape[0])], 
                [np.max(arr[:, j]) for j in range(arr.shape[1])], 
                np.max(arr)],
        "min": [[np.min(arr[i]) for i in range(arr.shape[0])], 
                [np.min(arr[:, j]) for j in range(arr.shape[1])], 
                np.min(arr)],
        "sum": [[arr.sum(axis=0).tolist(), 
                 arr.sum(axis=1).tolist(), 
                 arr.sum().item()]]
    }

    return calculations

def get_matrix_input():
    print("Do you want to enter the matrix as a whole or row by row? (Enter 'whole' or 'row')")
    choice = input().strip().lower()
    
    if choice == 'whole':
        print("Please enter the 9 numbers separated by spaces:")
        input_numbers = list(map(float, input().strip().split()))
        return calculate(input_numbers)
    
    elif choice == 'row':
        matrix = []
        for i in range(3):
            row = input(f"Enter row {i+1} (3 numbers separated by spaces): ")
            numbers = list(map(float, row.strip().split()))
            if len(numbers) != 3:
                print("Each row must contain exactly 3 numbers. Please try again.")
                return get_matrix_input()  # Restart the input process
            matrix.append(numbers)
        flat_list = [num for sublist in matrix for num in sublist]  # Flatten the list
        return calculate(flat_list)
    
    else:
        print("Invalid choice. Please enter 'whole' or 'row'.")
        return get_matrix_input()  # Restart the input process

# Run the program
if __name__ == "__main__":
    results = get_matrix_input()
    pprint(results)  
