from requests import session
import os,sys


class Convertico:
    def __init__(self,target_img_path):
        self.api_url = "https://convertico.com/convert_script.php"
        self.file_path = target_img_path
        print(self.file_path)

    def create_session(self):
        sess = session()
        headers = {
            "authority": "convertico.com",
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            # "cookie": "bsau=17082336602642368391; __utma=130953885.1204855630.1707765589.1708233660.1708322812.4; __utmc=130953885; __utmz=130953885.1708322812.4.4.utmcsr=google^|utmccn=(organic)^|utmcmd=organic^|utmctr=(not^%^20provided); __utmt=1; __utmb=130953885.1.10.1708322812; bsas=17083228124842530524; __gads=ID=d9a7dc368c0a223c:T=1707765588:RT=1708322814:S=ALNI_Mb5XiJdmTTBFf13XiedN1tvqpAv3Q; __gpi=UID=00000d1fea302e4e:T=1707765588:RT=1708322814:S=ALNI_MYqhIxamtcQ9nbDPqjzlzEQ5Yfoiw; __eoi=ID=f3bd0c982737f387:T=1707765588:RT=1708322814:S=AA-AfjYyW2Zf53I-Ou6FmyPT0k68; FCNEC=^%^5B^%^5B^%^22AKsRol9SNwy_-I9_PciFOYrPPRZwJLbWni-jGUl8zMJ4ARRwcaMEGYe2wMOg4S0IphmIHhZEcpyIfWOBUVuYdfHUzQ0w9Emedwd-98TIIqVNfi5Db8dBrEplNvwLplN4RYXV4MwQtm3RLmAVCcnPrrEtVxZLJuEoUg^%^3D^%^3D^%^22^%^5D^%^5D",
            "origin": "https://convertico.com",
            "referer": "https://convertico.com/",
            "sec-ch-ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            "x-requested-with": "XMLHttpRequest",
        }
        sess.headers.update(headers)
        return sess
    
    def get_file_info(self, file_path: str):
        img_name = os.path.basename(file_path)
        img_type = os.path.splitext(img_name)[-1][1:]
        files = {
            "imgfile": (img_name, open(img_name, "rb")),
        }
        file_info = {
            'img_name': img_name,
            'files': files,
            'type': img_type
        }
        return file_info

        
    def convert(self, sess,file_info: str):
        files = file_info['files']
        img_type = file_info['type']
        data = {
            "from": str, # -> png or jpg or jpeg or svg
            "into": "ico",
            "name": str, # -> png-to-ico or jpg-to-ico or jpeg-to-ico or svg-to-ico
            "hidden": "",
            "size256": "1",
            "size128": "1",
            "size64": "1",
            "size48": "1",
            "size40": "0",
            "size32": "1",
            "size24": "0",
            "size20": "0",
            "size16": "1",
        }
        data['from'] = img_type
        data['name'] = f"{img_type}-to-ico"
        response = sess.post(self.api_url, data=data, files=files)
        if response.status_code == 200:
            return response.json()
    
    def save_ico(self, sess,ico_data: dict):
        '''
        {'log': ['images/1708323812.2771/logo-ec--en.svg'],
        'initialType': 'SVG',
        'type': 'ico',
        'original': '/images/1708323812.2771/logo-ec--en.svg',
        'folder_name': 1708323812.27715,
        'New': '/images/1708323812.2771/logo-ec--en.ico',
        'size': 113290,
        'name': 'logo-ec--en',
        'preview': '/images/1708323812.2771/_previmg.png'}
        '''
        domain = 'https://convertico.com'
        ico_url = domain + ico_data['New']
        ico_name = ico_data['name']
        ico_rsp = sess.get(ico_url)
        if ico_rsp.status_code == 200:
            ico_name = f"{ico_name}.ico"
            ico_path = os.path.join(os.path.dirname(self.file_path), ico_name)
            with open(ico_path, "wb") as ico_file:
                ico_file.write(ico_rsp.content)

    def main(self):
        file_path = self.file_path
        sess = self.create_session()
        file_info = self.get_file_info(file_path)
        ico_data = self.convert(sess, file_info)
        self.save_ico(sess, ico_data)


if __name__ == "__main__":
    # Get file path from command line argument
    target_img_path = sys.argv[1]
    convertico = Convertico(target_img_path)
    convertico.main()