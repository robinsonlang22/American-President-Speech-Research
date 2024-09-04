import json

def test_read_fixed_obama_speech():
    input_file = '../final_json/42_cliton_speech.json'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("读取成功")
    except Exception as e:
        print(f"读取失败: {e}")

if __name__ == "__main__":
    test_read_fixed_obama_speech()
