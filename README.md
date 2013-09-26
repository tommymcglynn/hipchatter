hipchatter
==========

A sample project to help me understand how buildout works.

## Initial Setup

Prep and run [buildout](https://github.com/buildout/buildout) to satisfy application dependencies.

    $ python bootstrap.py
    $ bin/buildout

## Example

    $ bin/python
    >>> from hipchatter import messenger
    >>> messenger.send_joke('hipchat_api_key', 'hipchat_room_id')
