def readfile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
            return content.splitlines();
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found")
    except Exception as e:
        print(f"An error occured: {e}")

