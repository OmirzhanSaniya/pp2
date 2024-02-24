import re
import csv

with open("row.txt", "r",encoding="utf8") as f:
    text = f.read()

data = {
    'БИН': re.search(r"БИН (\d+)", text),
    'НДС Серия': re.search(r"НДС Серия (\d+)", text),
    'Чек №': re.search(r"Чек №(\d+)", text),
    'ИТОГО': re.search(r"ИТОГО:\n(.+)", text),
    'НДС 12%': re.search(r"в т\.ч\. НДС 12%:\n(.+)", text),
    'Фискальный признак': re.search(r"Фискальный признак:\n(.+)", text),
    'Время': re.search(r"Время: (.+)", text),
    'Место': re.search(r"(г\..+)", text),
    'Оператор фискальных данных': re.search(r"Оператор фискальных данных: (.+)", text),
    'Код ККМ КГД (РНМ)': re.search(r"Код ККМ КГД \(РНМ\): (.+)", text),
}

order_info = re.findall(r"\n(?P<order>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n", text)

with open('data.csv', 'w', newline='' ,encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data.keys())
    writer.writerow([v.group(1) if v else '' for v in data.values()])
    writer.writerow(['order', 'name', 'count', 'price'] + [''] * (len(data) - 4))  # Add empty strings for the missing columns
    for x in order_info:
        writer.writerow([
            x[0], 
            x[1],
            float(x[2].strip().replace(',','.')),
            float(x[3].strip().replace(',','.').replace(' ','')),
            '', '', '', '', '', '' 
        ])
