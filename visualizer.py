import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

def visualize(f):
    #Transforms the input into a grid for example, [["FC","VC"],["VC","FC"]]
    grid = [line.strip().split("\t") for line in f] 

    # Assuming the images are in images directory and named 'FC.png', 'VC.png', etc.
    path_to_images = 'images/'

    
    fig, axs = plt.subplots(len(grid), len(grid[0]), figsize=(5, 5)) 

    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    for ax in axs.flatten():
        ax.axis('off')

    for i, row in enumerate(grid):
        for j, img_code in enumerate(row):
            img_path = f"{path_to_images}{img_code}.png" 
            img = mpimg.imread(img_path) 
            axs[i, j].imshow(img) 

    plt.show()

if __name__ == "__main__":
    visualize(sys.stdin)