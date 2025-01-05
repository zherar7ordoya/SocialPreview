from PIL import Image, ImageDraw, ImageFont

def create_topgun_style_preview():
    # Get repository details from the user
    repo_name = input("Repository name: ")
    description = input("Short description: ")
    technologies = input("Technologies used (comma-separated): ")
    output_path = input("Output file name (e.g., preview.png): ")

    # Set image dimensions
    width, height = 1280, 640
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Background: Sky-like gradient
    for i in range(height):
        color = (135, 206, 235 - i // 4, 255)  # Light blue to white
        draw.line([(0, i), (width, i)], fill=color)

    # Fonts
    font_title = ImageFont.truetype("arial.ttf", 64)
    font_desc = ImageFont.truetype("arial.ttf", 36)

    # Add a bold stripe (red) for decoration
    # stripe_height = 50
    # draw.rectangle(
    #     [(0, height // 2 - stripe_height // 2), (width, height // 2 + stripe_height // 2)],
    #     fill=(255, 0, 0),
    # )

    # Add repository name
    title = repo_name.upper()
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    text_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - text_width) // 2, height // 2 - 80), title, fill="white", font=font_title)

    # Add description
    desc_bbox = draw.textbbox((0, 0), description, font=font_desc)
    desc_width = desc_bbox[2] - desc_bbox[0]
    draw.text(((width - desc_width) // 2, height // 2 + 20), description, fill="white", font=font_desc)

    # Add technologies
    techs = f"Technologies: {technologies}"
    techs_bbox = draw.textbbox((0, 0), techs, font=font_desc)
    tech_width = techs_bbox[2] - techs_bbox[0]
    draw.text(((width - tech_width) // 2, height // 2 + 80), techs, fill="white", font=font_desc)

    # Save the image
    image.save(output_path)
    print(f"Image generated and saved as {output_path}")

if __name__ == "__main__":
    create_topgun_style_preview()
