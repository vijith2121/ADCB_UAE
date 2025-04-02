import scrapy
from ADCB_UAE.items import Product
from lxml import html
import os
import re
from scrapy_playwright.page import PageMethod
import html as html_parser


def clean(text):
    if not text:
        return None
    return ' '.join(''.join(text).split()).strip()

class AdcbUaeSpider(scrapy.Spider):
    name = "ADCB_UAE"

    custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "DOWNLOAD_HANDLERS": {"http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler"},
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": 30000,
    }

    def start_requests(self):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".mhtml"):
                # file_path = f"file://{os.path.abspath(os.path.join(folder_path, file_name))}"
                # file_path = 'file:///home/vijith/Downloads/DHANOOP%20KALLINGAPURAM%20SUDHARMAN.mhtml'
                # file_path = 'file:///home/vijith/Desktop/vijith/spiders/ADCB_UAE/ADCB_UAE/spiders/878561.mhtml'
                # file_path = 'file:///home/vijith/Downloads/DHANOOP%20KALLINGAPURAM%20SUDHARMAN.mhtml'
                # print(file_path)
                # file_path = 'file:///home/vijith/Downloads/DHANOOP%20KALLINGAPURAM%20SUDHARMAN.mhtml'
                file_path = 'file:///home/vijith/Desktop/vijith/spiders/ADCB_UAE/ADCB_UAE/spiders/878561.mhtml'
                yield scrapy.Request(
                    url=file_path,
                    callback=self.parse,
                )
                return

    def parse(self, response):
        parser = html.fromstring(response.text)

        xpath_address2 = "//td[contains(text(), 'Address')]//parent::tr//following-sibling::tr[1]/td[2]//text()"
        xpath_address3 = "//td[contains(text(), 'Address')]//parent::tr//following-sibling::tr[2]/td[2]//text()"
        xpath_data = "//td[contains(text(), 'CID No.')]//parent::tr//parent::tbody//tr"

        cleaned_text = response.text.replace("=3D", "=").replace("\n", "").replace("\r", "").replace("\t", "").replace("&nbsp;", " ").strip()

        address2 = ''.join(parser.xpath(xpath_address2)).strip().replace('=', '')
        address3 = ''.join(parser.xpath(xpath_address3)).strip().replace('=', '').replace('&nbs', '').replace('p;', '')
        try:
            total_os_elements = [
                item for item in cleaned_text.split('Total OS', 1)[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip()
        except Exception as e:
            print(e)
            total_os_elements = ''
        if '</td>' in total_os_elements:
            total_os_elements = total_os_elements.split('</td>')[0].strip()
        try:
            employer_name = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Employer Name', 1)[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1]
        except Exception as e:
            print(e)
            employer_name = ''
        if '</td>' in employer_name:
            employer_name = employer_name.split('</td>')[0].strip()
        try:
            Mobile_Number = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Mobile Number', 1)[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Mobile_Number = ''
        if '</td>' in Mobile_Number:
            Mobile_Number = Mobile_Number.split('</td>')[0].strip()
        try:
            Office_Numbers  = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Office1  /  Of=fice 2 Number')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Office_Numbers = ''
        if '</td>' in Office_Numbers:
            Office_Numbers = Office_Numbers.split('</td>')[0].strip()
        try:
            Ref_name_mobile  = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Ref Name  /  R=ef Mob')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Ref_name_mobile = ''
        if '</td>' in Ref_name_mobile:
            Ref_name_mobile = Ref_name_mobile.split('</td>')[0].strip()
        try:
            Email_ID  = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Email ID =')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Email_ID = ''
        try:
            Home_Country_Number  = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Home Country N=umber')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Home_Country_Number = ''
        if '</td>' in Home_Country_Number:
            Home_Country_Number = Home_Country_Number.split('</td>')[0].strip()
        try:
            Designation_Occupation = [
                item for item in cleaned_text.replace('&=nbsp;', '').split('Designation  /=  Occupation')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Designation_Occupation = ''

        if '</td>' in Designation_Occupation:
            Designation_Occupation = Designation_Occupation.split('</td>')[0].strip()

        try:
            Emirates_id = [
                item for item in str(cleaned_text).replace('&nb=sp;', '').split('Emirates ID')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Emirates_id = ''
        if '</td>' in Emirates_id:
            Emirates_id = Emirates_id.split('</td>')[0].strip()
        try:
            address1 = [
                item for item in str(cleaned_text).split('class="ez1">Address')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            address1 = ''
        try:
            Residence_number = [
                item for item in str(cleaned_text).split('Residence1  / = Residence 2 Number')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Residence_number = ''
        if '</td>' in Residence_number:
            Residence_number = Residence_number.split('</td>')[0].strip()

        address1 = address1.split('</td>')[0].strip() if '</td>' in address1 else address1
        address = clean(', '.join(list(filter(None, [address1,address2,address3]))))
        items = parser.xpath(xpath_data)
        data = {}
        for item in items:
            items1 = item.xpath('.//td[contains(@class, "ez1")]//text()')
            items2 = item.xpath('.//td[contains(@class, "data")]//text()')
            data1 = [
                i.strip().replace('\r\n', '').replace('&nbs=p;', '').replace('&=nbsp;', '').replace('&nbsp=;', '').replace('=', '').replace('&nbsp;', '') for i in items1 if i.strip().replace('\r\n', '').replace('&nbs=p;', '')
            ]
            data2 = [
                i.strip().replace('\r\n', '').replace('&nbs=p;', '').replace('&=nbsp;', '').replace('&nbsp=;', '').replace('=', '').replace('&nbsp;', '') for i in items2 if i.strip().replace('\r\n', '').replace('&nbs=p;', '')
            ]
            data_items = dict(zip(data1, data2))
            if 'CID No.' in data_items:
                cid_no = clean(''.join(data_items.get('CID No.', '')).strip())
                nationality_passport = data_items.get('Nationality  /  Passport', '').split('/')
                nationality, passport_no = clean(''.join(nationality_passport[0]).strip()), clean(''.join(nationality_passport[-1]).strip())
                data['cid_no'] = cid_no
                data['nationality'] = nationality
                data['passport_no'] = passport_no
            elif 'Name' in data_items:
                gender_date_of_birth = data_items.get('Gender  /  Date Of Birth', '').split('/')
                gender, date_of_birth = gender_date_of_birth[0].strip(), gender_date_of_birth[-1].strip()
                office_number = data_items.get('Office1  /  Office 2 Number', '').replace('/', '').strip()
                data['name'] = clean(data_items.get('Name', ''))
                data['gender'] = clean(gender)
                data['date_of_birth'] = clean(date_of_birth)

        data['total_os'] = clean(total_os_elements) if total_os_elements else None
        data['employer_name'] = clean(employer_name) if employer_name else None
        data['Mobile_Number'] = clean(Mobile_Number) if Mobile_Number else None
        data['Office_Numbers'] = clean(Office_Numbers) if Office_Numbers else None
        data['Reference_name_mobile'] = clean(Ref_name_mobile) if Ref_name_mobile else None
        data['Email_ID'] = clean(Email_ID) if Email_ID else None
        data['Home_Country_Number'] = clean(Home_Country_Number) if Home_Country_Number else None
        data['Designation_Occupation'] = clean(Designation_Occupation) if Designation_Occupation else None
        data['Emirates_id'] = clean(Emirates_id) if Emirates_id else None
        data['address'] = clean(address) if address else None
        data['Residence_number'] = clean(Residence_number) if Residence_number else None
        yield Product(**data)