# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.1.0...master
[1.1.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/tomsquest/mediathequeroubaix.py/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/0.2.0...1.0.0
[0.2.0]: https://github.com/tomsquest/mediathequeroubaix.py/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/tomsquest/mediathequeroubaix.py/tree/0.1.0
