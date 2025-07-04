import scrapy
from ADCB_UAE.items import Product
from lxml import html
import os
from datetime import date
import pandas as pd



def clean(text):
    if not text:
        return None
    return ' '.join(''.join(text).split()).strip()

class AdcbUaeSpider(scrapy.Spider):
    name = "ADCB_UAE"

    def start_requests(self):
        # items_list = []
        folder_path = os.path.dirname(os.path.abspath(__file__))
        c = 0
        for file_name in os.listdir(folder_path):
        #     if '-' not in file_name:
        #         items_list.append(file_name.split('.')[0])
        # df = pd.DataFrame(items_list)

        # df.to_csv('cid.csv', index=False)
        # # print(items_list)
            if file_name.endswith(".mhtml") and '-' not in file_name:
                c += 1
                print(file_name)
                file_path = f"file://{os.path.abspath(os.path.join(folder_path, file_name))}"
                yield scrapy.Request(
                    url=file_path,
                    callback=self.parse,
                )
                # return
        print(f'Request count : {c}')

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
        
        try:
            Region = [
                item for item in str(cleaned_text).split('Region')[-1].strip().split('</td>') if item.strip()
                ][0].split('nowrap="">')[-1].strip().replace('=', '').strip().split('"data">')[-1].replace('&nbsp;', '')
        except Exception as e:
            print(e)
            Region = ''
        if '</td>' in Region:
            Region = Region.split('</td>')[0].strip()

        address1 = address1.split('</td>')[0].strip() if '</td>' in address1 else address1
        address = clean(', '.join(list(filter(None, [address1,address2,address3]))))
        scrape_date = date.today()
        # scrape_date = '2025-04-24'
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
                data['cid_no'] = cid_no.replace('&nbsp;', '') if cid_no else ''
                data['nationality'] = nationality.replace('&nbsp;', '') if nationality else ''
                data['passport_no'] = passport_no.replace('&nbsp;', '').replace('td> 09 09', '') if passport_no else ''
            elif 'Name' in data_items:
                gender_date_of_birth = data_items.get('Gender  /  Date Of Birth', '').split('/')
                gender, date_of_birth = gender_date_of_birth[0].strip(), gender_date_of_birth[-1].strip()
                # office_number = data_items.get('Office1  /  Office 2 Number', '').replace('/', '').strip()
                data['name'] = clean(data_items.get('Name', '')).replace('&nbsp;', '')
                data['gender'] = clean(gender).replace('&nbsp;', '') if gender else ''
                data['date_of_birth'] = clean(date_of_birth).replace('&nbsp;', '') if date_of_birth else ''
        data['total_os'] = clean(total_os_elements).replace('&nbsp;', '') if len(total_os_elements) < 80 else None
        data['employer_name'] = clean(employer_name).replace('&nbsp;', '') if employer_name and len(employer_name) < 80 else None
        data['Mobile_Number'] = clean(Mobile_Number).replace('&nbsp;', '') if len(Mobile_Number) < 80 else None
        data['Office_Numbers'] = clean(Office_Numbers).replace('&nbsp;', '') if len(Office_Numbers) < 80 else None
        data['Reference_name_mobile'] = clean(Ref_name_mobile).replace('&nbsp;', '') if Ref_name_mobile and len(Ref_name_mobile) < 300 else None
        data['Email_ID'] = clean(Email_ID).replace('&nbsp;', '') if len(Email_ID) < 80 else None
        data['Home_Country_Number'] = clean(Home_Country_Number).replace('&nbsp;', '') if Home_Country_Number and len(Home_Country_Number) < 80 else None
        data['Designation_Occupation'] = clean(Designation_Occupation).replace('&nbsp;', '') if Designation_Occupation and len(total_os_elements) < 400 else None
        data['Emirates_id'] = clean(Emirates_id).replace('&nbsp;', '') if Emirates_id and len(Emirates_id) < 80 else None
        data['address'] = clean(address).replace('&nbsp;', '').replace('&nbs p;', '').replace('< /td>', '').replace('09 09', '').replace('20,', '').replace('<font color"black">.</font>,', "").strip() if address and address else None
        data['Residence_number'] = clean(Residence_number).replace('&nbsp;', '') if Residence_number and len(Residence_number) < 80 else None
        data['scrape_date'] = str(scrape_date).replace('&nbsp;', '') if scrape_date else ''
        data['Region'] = str(Region).replace('&nbsp;', '') if Region and len(Region) < 80 else ''
        yield Product(**data)
