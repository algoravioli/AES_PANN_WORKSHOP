#%%
import numpy as np

def area_of_rectangle(length, width):
    return length * width

def produce_data_for_rectangles(num_samples, high_val=100.0):
    x = np.array([])
    y = np.array([])
    for i in range(num_samples):
        # Generate random data for length and width
        length = np.random.uniform(low=0.0, high=high_val)
        width = np.random.uniform(low=0.0, high=high_val)
        # Calculate area
        area = area_of_rectangle(length, width)
        # x shape should be (num_samples, 2)
        x_curr = np.array([[length, width]])
        y_curr = np.array([area])
        if i == 0:
            x = x_curr
            y = y_curr
        else:
            x = np.vstack((x, x_curr))
            y = np.vstack((y, y_curr))
    return x, y

def train_test_split_np_array(x_array, y_array, split_ratio):
    
    # Split the data into training and testing data
    split_index = int(len(x_array) * split_ratio)
    x_train = x_array[0:split_index]
    y_train = y_array[0:split_index]
    x_test = x_array[split_index:-1]
    y_test = y_array[split_index:-1]
    return x_train, y_train, x_test, y_test

print("Helper functions loaded successfully!")



# %%
