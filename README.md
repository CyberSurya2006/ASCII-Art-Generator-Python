# ASCII-Art-Generator-Python

How to Use:
  1. Save this script as ascii_art.py
  2. Install Pillow if not already installed: pip install pillow
  3. Run it from the command line: python ascii_art.py path/to/your/image.jpg
  4. The script will output the ASCII art to the console.


Notes:
  →Supports common image formats (JPEG, PNG, etc.) via Pillow.
  →Adjust width in the function call for different resolutions.
  →For very large images, increase width for more detail, but it may slow down processing.


Fixing the "No Such File or Directory" Error:
  If you try to run the ASCII Generator script and see an error like:
  python: can't open file 'C:\Users<username>\ascii_art.py': [Errno 2] No such file or directory
  This means Python cannot find the ascii_art.py file in the location you are running it from. I faced the same issue while working on this project, so here is the fix.

  Why this happens:
    When you run "python ascii_art.py", Python looks for the file in your current working directory.
    If the file is saved somewhere else, Python reports that it cannot find it.
    The path shown in the error usually means you are running the command from the wrong folder or using the wrong file path.

  How to fix it:
    1. Create a folder such as: C:\Users<username>\Desktop\ASCII_Art.
    2. Save the Python file as: ascii_art.py inside that folder.
    3. Put your image (for example: photo.jpg) inside the same ASCII_Art folder. This avoids confusion with paths.
    4. Open Command Prompt or Press Win + R, type cmd, and press Enter.
    5. Then run: cd Desktop\ASCII_Art
    6. Run the Script: python ascii_art.py photo.jpg
    7. If the image file has spaces in its name: python ascii_art.py "my photo.jpg"
   The ASCII output should now appear in the console.
    
  Additional Notes:
    → Check Python installation using: python --version
    → Ensure the script is saved as .py and not .txt.
    → If permissions cause issues, try running Command Prompt as Administrator.
    → Test Python with a simple script like print("Hello") to verify it works.
    → If you still have issues, double-check:
        a) The exact command you typed.
        b) The full error message.
        c) The location of the .py script and the image file.
