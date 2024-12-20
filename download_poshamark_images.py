from urllib import request
import os

# Specify the file name
file_name = 'Clothing_Data.csv'


img_url_index = 3 
product_id_index = 0

# Create a directory to save images
os.makedirs('downloaded_images', exist_ok=True)

c=0
# Open the CSV file and read the 'img_url' column
with open(file_name, 'r', encoding='utf-8') as file:
    # Loop through each line in the file
    for line in file:
        # Split the line by commas
        row = line.strip().split(',')
        
        # Get the img_url value
        img_url = row[img_url_index]
        product_id = row[product_id_index]
        
        # Download the image
        try:
            response = request.urlopen(img_url)
                
            # Save the image
            img_path = 'Images\\' + product_id + ".jpg"
            with open(img_path, 'wb') as img_file:
                img_file.write(response.read())
            
            print(f"Downloaded {img_url}")
            
            c+=1
            if c%10==0:
                print(c)
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")
