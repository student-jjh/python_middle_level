import requests

datas = {
        'cargoReferenceNo' : '11TEST11',
        'portEntryDate' : '2022-03-08',
        'carryDate' : '2022-03-08 01:01:01',
        'cyTerminal' : 'TEST4',
        'houseBlNo': 'ONEYMEXV02369400'
        }


response = requests.post('http://192.168.0.77:8888/api/setCargoNo', data = datas)

print(response.content)
# print(response.json())
# print(response.text)