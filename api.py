import requests

resgeta = requests.get("https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/images")

# resget = requests.get("https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/image",
#                          params=query)

# respost = requests.post('https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/image',
#                          json = {'imgId':'4',
#                                  'altText': 'Fourth Image',
#                                  'imgUrl': 'https://drive.google.com/file/d/1tLeacAm7E4MYmTrwbgZHK4915olPf6Gu/view?usp=share_link'})

# resdel = requests.delete('https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/image',
#                          json = {'imgId':'4'})
                         
print(resgeta.json())