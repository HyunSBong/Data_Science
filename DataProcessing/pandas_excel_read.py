import pandas as pd

filename = "stats_104102.xlsx" # 파일 이름
sheet_name = "stats_104102" # 시트 이름
book = pd.read_excel(filename, sheet_name=sheet_name, header=1) # 첫 번째 줄부터 헤더

# 2018년 인구로 정렬
book = book.sort_values(by=2018, ascending=False)
print(book)