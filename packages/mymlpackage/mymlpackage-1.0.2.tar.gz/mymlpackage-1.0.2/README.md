This is my custom ML package based on the
[scikit-learn](https://scikit-learn.org/stable/) library. It contains the
following modules:

- PCA library
- SVD library
- K-means library
- K-medoids library
- t-SNE library

# My ML package (mymlpackage):

This is a simple package that contains some useful functions for machine
learning, to practice an experiment in the ML course from the University of
Antioquia.

for mor information about the package, please visit the
[documentation](https://pypi.org/project/mymlpackage/#files)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this
package.

```bash
pip install mymlpackage
```

## Usage example

```python
import mymlpackage as mp

mp.KMeans(X, k, max_iter, tol)
mp.KMedoids(X, k, max_iter, tol)
mp.svd(X)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

```CMD
Copyright (c) 2023 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Authors

Name: Lina María Beltrán Durango

E-mail: linam.beltran@udea.edu.co
