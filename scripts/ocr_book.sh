#!/bin/bash
# OCR Book Script - Uses macOS Vision Framework to OCR scanned PDFs
# Usage: ./ocr_book.sh <pdf_path> [start_page] [end_page]
# Output: text file in same directory as PDF

PDF_PATH="$1"
START_PAGE="${2:-1}"
END_PAGE="${3:-0}"  # 0 means all pages
OUTPUT_DIR="/tmp/ocr_book_output"

mkdir -p "$OUTPUT_DIR"

# Get total pages
TOTAL_PAGES=$(python3 -c "
import fitz
doc = fitz.open('$PDF_PATH')
print(len(doc))
doc.close()
")

if [ "$END_PAGE" -eq 0 ] || [ "$END_PAGE" -gt "$TOTAL_PAGES" ]; then
    END_PAGE=$TOTAL_PAGES
fi

echo "OCR processing: $PDF_PATH"
echo "Pages: $START_PAGE to $END_PAGE (total: $TOTAL_PAGES)"
echo "Output: $OUTPUT_DIR"

# Extract pages as images using pymupdf
python3 -c "
import fitz
doc = fitz.open('$PDF_PATH')
for i in range($START_PAGE - 1, $END_PAGE):
    page = doc[i]
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    pix.save(f'$OUTPUT_DIR/page_{i+1:04d}.png')
    if (i + 1) % 50 == 0:
        print(f'Extracted {i+1} pages...')
doc.close()
print(f'Extraction complete: {$END_PAGE - $START_PAGE + 1} pages')
"

# OCR each page using macOS Vision
OUTPUT_TEXT="${PDF_PATH%.pdf}_OCR.txt"
> "$OUTPUT_TEXT"  # Clear output file

for img in $(ls "$OUTPUT_DIR"/page_*.png 2>/dev/null | sort); do
    page_num=$(basename "$img" .png | sed 's/page_0*//')
    echo "" >> "$OUTPUT_TEXT"
    echo "========== 第 ${page_num} 页 ==========" >> "$OUTPUT_TEXT"
    swift /tmp/ocr_vision.swift "$img" >> "$OUTPUT_TEXT" 2>/dev/null
    echo "OCR'd page $page_num"
done

echo "OCR complete! Output: $OUTPUT_TEXT"
echo "Total pages processed: $(($END_PAGE - $START_PAGE + 1))"

# Cleanup images
rm -rf "$OUTPUT_DIR"
