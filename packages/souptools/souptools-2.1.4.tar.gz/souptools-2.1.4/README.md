[![Donate via PayPal][donate-image]][donate-link]
[![Discord][discord-image]][discord-link]
[![Build][github-ci-image]][github-ci-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]
[![PyPI Downloads][pypi-down]][pypi-link]
[![PyPI - Python Version][python-image]][pypi-link]
![License][license-image-mit]

# Soup Sieve

## Overview

Soup Sieve is a CSS selector library designed to be used with [Beautiful Soup 4][bs4]. It aims to provide selecting,
matching, and filtering using modern CSS selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin select feature, and as of Beautiful Soup
version 4.7.0, it now is :confetti_ball:. Soup Sieve can also be imported in order to use its API directly for
more controlled, specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS draft specifications, though there are a
number that don't make sense in a non-browser environment. Selectors that cannot provide meaningful functionality simply
do not match anything. Some of the supported selectors are:

- `.classes`
- `#ids`
- `[attributes=value]`
- `parent child`
- `parent > child`
- `sibling ~ sibling`
- `sibling + sibling`
- `:not(element.class, element2.class)`
- `:is(element.class, element2.class)`
- `parent:has(> child)`

