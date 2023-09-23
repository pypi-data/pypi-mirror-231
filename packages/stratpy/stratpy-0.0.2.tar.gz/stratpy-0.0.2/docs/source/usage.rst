Usage
=====

.. _installation:

Installation
------------

To use stratpy, first install it using pip:

.. code-block:: console

   $ pip install stratpy

Creating games
----------------

To create a new game use the ``Game()`` constructor:

.. autofunction:: statpy.Game()

Optional parameters:
``title:`` title of the game which will be used during export.
``players:`` number of players in the game (default is 2)
``gametype:`` The type of game you want to model. Either Type.Normal for normal form games
 displayed in a matrix or Type.Extensive for extensive form games using tree structures.

For example:

>>> from stratpy import *
>>> my_game = Game(title:"My Game", players:2, gametype:Type.Normal)



Variables
----------------

.. autofunction:: statpy.Variable()
To create variables to be used for the players utility, use the ``Variable()`` constructor.

Variables require a name parameter used when displaying the payout.
``name:`` name of the variable as a string (e.x. "X")

Preference between variable utility can be ordered using the '>' and '==' operators.

For example:

>>> a = Variable("A")
>>> b = Variable("B")
>>> c = Variable("C")
>>> a > b == c

This results in players preferring a over b and c, and being indifferent to b and c.

