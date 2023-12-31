import csv
import json

def convert_file(csv_file, json_file, model):
    with open(csv_file, encoding='utf-8') as f:
        result = []
        for row in csv.DictReader(f):
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                if row['is_published'] == 'FALSE':
                    row['is_published'] = False
            result.append({'model': model, 'fields': row})
    with open(json_file, "w", encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    convert_file('ads.csv', 'ads.json', 'ads.ad')
    convert_file('categories.csv', 'categories.json', 'ads.category')
