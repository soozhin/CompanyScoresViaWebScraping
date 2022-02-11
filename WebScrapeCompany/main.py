'''
Input: List of company names
Output: List of company review score from websites like "openwork"
'''
from random import random

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getWebsite(url):
    driver = webdriver.Chrome("/Users/limsoozhin/Documents/学校機関/室蘭工業大学/就活/WebScrapeCompany/chromedriver")
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    return soup

def getCompanyAndScore(soup, target_company, company_name_class):
    company_names = soup.find_all("div", class_=company_name_class)
    target_company_dict = {}
    for company_name in company_names:
        company = company_name.find("h3", attrs={"class":"fs-18 lh-1o3 p-r"})
        if target_company in company.text:
            company_score = company_name.find("p", attrs={"class":"totalEvaluation_item fs-15 fw-b"})
            target_company_dict[company.text.strip()] = company_score.text.strip()
    return target_company_dict

if __name__ == '__main__':
    print("This program outputs company review scores from openwork")

    company_name_class = "searchCompanyName"
    evaluation_class = "totalEvaluation_item fs-15 fw-b"
    company_list = ["株式会社ソフトクリエイトホールディングス", "株式会社ジャパンテクニカルソフトウェア", "セントラルソフト株式会社",
                    "株式会社ビッツ", "北海道旅客鉄道株式会社", "株式会社アルファシステムズ", "株式会社ユー・エス・イー",
                    "株式会社北海道キューブシステム", "株式会社ソフトコム", "アステック株式会社", "三菱電機エンジニアリング株式会社",
                    "東芝デベロップメントエンジニアリング株式会社", "インフォコム株式会社", "東京海上日動システムズ株式会社",
                    "株式会社カーネル・ソフト・エンジニアリング", "株式会社マースエンジニアリング", "サン情報サービス株式会社",
                    "株式会社ソフトウェア・サイエンス", "株式会社日立ソリューションズ", "株式会社クレスコ", "株式会社日本デジタル研究所",
                    "株式会社モビテック", "株式会社日立ハイシステム21", "北海道警察情報通信部", "クオリサイトテクノロジーズ株式会社",
                    "ジョンソンコントロールズ株式会社", "株式会社NTTデータMSE", "リコーITソリューションズ株式会社",
                    "株式会社メイテック", "日本製鉄株式会社", "株式会社iD", "北都システム株式会社",
                    "パナソニックITS株式会社", "日鉄テックスエンジ株式会社", "株式会社日立産業制御ソリューションズ",
                    "北海道総合通信網株式会社", "株式会社長大", "株式会社DNPデジタルソリューションズ", "株式会社DNP情報システム",
                    "株式会社朋栄", "ヤスダファインテ株式会社", "株式会社OKIソフトウェア", "株式会社ランドコンピュータ",
                    "株式会社内田洋行", "日本プロセス株式会社", "日本電気株式会社", "日本信号株式会社", "アクセンチュア株式会社",
                    "ほくでん情報テクノロジー株式会社", "テックスエンジソリューションズ株式会社", "株式会社OEC", "陣上工業株式会社",
                    "株式会社スマート・ソリューション・テクノロジー", "日商エレクトロニクス株式会社", "株式会社NSソリューションズ東京",
                    "株式会社コア北海道カンパニー", "キーウェアソリューションズ株式会社", "東芝デジタルソリューションズ株式会社",
                    "TIS北海道株式会社", "株式会社エスイーシー", "株式会社ユードム", "株式会社ズコーシャ", "株式会社ネクシス",
                    "常磐システムエンジニアリング株式会社", "インフォテクノ株式会社", "エクシオグループ株式会社",
                    "北海道NSソリューションズ株式会社", "株式会社SCC", "NTT東日本－北海道", "株式会社内田洋行ITソリューションズ",
                    "株式会社アットマークテクノ", "株式会社シーエスアイ", "株式会社第一システムエンジニアリング", "株式会社マイナビEdge",
                    "日本電営株式会社", "ドゥウェル株式会社", "株式会社アルトナー"]

    f = open("results.csv", "a")

    for target_company in company_list:
        url = f"https://www.vorkers.com/company_list?field=&pref=&src_str={target_company}&sort=1&ct=comlist"
        soup = getWebsite(url)
        target_company_dict = getCompanyAndScore(soup, target_company, company_name_class)
        for company in target_company_dict:
            result = company + ", " + target_company_dict[company] + "\n"
            f.write(result)
            print(result, end="")
        random_second = random()*100//10
        print("Sleep for ", random_second, "seconds")
        time.sleep(random_second)

    f.close()
