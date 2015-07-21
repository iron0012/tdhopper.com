Title: New Post Function for Bash
Date: 2015-07-21 11:02
Slug: new-post-function-for-bash
Tags: pelican, blogging, bash

On of the things I don't like about using a static site generator is the friction required for creating a new post. I've often end up posting things to Twitter that I would prefer to be more permanent simply because of the ease of tweeting.

To that end, I created a quick Bash function [to create a new post for me](https://github.com/tdhopper/dotfiles/blob/6b793abde7ca9aa1e75c57b1f98f77f4b2a177a4/bash_functions#L1-L26). Creating this post in my Pelican directory only requires typing

```
new-post "New Post Function for Bash"
```

Combined with Greg Reda's [Travis CI](http://stiglerdiet.com/blog/2015/Mar/27/auto-deploying-stigler-diet-with-travis-ci/) trick, the friction in getting a new post online is greatly reduced.

