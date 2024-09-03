import json

def filter_china_sentences(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    content = data.get('content', '')
    title = data.get('title', '')
    date = data.get('date', '')

    china_sentences = [sentence for sentence in content.split('. ') if 'China' in sentence]

    output_data = []
    for sentence in china_sentences:
        output_data.append({
            'title': title,
            'date': date,
            'sentence': sentence
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

# Example usage
filter_china_sentences('output.json', 'filtered_output.json')
