# dcimg2btf
This is a script to convert files in the dcimg format from Hamamatsu Photonics to the btf format.

The dcimg format is a format that allows for fast writing, but it cannot be loaded in programs such as Fiji. Therefore, it was necessary to convert it to the more manageable btf format, and I implemented code to directly convert dcimg format to btf format. The conversion speed has been improved with some optimizations.

## Installation

1.Clone this repository in command line.
```bash
$ git clone https://github.com/MonmaNobuaki/dcimg2btf.git
```

2.Go into the repository.
$ cd dcimg2btf
