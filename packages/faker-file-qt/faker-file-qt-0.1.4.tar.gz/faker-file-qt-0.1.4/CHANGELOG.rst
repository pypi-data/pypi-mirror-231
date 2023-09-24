Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.4
-----
2023-09-23

- Set minimal required version of faker-file to 0.17.8.
- Add selects for image, pdf and mp3 generator selection.

0.1.3
-----
2023-07-28

- Set minimal required version of faker-file to 0.17.2.
- Add menus.

0.1.2
-----
2023-07-26

- UI improvements.
- Added JSON file provider.
- Improved tests.

0.1.1
-----
2023-07-25

- UI improvements.
- Open default app on click on the results.

0.1
---
2023-07-24

- Initial beta release.
