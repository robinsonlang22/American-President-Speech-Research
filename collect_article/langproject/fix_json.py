import re

def fix_json_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式在每个对象之间添加逗号
    fixed_content = re.sub(r'}\s*{', '},\n{', content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

if __name__ == "__main__":
    input_file = 'truman_speech.json'
    output_file = 'fixed_truman_speech.json'
    fix_json_format(input_file, output_file)

