# Convertico

Convertico is a tool for converting image files to ICO format. This tool allows you to easily convert PNG, JPG, JPEG, or SVG files to ICO format directly from the context menu in Windows.

## Installation

To set up Convertico on your machine and enable the context menu option, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git or download it as a ZIP file and extract it.

2. **Install Dependencies**: Ensure you have Python installed on your machine. This tool requires the `requests` library, which you can install using pip:

`pip install requests`


3. **Configure Context Menu Entry**:
- Navigate to the `Convertico` directory where you cloned or extracted the repository.
- Open `convertico_context_menu_registration.reg` file with a text editor.
- Modify the path in the `command` key to point to the location of your `convertico.bat` file.
- Double-click on `convertico_context_menu_registration.reg` to add the context menu entry to your registry. Confirm any prompts that appear.

4. **Usage**:
- Now you can right-click on any PNG, JPG, JPEG, or SVG file in Windows File Explorer.
- Select "Convert to ICO" from the context menu to convert the file to ICO format.
- The ICO file will be saved in the same directory as the original image file.

5. **Customization**:
- If you want to change the icon associated with the context menu entry, you can replace the `convertico.ico` file with your desired icon. Ensure the icon file is named `convertico.ico`.

## Troubleshooting

- If the context menu entry does not appear after double-clicking `convertico_context_menu_registration.reg`, try restarting Windows Explorer or restarting your computer.
- Ensure that Python is added to your system PATH to execute the script from any directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

