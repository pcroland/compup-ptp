# compup-ptp
### Comparison uploader for PassThePopcorn.
## Installation
* `install -D -m 755 <(curl -fsSL git.io/JYTIj) ~/.local/bin/compup-ptp`\
(If you don' have `~/.local/bin` in your PATH, add `PATH="$HOME/.local/bin:$PATH"` to your `.bashrc`/`.zshrc`.)
* Add your API key in the script. (`nano ~/.local/bin/compup-ptp`)
* `hash -r`
## Usage
```sh
usage: compup-nc [-h] [-v] [-i [IMAGES [IMAGES ...]]] [-c COMPARES] [-n NUMBER] [-w WIDTH] [-o]

optional arguments:
  -h, --help            show help message
  -v, --version         show version
  -i [IMAGES [IMAGES ...]], --images [IMAGES [IMAGES ...]]
                        image sources. (default: *.png)
  -c COMPARES, --compares COMPARES
                        compare names, comma separated. (default: source, encode)
  -n NUMBER, --number NUMBER
                        number of images in a row. (default: number of compare names)
  -w WIDTH, --width WIDTH
                        width of the image row (default: 500)
  -o, --oxipng          use oxipng before uploading (default: False)
```
## How it works
![image1](https://i.kek.sh/dzAbsN5jT7d.gif)