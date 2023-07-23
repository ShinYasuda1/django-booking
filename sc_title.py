import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox

def scrape_and_save():
    url = "https://hitsujienglish.com/"
    max_articles = 50  # 抽出する記事の最大数
    articles_per_page = 14  # 1ページあたりの記事数
    num_pages = max_articles // articles_per_page + 1  # 必要なページ数（1ページあたりの記事数で割って切り上げ）

    workbook = Workbook()
    sheet = workbook.active

    count = 0
    for page in range(1, num_pages + 1):
        page_url = f"{url}page/{page}/"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tags = soup.find_all('h3', class_='post-card-title')

        for i, title in enumerate(title_tags):
            if count >= max_articles:
                break
            sheet.cell(row=count + 1, column=1, value=title.text.strip())
            count += 1
            time.sleep(2)

    workbook.save("articles.xlsx")
    messagebox.showinfo("完了", f"{count}個の記事タイトルが抽出され、articles.xlsxに保存されました。")

# Tkinterウィンドウを作成
app = tk.Tk()
app.title("Webサイトスクレイピング")

# ボタンを配置
scrape_button = tk.Button(app, text="スクレイピング開始", command=scrape_and_save)
scrape_button.pack(pady=20)

app.mainloop()
