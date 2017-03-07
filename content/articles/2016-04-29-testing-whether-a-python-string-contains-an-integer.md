Title: Testing whether a Python string contains an integer
Date: 2016-04-29
Category: til
Tags: python

If you want to check whether a Python string contains a integer, you can try casting to an int with `int()` and catching the `ValueError` if it's not an integer. Alternatively, you can use the [`str.isdigit()`](https://docs.python.org/2/library/stdtypes.html#str.isdigit) method. It will "return true if all characters in the string are digits and there is at least one character, false otherwise." However, `isdigit` will only work for positive integers (and for those in base-10 or lower).


Thanks to [Jeremy Kahn for reminding me](https://twitter.com/trochee/status/726162607460114433) that `isdigit` only detects positive integers.

