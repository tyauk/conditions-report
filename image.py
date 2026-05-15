import requests
import xmltodict
from PIL import Image, ImageDraw, ImageFont


url = 'https://snowreporting.herokuapp.com/feed?format=xml&resortId=3'
response = requests.get(url)
data = ""


img = Image.open("BMR-FY25-CR-Data-Image-CRM-Blank.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("GoogleSans_17pt-Bold.ttf", size=60)
status = ImageFont.truetype("GoogleSans_17pt-Bold.ttf", size=35)





def save():
    img.save('image.png')






def learningCentres(lc):

    if ("Open" in lc[0]) or ("Open" in lc[1]) or ("Open" in lc[2]):
        draw.text((690,1490), "OPEN", font=status, fill=(36,217,36))
    else:
        draw.text((690,1490), "CLOSED", font=status, fill=(217,67,41))


    if ("Open" in lc[3]) or ("Open" in lc[4]) or ("Open" in lc[5]):
        draw.text((690,1290), "OPEN", font=status, fill=(36,217,36))
    else:
        draw.text((690,1290), "CLOSED", font=status, fill=(217,67,41))


    save()




def populateLifts(lifts,lc):

    if "Open" in lifts[0] or "Scheduled" in lifts[0]:
        draw.text((690,820), "OPEN", font=status, fill=(36,217,36))
    elif "Closed" in lifts[0]:
        draw.text((690,820), lifts[0].upper(), font=status, fill=(217,67,41))



    if "Open" in lifts[1] or "Scheduled" in lifts[1]:
        draw.text((170,820), "OPEN", font=status, fill=(36,217,36))
    elif "Closed" in lifts[1]:
        draw.text((170,820), lifts[1].upper(), font=status, fill=(217,67,41))



    if "Open" in lifts[2] or "Scheduled" in lifts[2]:
        draw.text((170,270), "OPEN", font=status, fill=(36,217,36))
    elif "Closed" in lifts[2]:
        draw.text((170,270), lifts[2].upper(), font=status, fill=(217,67,41))



    if "Open" in lifts[3] or "Scheduled" in lifts[3]:
        draw.text((170,1355), "OPEN", font=status, fill=(36,217,36))
    elif "Closed" in lifts[3]:
        draw.text((170,1355), lifts[3].upper(), font=status, fill=(217,67,41))



    if "Open" in lifts[4] or "Scheduled" in lifts[4]:
        draw.text((690,270), "OPEN", font=status, fill=(36,217,36))
    elif "Closed" in lifts[4]:
        draw.text((690,270), lifts[4].upper(), font=status, fill=(217,67,41))



    learningCentres(lc)





def populateTrails(openT,totalT,lifts,lc):
    #VILLAGE TRAILS
    draw.text((170,320), (openT[2] + "/" + totalT[2]), font=font, fill=(255,255,255))
    
    #NORTH TRAILS
    draw.text((690,320), (openT[4] + "/" + totalT[4]), font=font, fill=(255,255,255))
    
    #SOUTH TRAILS
    draw.text((170,870), (openT[1] + "/" + totalT[1]), font=font, fill=(255,255,255))
    
    #ORCHARD TRAILS
    draw.text((690,870), (openT[0] + "/" + totalT[0]), font=font, fill=(255,255,255))
    
    #VALLEY TRAILS
    draw.text((170,1405), (openT[3] + "/" + totalT[3]), font=font, fill=(255,255,255))

    populateLifts(lifts,lc)





def getData():

    areas = data['ResortFeedViewModel']['MountainAreas']['MountainArea']
    openTrails = []
    totalTrails = []
    lifts = []
    lc = []

    for i in range(len(areas)):
        openTrails.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][i]['OpenTrailsCount'])
        totalTrails.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][i]['TotalTrailsCount'])

    lifts.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][0]['Lifts']['Lift']['Status'])
    lifts.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][1]['Lifts']['Lift'][2]['Status'])
    lifts.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][2]['Lifts']['Lift'][2]['Status'])
    lifts.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][3]['Lifts']['Lift']['Status'])
    lifts.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][4]['Lifts']['Lift']['Status'])

    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][1]['Lifts']['Lift'][0]['Status'])
    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][1]['Lifts']['Lift'][1]['Status'])
    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][1]['Lifts']['Lift'][3]['Status'])

    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][2]['Lifts']['Lift'][0]['Status'])
    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][2]['Lifts']['Lift'][1]['Status'])
    lc.append(data['ResortFeedViewModel']['MountainAreas']['MountainArea'][2]['Lifts']['Lift'][3]['Status'])

    populateTrails(openTrails,totalTrails,lifts,lc)





if response.status_code == 200:
    data = xmltodict.parse(response.text)

    getData()
else:
    print(f"Failed to retrieve data: {response.status_code}")


