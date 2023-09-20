# pdfTableJson
Extract tables data from pdf files To JSON

## Installation
- Rquired Python >= 3.8
- install with pip
```
pip install pdfTableJson
```

## Example
#### import
```py
import pdfTableJson.converter as converter

path = "PATH/PDF_NAME.pdf"
result = converter.main(path)
print(result)
```

#### CLI
```py
python a.py -i "pdf_path/pdf_name.pdf" -j -p
```

## License
- GPL-3.0 license

## Contact
- [@yousojeong](https://github.com/yousojeong)
