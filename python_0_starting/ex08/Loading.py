import os


def ft_tqdm(lst: range) -> None:

    size_of_terminal = os.get_terminal_size().columns - 40

    for i, item in enumerate(lst, 1):
        bar_formula = (i * size_of_terminal // len(lst))
        percentage = (i * 100) // len(lst)
        progress_bar = f"{'=' * bar_formula:<{size_of_terminal}}"  
        print(f'\r{percentage:>3}%|{progress_bar}| {i}/{len(lst)}', end='',
              flush=True)
        yield i
