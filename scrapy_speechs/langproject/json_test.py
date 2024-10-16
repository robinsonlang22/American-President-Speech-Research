import json

def test_read_fixed_obama_speech():
    input_file = '../final_json/deduplicated_canada.json'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("read success")
    except Exception as e:
        print(f"read failed: {e}")

if __name__ == "__main__":
    test_read_fixed_obama_speech()
