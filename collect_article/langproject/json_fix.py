import re

def fix_json_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # use regex to add comma between objects
    fixed_content = re.sub(r'}\s*{', '},\n{', content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

if __name__ == "__main__":
    # 需要修改文件名
    input_file = 'cliton_speech.json'
    output_file = 'fixed_cliton_speech.json'
    fix_json_format(input_file, output_file)

