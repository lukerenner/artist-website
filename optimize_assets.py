import os
from PIL import Image, ImageOps

IMAGES_DIR = "public/images"
FAVICON_SOURCE = "public/images/hero/bonnie-hero-alt.webp" # Using hero alt as source
OG_SOURCE = "public/images/hero/bonnie-hero-alt.webp"

def convert_to_webp(root_dir):
    print("Converting images to WebP...")
    large_pngs = ['ecstasy.png', 'the-witnesses-project.png', 'piano-strip.png']
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                filename_no_ext = os.path.splitext(file_path)[0]
                webp_path = f"{filename_no_ext}.webp"
                
                # Determine quality based on file size/type
                quality = 90 if file in large_pngs else 85
                
                if not os.path.exists(webp_path):
                    try:
                        with Image.open(file_path) as img:
                            img.save(webp_path, "WEBP", quality=quality, method=6)
                            print(f"Converted: {file} -> {os.path.basename(webp_path)} (quality={quality})")
                    except Exception as e:
                        print(f"Error converting {file}: {e}")
                else:
                    # Re-optimize large PNGs even if WebP exists
                    if file in large_pngs:
                        try:
                            with Image.open(file_path) as img:
                                img.save(webp_path, "WEBP", quality=quality, method=6)
                                print(f"Re-optimized: {file} -> {os.path.basename(webp_path)} (quality={quality})")
                        except Exception as e:
                            print(f"Error re-optimizing {file}: {e}")
                    else:
                        print(f"Skipping (exists): {webp_path}")

def cleanup_redundant_originals(root_dir):
    """Remove JPG/PNG files that have WebP equivalents"""
    print("\nCleaning up redundant original files...")
    removed_count = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                filename_no_ext = os.path.splitext(file_path)[0]
                webp_path = f"{filename_no_ext}.webp"
                
                # Only delete if WebP version exists
                if os.path.exists(webp_path):
                    try:
                        os.remove(file_path)
                        removed_count += 1
                        print(f"Removed: {file}")
                    except Exception as e:
                        print(f"Error removing {file}: {e}")
    
    print(f"\nRemoved {removed_count} redundant original files.")

def generate_og_image():
    print("Generating OG Image...")
    output_dir = "public/og"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "og-image.jpg")
    
    if os.path.exists(OG_SOURCE):
        try:
            with Image.open(OG_SOURCE) as img:
                # Resize/Crop to 1200x630
                target_ratio = 1200 / 630
                img_ratio = img.width / img.height
                
                if img_ratio > target_ratio:
                    # Image is wider, crop width
                    new_width = int(img.height * target_ratio)
                    offset = (img.width - new_width) // 2
                    img = img.crop((offset, 0, offset + new_width, img.height))
                else:
                    # Image is taller, crop height
                    new_height = int(img.width / target_ratio)
                    offset = (img.height - new_height) // 2
                    img = img.crop((0, offset, img.width, offset + new_height))
                
                img = img.resize((1200, 630), Image.Resampling.LANCZOS)
                img.save(output_path, quality=90)
                print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error generating OG image: {e}")
    else:
        print(f"Source for OG image not found: {OG_SOURCE}")

def generate_favicons():
    print("Generating Favicons...")
    sizes = [
        (16, "public/favicon-16x16.png"),
        (32, "public/favicon-32x32.png"),
        (180, "public/apple-touch-icon.png"),
        (192, "public/android-chrome-192x192.png"),
        (512, "public/android-chrome-512x512.png")
    ]
    
    # Use a square crop of the source
    if os.path.exists(FAVICON_SOURCE):
        try:
            with Image.open(FAVICON_SOURCE) as img:
                # Square crop first
                min_dim = min(img.size)
                left = (img.width - min_dim) // 2
                top = (img.height - min_dim) // 2
                right = (img.width + min_dim) // 2
                bottom = (img.height + min_dim) // 2
                img = img.crop((left, top, right, bottom))
                
                for size, path in sizes:
                    resized = img.resize((size, size), Image.Resampling.LANCZOS)
                    resized.save(path)
                    print(f"Generated: {path}")
                    
                # Generate ICO
                img.resize((32, 32), Image.Resampling.LANCZOS).save("public/favicon.ico")
                print("Generated: public/favicon.ico")
                
        except Exception as e:
            print(f"Error generating favicons: {e}")
    else:
        print(f"Source for favicons not found: {FAVICON_SOURCE}")

if __name__ == "__main__":
    convert_to_webp(IMAGES_DIR)
    cleanup_redundant_originals(IMAGES_DIR)
    generate_og_image()
    generate_favicons()
