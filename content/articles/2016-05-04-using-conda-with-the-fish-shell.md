Title: Using Conda with the Fish Shell
Category: Today I Learned
Date: 2016-05-04

I'm trying out the beautiful [Fish shell](https://fishshell.com/). I've been a Bash user up until now.

I was bummed to see that `source activate ENV` (for activating [Conda environments](http://conda.pydata.org/docs/using/envs.html "Managing environments &mdash; Conda   documentation")) didn't work natively in Fish.

Apparently the [Conda team is adding native support for Fish](https://groups.google.com/a/continuum.io/d/msg/conda/8aaYESlLZI8/Ov1UcFhWCAAJ), but it's not available as of 2016-05-04.

There are several projects developed to help in the meantime:

* [conda-workon](http://pypi.python.org/pypi/conda-workon/0.3.0)
* [fish-conda-virtualenv](https://github.com/fabioramponi/fish-conda-virtualenv)
* [condactivate](https://gist.github.com/jiffyclub/9679788)

I'm going to wait for the Conda update to be released.
