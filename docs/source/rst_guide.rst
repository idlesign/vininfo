RST Quick guide
===============

Online reStructuredText editor - http://rst.ninjs.org/


Main heading
============


Secondary heading
-----------------

Minor heading
~~~~~~~~~~~~~


Typography
----------

**Bold**

`Italic`

``Accent``



Blocks
------

Double colon to consider the following paragraphs preformatted::

    This text is preformated. Can be used for code samples.


.. code-block:: python

    # code-block accepts language name to highlight code
    # E.g.: python, html
    import this


.. note::

    This text will be rendered as a note block (usually green).


.. warning::

    This text will be rendered as a warning block (usually red).



Lists
-----

1. Ordered item 1.

  Indent paragraph to make in belong to the above list item.

2. Ordered item 2.


+ Unordered item 1.
+ Unordered item .



Links
-----

:ref:`Documentation inner link label <some-marker>`

.. _some-marker:


`Outer link label <http://github.com/idlesign/makeapp/>`_

Inline URLs are converted to links automatically: http://github.com/idlesign/makeapp/


Images
------

.. image:: path_to_image/image.png


Automation
----------

http://sphinx-doc.org/ext/autodoc.html

.. automodule:: my_module
   :members:

.. autoclass:: my_module.MyClass
    :members: do_this, do_that
    :inherited-members:
    :undoc-members:
    :private-members:
    :special-members:
    :show-inheritance:

