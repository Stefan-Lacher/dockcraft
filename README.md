# DockCraft

DockCraft is a Python-based tool designed to format Dockerfiles according to best practices, making them clean, efficient, and easy to maintain. Whether you're working on a personal project or managing a fleet of containers in a production environment, DockCraft helps ensure your Dockerfiles are well-structured and follow industry standards.

## Why the Name "DockCraft"?

The name **DockCraft** is inspired by two key concepts:

- **Dock**: While we chose not to use "Docker" directly to avoid any potential trademark concerns, "Dock" is a subtle nod to the containerization ecosystem. It evokes the idea of docking ships—just as containers (whether Docker or other types) are docked and managed within their environments.

- **Craft**: This term emphasizes the idea of craftsmanship. Crafting something with care, precision, and attention to detail is central to what DockCraft does. It reflects the tool's mission to help developers create Dockerfiles that are not only functional but also optimized, clean, and aligned with best practices.

Together, **DockCraft** suggests a tool that helps you "craft" your container-related files with the same care and expertise you'd use in any well-crafted project.

## Features

- **Reorders Instructions**: DockCraft reorganizes Dockerfile instructions into a logical order according to best practices.
- **Combines RUN Commands**: Multiple `RUN` commands are combined where possible to minimize the number of layers and reduce image size.
- **Formats Dockerfiles**: The tool ensures consistent formatting, making your Dockerfiles easier to read and maintain.
- **Extensible**: Written in Python, DockCraft is easy to extend and customize to fit your specific needs.

## Installation

To install DockCraft, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/Stefan-Lacher/dockcraft.git
cd dockcraft
pip install -r requirements.txt
```

## Contributing to the project
If you want to contribute to the project, please read the following [document](CONTRIBUTING.md).

## License
DockCraft is licensed under the MIT License. The full text of the license can be found in the [LICENSE](LICENSE) file in this repository.
