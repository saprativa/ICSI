import os
import xml.etree.ElementTree as ET



#load all the transcript files
transcripts_path = './ICSI_original_transcripts/transcripts'
transcript_files = os.listdir(transcripts_path)



#load all the abstractive summary files
abssum_path = './ICSIplus/Contributions/Summarization/abstractive'
abssum_files = os.listdir(abssum_path)



#collect all files which are present in both transcript and summarization folders
filelist=[]
for file in abssum_files:
    if f'{file[:-12]}.mrt' in transcript_files:
        filelist.append(f'{file[:-12]}.mrt')



#create the tanscript directory
if not os.path.exists("./transcripts"):
    os.makedirs("./transcripts")
    
    
    
#create the summaries directory 
if not os.path.exists("./abstractive_summaries"):
    os.makedirs("./abstractive_summaries")

    

#extract all the transcripts
for file in filelist:
    f = open(f'./transcripts/{file}.txt', 'w')
    tree = ET.parse(f'{transcripts_path}/{file}')
    root = tree.getroot()
    
    for child in root[1]:
        texts = child.itertext()
        for text in texts:
            if len(text.strip()) != 0:
                #print(text.strip(), end=' ')
                f.write(text.strip() + " ")
    f.close()
    
    

#extract all the abstractive summaries
for file in abssum_files:
    f = open(f'./abstractive_summaries/{file[:-4]}.txt', 'w')
    tree = ET.parse(f'{abssum_path}/{file}')
    root = tree.getroot()
    
    for section in root:
        for sentence in section:
            #print(sentence.text, end = " ")
            f.write(sentence.text.strip() + " ")
    f.close()
    
    
    
    
    
    
            