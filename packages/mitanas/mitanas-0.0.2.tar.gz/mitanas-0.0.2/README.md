# MITANAS
**M**ake **IT** **AN** **A**utostart **S**cript. Mitanas generates an executable from your project and 
configures it to boot along with the system.

## Key Features

- Executable Generation: **Mitanas** utilizes PyInstaller to generate executables from Python scripts. You can specify the project name and the path to the main script.

- Startup Configuration: In addition to executable generation, **Mitanas** also configures automatic startup of the executable with the operating system.

## Pre requisites
* Python 3.x
* Crontab (Linux)
* Linux | ~~Windows~~ (Coming soon)

## Basic Usage
Mitanas must be installed in the same environment that you want to configure in order to extract the project's dependencies with greater precision.
```python
from mitanas import Mitanas

# Create an instance of Mitanas with the project name and the path to the main script.
mitanas = Mitanas("my_project", "my_script.py")

# Generate the executable and configure automatic startup.
executable_path = mitanas.configure()
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.