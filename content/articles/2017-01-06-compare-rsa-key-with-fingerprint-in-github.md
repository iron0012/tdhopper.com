Title: Compare RSA Key with Fingerprint in Github
Category: Today I Learned
Date: 2017-01-06

When you add an SSH key to your Github account, Github shows you the hexadecimal form of the MD5 hash of your public key.

If you ever need to compare that against a key file on your computer, you can run:

```
ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub
```

I learned this from [StackOverflow](http://stackoverflow.com/a/32130465/982745).