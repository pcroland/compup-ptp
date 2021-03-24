# compup-ptp
### Comparison uploader for PassThePopcorn.
## Installation
* `pip install requests`
* `install -D -m 755 <(curl -fsSL git.io/JYTIj) ~/.local/bin/compup-ptp`\
(If you don' have `~/.local/bin` in your PATH, add `PATH="$HOME/.local/bin:$PATH"` to your `.bashrc`/`.zshrc`.)
* Add your API key in the script. (`nano ~/.local/bin/compup-ptp`)
* `hash -r`
## Usage
```sh
usage: compup-ptp [-h] [-v] [-i [IMAGES [IMAGES ...]]] [-c COMPARES] [-o]

optional arguments:
  -h, --help            Shows this help message.
  -v, --version         Shows version.
  -i [IMAGES [IMAGES ...]], --images [IMAGES [IMAGES ...]]
                        image sources. (default: *.png)
  -c COMPARES, --compares COMPARES
                        compare names, comma separated. (default: source, encode) (default: source, encode)
  -o, --oxipng          use oxipng before uploading. (default: false) (default: False)
```
## How it works
![image1](https://i.kek.sh/dzAbsN5jT7d.gif)
