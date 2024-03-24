import re

class ActivationTool:
    def __init__(self, file_path):
        self.file_path = file_path

    def activate_language(self):
        with open(self.file_path, 'r') as file:
            # Read BOMb code from file
            bomb_code = file.read()

            # Convert BOMb code to JavaScript
            js_code = self.convert_to_js(bomb_code)

            # Write JavaScript code to new file
            with open('activated_code.js', 'w') as js_file:
                js_file.write(js_code)

    def convert_to_js(self, bomb_code):
        # Placeholder implementation for conversion to JavaScript
        # You can implement the actual conversion logic here

        # Convert @property declarations
        bomb_code = re.sub(r'@property\("([^"]+)",\s*"([^"]+)"\);', r'element.style.\1 = "\2";', bomb_code)

        # Convert @eventListener declarations
        bomb_code = re.sub(r'@eventListener\("([^"]+)",\s*"([^"]+)",\s*function\(\)\s*{([^}]*)}\);', r'element.addEventListener("\1", function() {\3});', bomb_code)

        # Convert @selector declarations
        bomb_code = re.sub(r'@selector\("([^"]+)"\)\s*{([^}]*)}', r'document.querySelector("\1").style {\2}', bomb_code)

        return bomb_code

# Example usage
if __name__ == "__main__":
    tool = ActivationTool("src/bomb.js")
    tool.activate_language()
      
