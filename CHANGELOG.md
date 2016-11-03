# Release 0.2.0 - Thursday 3 November  23:49:32 AEDT 2016

- Allow user to set XML encoding (#6)
  - Added encoding parameter to to_xml
  - Changed default encoding to UTF-8.
  - Added XMLModel attribute xml_encoding with default 'UTF-8'.
  - Added docs detailing how to set the encoding.
- Ensure deeply nested lists are traversed even if the parent is OK. (#5)
  - Test schematics serialized_name BaseType feature.

# Release 0.1.2 - Wednesday 2 November  23:13:48 AEDT 2016

- Support lists with a single item in XML being converted to raw_data with a list not dict. (#2)
- Set reports no in pylintrc (#1)
- Removed keyword only args from to_xml function for py 3.3/3.4 support. (#3)

# Release 0.1.1 - Wednesday 2 November  08:02:07 AEDT 2016

- Fixed travis YAML file parse error
- Allow travis failures for pypy and pypy3
- Added pytest-cov
- Fixed pylint issue with __init__ import
- Cleaned up test requirements

# Release 0.1.0 - Wed Nov 2 07:55:01 EST 2016

- Initial release

