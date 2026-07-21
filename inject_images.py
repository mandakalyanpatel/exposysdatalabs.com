import re

with open('Aca6.html', 'r', encoding='utf-8') as f:
    content = f.read()

images = [
    'train_ml.png',
    'train_nlp.png',
    'train_ai.png',
    'train_ds.png',
    'train_c.png',
    'train_net.png',
    'train_web.png',
    'train_java.png',
    'train_bot.png'
]

# We want to replace `<div class="course-icon">` with `<img src="IMAGE_NAME" class="course-image-top"><div class="course-icon">`
# But we need to do this sequentially for all 9 courses.

parts = content.split('<div class="course-icon">')
if len(parts) == 10: # 1 before the first, and 9 after
    new_content = parts[0]
    for i in range(9):
        new_content += f'<img src="{images[i]}" alt="Course Image" class="course-image-top">\n                <div class="course-icon">' + parts[i+1]
        
    with open('Aca6.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Images injected successfully.")
else:
    print(f"Error: Found {len(parts)-1} course icons instead of 9.")
