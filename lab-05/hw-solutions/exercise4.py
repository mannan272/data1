import numpy as np
import matplotlib.pyplot as plt

# creating two numpy array associated to x_train and y_train 
x_train = np.array([1,2,3])
y_train = np.array([2,3,6])
type(x_train)

# checking dimensions of the two arrays
print(x_train.shape,y_train.shape)

# Reshaping x_train and y_train
x_train = x_train.reshape(3,1)
y_train = y_train.reshape(3,1)

# checking the new dimensons of x_train and y_train
print(x_train.shape, y_train.shape)

# Making a simple scatterplot
plt.scatter(x_train,y_train)

# defining a function to create a nice scatterplot
def nice_scatterplot(x, y, title):
    # font size
    f_size = 18
    
    # making the figure
    fig, ax = plt.subplots(1,1, figsize=(8,5)) # Create figure object

    # setting axes limits to make the scale nice
    ax.set_xlim(np.min(x)-1, np.max(x) + 1)
    ax.set_ylim(np.min(y)-1, np.max(y) + 1)

    # adjusting size of tickmarks in axes
    ax.tick_params(labelsize = f_size)
    
    # removing tick labels
    ax.tick_params(labelbottom=False,  bottom=False)
    
    # adjusting size of axis label
    ax.set_xlabel(r'$x$', fontsize = f_size)
    ax.set_ylabel(r'$y$', fontsize = f_size)
    
    # setting figure title label
    ax.set_title(title, fontsize = f_size)

    # setting up a personalised grid  
    ax.grid(True, lw=1.75, ls='--', alpha=0.15)

    # making actual plot (Notice the label argument!)
    ax.scatter(x, y, label=r'$my\,points$')
    
    # adding a legend
    ax.legend(loc='best', fontsize = f_size);
    
    return ax

nice_scatterplot(x_train, y_train, 'Nice Scatterplot')
