import json
from datetime import datetime

# 假设你有一个字典来映射日期范围到总统名称
presidents_by_date = {
    ('1789-04-30', '1797-03-04'): 'George Washington',
    ('1797-03-04', '1801-03-04'): 'John Adams',
    ('1801-03-04', '1809-03-04'): 'Thomas Jefferson',
    ('1809-03-04', '1817-03-04'): 'James Madison',
    ('1817-03-04', '1825-03-04'): 'James Monroe',
    ('1825-03-04', '1829-03-04'): 'John Quincy Adams',
    ('1829-03-04', '1837-03-04'): 'Andrew Jackson',
    ('1837-03-04', '1841-03-04'): 'Martin Van Buren',
    ('1841-03-04', '1841-04-04'): 'William Henry Harrison',
    ('1841-04-04', '1845-03-04'): 'John Tyler',
    ('1845-03-04', '1849-03-04'): 'James K. Polk',
    ('1849-03-04', '1850-07-09'): 'Zachary Taylor',
    ('1850-07-09', '1853-03-04'): 'Millard Fillmore',
    ('1853-03-04', '1857-03-04'): 'Franklin Pierce',
    ('1857-03-04', '1861-03-04'): 'James Buchanan',
    ('1861-03-04', '1865-04-15'): 'Abraham Lincoln',
    ('1865-04-15', '1869-03-04'): 'Andrew Johnson',
    ('1869-03-04', '1877-03-04'): 'Ulysses S. Grant',
    ('1877-03-04', '1881-03-04'): 'Rutherford B. Hayes',
    ('1881-03-04', '1881-09-19'): 'James A. Garfield',
    ('1881-09-19', '1885-03-04'): 'Chester A. Arthur',
    ('1885-03-04', '1889-03-04'): 'Grover Cleveland',
    ('1889-03-04', '1893-03-04'): 'Benjamin Harrison',
    ('1893-03-04', '1897-03-04'): 'Grover Cleveland',
    ('1897-03-04', '1901-09-14'): 'William McKinley',
    ('1901-09-14', '1909-03-04'): 'Theodore Roosevelt',
    ('1909-03-04', '1913-03-04'): 'William Howard Taft',
    ('1913-03-04', '1921-03-04'): 'Woodrow Wilson',
    ('1921-03-04', '1923-08-02'): 'Warren G. Harding',
    ('1923-08-02', '1929-03-04'): 'Calvin Coolidge',
    ('1929-03-04', '1933-03-04'): 'Herbert Hoover',
    ('1933-03-04', '1945-04-12'): 'Franklin D. Roosevelt',
    ('1945-04-12', '1953-01-20'): 'Harry S. Truman',
    ('1953-01-20', '1961-01-20'): 'Dwight D. Eisenhower',
    ('1961-01-20', '1963-11-22'): 'John F. Kennedy',
    ('1963-11-22', '1969-01-20'): 'Lyndon B. Johnson',
    ('1969-01-20', '1974-08-09'): 'Richard Nixon',
    ('1974-08-09', '1977-01-20'): 'Gerald Ford',
    ('1977-01-20', '1981-01-20'): 'Jimmy Carter',
    ('1981-01-20', '1989-01-20'): 'Ronald Reagan',
    ('1989-01-20', '1993-01-20'): 'George H. W. Bush',
    ('1993-01-20', '2001-01-20'): 'Bill Clinton',
    ('2001-01-20', '2009-01-20'): 'George W. Bush',
    ('2009-01-20', '2017-01-20'): 'Barack Obama',
    ('2017-01-20', '2021-01-20'): 'Donald Trump',
    ('2021-01-20', '2025-01-20'): 'Joe Biden',
}

def get_president_by_date(date):
    for date_range, president in presidents_by_date.items():
        start_date, end_date = date_range
        if start_date <= date <= end_date:
            return president
    return 'Unknown'  # 如果没有匹配的日期范围，返回 'Unknown'

def update_presidents_in_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)  # 读取整个文件并解析为JSON数组

    for item in data:
        date = item.get('date')
        if date:
            item['president'] = get_president_by_date(date)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = 'fixed_output.json'
    output_file = 'updated_output.json'
    update_presidents_in_json(input_file, output_file)

