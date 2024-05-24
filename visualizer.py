import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os

def visualize(f, title: str = None):
    #Transforms the input into a grid for example, [["FC","VC"],["VC","FC"]]
    grid = [line.strip().split("\t") for line in f] 

    # Assuming the images are in images directory and named 'FC.png', 'VC.png', etc.
    path_to_images = 'images/'
    
    fig, axs = plt.subplots(len(grid), len(grid[0]), figsize=(5, 5)) 
    if title != None:
        fig.canvas.manager.set_window_title(title)

    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    for ax in axs.flatten():
        ax.axis('off')

    for i, row in enumerate(grid):
        for j, img_code in enumerate(row):
            img_path = f"{path_to_images}{img_code}.png" 
            img = mpimg.imread(img_path) 
            axs[i, j].imshow(img) 
    return fig
def render():
    plt.show()

def usage():
  script_name = sys.argv[0]
  print(f"Usage:")
  print(f"\tpython {script_name} [files...]")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            try:
                f = open(file)
            except FileNotFoundError as e:
                print(f"{e}", file=sys.stderr)
                exit(1)
        for file in sys.argv[1:]:
            with open(file) as f:
                visualize(f, os.path.basename(file))
                plt.savefig("./diagrams/" + os.path.basename(file).replace(".out", ".out.png"))
                # plt.savefig("./diagrams/" + os.path.basename(file).replace(".txt", ".png"))
    else:
        visualize(sys.stdin)
        render()