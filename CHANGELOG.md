# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2024-08-14
### Added
- Feature: DockCraft Input Parser
    - path: For adding the path where to search for Dockerfiles.
    - verbose: For having more log output. If you set it you change the mode from info to debug.
    - recursive: Search for Dockerfiles recursively in subdirectories.
### Changed
- Changed the main pipeline:
    - adjusted init with the DockCraft Input Parser
- Changed for logging:
    - main pipeline
    - Dockerfile Reader
    - Dockerfile Finder
### Removed
- print statements

## [0.3.0] - 2024-08-14
### Added
- Feature: DockCraft File Finder
### Changed
- Changed the main pipeline:
    - added the DockCraft File Finder to the init
    - added the DockCraft Reader to the init

## [0.2.0] - 2024-08-14
### Added
- Feature: DockCraft Reader
- Created the first iteration of the main pipeline
### Removed
- Removed mock tests for Pipeline Setup

## [0.1.0] - 2024-08-13
### Added
- Initial project setup.
- Basic `Makefile` for managing tasks.
- Initial `README.md`, `LICENSE`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`.
- Setup for code formatting, linting, and testing.
- Github Action Pipeline for Code Quality and Testing
