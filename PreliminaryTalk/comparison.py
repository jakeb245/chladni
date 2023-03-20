from src.compare import compare_images, add_figures
import matplotlib.pyplot as plt


def get_filenames(freq):
    exp_name = f"/Users/jakebuchanan/code/chladni/data/figure_{freq}.png"
    theo_name = f"/Users/jakebuchanan/code/chladni/PreliminaryTalk/model_{freq}.PNG"

    return exp_name, theo_name


if __name__ == '__main__':
    freq_list = [445, 2212, 3020, 3926, 1600, 582]

    for freq in freq_list:
        exp, theo = get_filenames(freq)
        error = compare_images(exp, theo)
        added = add_figures(exp, theo)
        print(f"Error for f = {freq} = {error}")

        fig = plt.figure()
        plt.axis('off')
        plt.imshow(added)
        plt.savefig(f"/Users/jakebuchanan/code/chladni/PreliminaryTalk/{freq}_added.png", bbox_inches='tight',
                    pad_inches=0, dpi=200)
