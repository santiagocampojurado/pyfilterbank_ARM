# PyFilterbank 
## Filter Banks and Acoustics Tools Package for Python
This package provides filter banks, and other useful tools for the daily work of the acoustician.

The main features are:

* Fractional octave filter bank (applies to IEC-61260:1995)

* Spectral weighting filters (IEC 61672:2003)
  + A-Weighting
  + B- and C-weighting

* Mel-Frequency filterbank (Triangular Filterbank)
  + as Transformation matrix
  + planned: with STFT

* Second order section / biquad filters and filter design
  + Butterworth SOS
  + RBJ audio EQ filter design module

* Gammatone filter bank


## Documentation
The [Documentation](http://siggigue.github.io/pyfilterbank) is placed on github pages and can be found [here](http://siggigue.github.io/pyfilterbank).

## Installation

### From GitHub (Local Source)

If you want the latest features or need to compile for a specific architecture (e.g., Raspberry Pi ARM):

1. Clone the repo:
   ```sh
   git clone https://github.com/SiggiGue/pyfilterbank.git
   cd pyfilterbank


2. Via `pip`:
  ```pip install .```

This will automatically build and install the sosfilt C extension for your platform.

### Alternative: Directly from GitHub

To install, `pip install git+https://github.com/SiggiGue/pyfilterbank.git`.

But if you're on a platform without a matching precompiled .so, pip will compile sosfilt.c during installation (assuming you have a C compiler installed).

### Raspberry Pi / ARM Notes

If you’re on a Raspberry Pi:

  1. Ensure you have the necessary build tools:
  ```sh
  sudo apt-get update
  sudo apt-get install -y build-essential python3-dev
  ```

  2. Then clone this repo or install via the Git link. The setup.py script will compile sosfilt.c locally.

## Status
This Project is in development status, be aware of that. If you find some bugs or if you want to help, just go for it and join!

## License
The 4 clause BSD License applies.

