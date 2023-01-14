# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.4.1] - 2023-01-14
### Fixed
- itemcallnumber is optional, indeed not all books have that type of identifier

## [1.4.0] - 2022-12-17
### Added
- Add barcode and call number to loans list

## [1.3.0] - 2022-12-17
### Added
- Add command to renew loans, with `loans renew`. The new loans will be printed after the renewal.

## [1.2.0] - 2022-12-05
### Added
- Print the soonest due date of the users' loans in the table. This helps to find the date you have to go to the library.

## [1.1.0] - 2022-11-27
### Added
- Print loans of each user sequentially (previously, only the first user's loans were displayed)

## [1.0.1] - 2022-11-23
### Fixed
- Authentication was not properly working due to a new Session being created, thus losing cookies

## [1.0.0] - 2022-11-22
### Added
- Add CLI (command-line interface) to create a sample config, show the config and get loans
- Display loans in a pretty table
- Print the username when getting loans ("Loans of John Doe")
- Display due dates as date, not date with time

## [0.2.0] - 2022-10-25
### Added
- Ability to get the current loans of a user

### Changed
- Drop support of Python 3.7 - 3.9. Only support Python 3.10

## [0.1.0] - 2022-10-05
### Added
- Initial release

[Unreleased]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.4.1...master
[1.4.1]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.4.0...1.4.1
[1.4.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.3.0...1.4.0
[1.3.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/0.2.0...1.0.0
[0.2.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/tomsquest/mediathequeroubaix.py/tree/0.1.0
